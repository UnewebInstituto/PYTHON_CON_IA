"""
Chatbot RAG local con Ollama + LangChain + ChromaDB + Streamlit
----------------------------------------------------------------
Analiza documentos (PDF, DOCX, TXT) y responde preguntas basándose
en su contenido, usando un LLM 100% local (Llama 3 vía Ollama).

Cómo ejecutar:
    pip install -r requirements.txt
    ollama pull llama3            # si no lo tienes descargado ya
    streamlit run app.py
"""

import os
import tempfile

import streamlit as st
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------------------------------
# Configuración general
# --------------------------------------------------------------------------
PERSIST_DIR = "chroma_db"          # carpeta donde se guarda el vector store

# NOTA: valores ajustados para equipos con recursos limitados
# (8 GB RAM total, sin GPU dedicada, ej. Lenovo IdeaPad 5 Pro i5-11300H).
# Si tu equipo tiene más RAM/GPU, puedes volver a modelos más grandes
# como "llama3" (8B) y "paraphrase-multilingual-mpnet-base-v2".
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
OLLAMA_MODEL = "phi3:mini"          # ~2.3 GB en RAM (quantizado Q4 por defecto en Ollama)
CHUNK_SIZE = 800                    # fragmentos más pequeños = menos contexto que procesar
CHUNK_OVERLAP = 100
TOP_K = 3                           # menos fragmentos recuperados = respuestas más rápidas

st.set_page_config(page_title="Asistente RAG local", page_icon="🤖")
st.title("🤖 Asistente inteligente sobre tus documentos")
st.caption("100% local · Ollama + Llama 3 + ChromaDB")

# --------------------------------------------------------------------------
# Utilidades: cargar documentos según su extensión
# --------------------------------------------------------------------------
def cargar_documento(ruta_temporal: str, nombre_original: str):
    """Devuelve una lista de objetos Document según el tipo de archivo."""
    extension = nombre_original.lower().split(".")[-1]

    if extension == "pdf":
        loader = PyPDFLoader(ruta_temporal)
    elif extension == "docx":
        loader = Docx2txtLoader(ruta_temporal)
    elif extension == "txt":
        loader = TextLoader(ruta_temporal, encoding="utf-8")
    else:
        raise ValueError(f"Formato no soportado: .{extension}")

    return loader.load()


@st.cache_resource(show_spinner=False)
def obtener_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def procesar_archivos(archivos_subidos):
    """Carga, fragmenta e indexa los documentos subidos en ChromaDB."""
    documentos = []

    for archivo in archivos_subidos:
        # Streamlit entrega el archivo en memoria; lo guardamos temporalmente
        # porque los loaders de LangChain necesitan una ruta en disco.
        sufijo = "." + archivo.name.split(".")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=sufijo) as tmp:
            tmp.write(archivo.getvalue())
            ruta_tmp = tmp.name

        try:
            docs = cargar_documento(ruta_tmp, archivo.name)
            for d in docs:
                d.metadata["fuente"] = archivo.name
            documentos.extend(docs)
        finally:
            os.remove(ruta_tmp)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    fragmentos = splitter.split_documents(documentos)

    embeddings = obtener_embeddings()
    vectorstore = Chroma.from_documents(
        documents=fragmentos,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
    )
    return vectorstore, len(documentos), len(fragmentos)


def construir_cadena_rag(vectorstore):
    """Construye la cadena LCEL: retriever -> prompt -> LLM -> parser."""
    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    plantilla = ChatPromptTemplate.from_template(
        """Eres un asistente que responde preguntas basándose EXCLUSIVAMENTE
en el siguiente contexto extraído de los documentos del usuario.
Si la respuesta no está en el contexto, di claramente que no la
encontraste en los documentos disponibles. Responde en español,
de forma clara y concisa.

Contexto:
{contexto}

Pregunta: {pregunta}

Respuesta:"""
    )

    llm = OllamaLLM(model=OLLAMA_MODEL, temperature=0.2)

    def formatear_contexto(docs):
        return "\n\n".join(
            f"[Fuente: {d.metadata.get('fuente', 'desconocida')}]\n{d.page_content}"
            for d in docs
        )

    cadena = (
        {"contexto": retriever | formatear_contexto, "pregunta": RunnablePassthrough()}
        | plantilla
        | llm
        | StrOutputParser()
    )
    return cadena


# --------------------------------------------------------------------------
# Estado de sesión
# --------------------------------------------------------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "cadena" not in st.session_state:
    st.session_state.cadena = None
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# --------------------------------------------------------------------------
# Barra lateral: carga de documentos
# --------------------------------------------------------------------------
with st.sidebar:
    st.header("📄 Documentos")
    archivos = st.file_uploader(
        "Sube tus documentos (PDF, DOCX, TXT)",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True,
    )

    if st.button("Procesar documentos", type="primary", disabled=not archivos):
        with st.spinner("Cargando, fragmentando e indexando documentos..."):
            vectorstore, n_docs, n_frag = procesar_archivos(archivos)
            st.session_state.vectorstore = vectorstore
            st.session_state.cadena = construir_cadena_rag(vectorstore)
        st.success(f"Listo: {n_docs} documento(s) → {n_frag} fragmentos indexados.")

    st.divider()
    st.caption(f"Modelo LLM: `{OLLAMA_MODEL}` (local vía Ollama)")
    st.caption(f"Embeddings: `{EMBEDDING_MODEL}`")

    if st.session_state.cadena and st.button("🗑️ Reiniciar conversación"):
        st.session_state.mensajes = []
        st.rerun()

# --------------------------------------------------------------------------
# Interfaz de chat
# --------------------------------------------------------------------------
if st.session_state.cadena is None:
    st.info("👈 Sube uno o varios documentos y pulsa **Procesar documentos** para empezar.")
else:
    # Mostrar historial
    for msg in st.session_state.mensajes:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    pregunta = st.chat_input("Escribe tu pregunta sobre los documentos...")

    if pregunta:
        st.session_state.mensajes.append({"role": "user", "content": pregunta})
        with st.chat_message("user"):
            st.markdown(pregunta)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                respuesta = st.session_state.cadena.invoke(pregunta)
                st.markdown(respuesta)

        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
