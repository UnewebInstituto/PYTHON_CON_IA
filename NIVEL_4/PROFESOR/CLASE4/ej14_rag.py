!pip install -q langchain langchain-community langchain-huggingface langchain-chroma chromadb sentence-transformers pypdf

# Instalar la dependencia zstd que requiere el instalador de Ollama
!sudo apt-get update -qq
!sudo apt-get install -y zstd

# Ahora sí, instalar Ollama dentro de la máquina virtual de Colab
!curl -fsSL https://ollama.com/install.sh | sh


import subprocess
import time

# Arrancar el servicio de Ollama en segundo plano
proceso_ollama = subprocess.Popen(["ollama", "serve"])
time.sleep(5)  # dar tiempo a que el servicio levante

print("Ollama corriendo en segundo plano.")


# Descargar el modelo (puede tardar varios minutos, pesa varios GB)
!ollama pull llama3


from langchain_community.document_loaders import PyPDFLoader
from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# Cargar el PDF
ruta_pdf = "/content/drive/MyDrive/data/manual_calidad_arroz.pdf"
loader = PyPDFLoader(ruta_pdf)
documentos = loader.load()

print(f"Documento cargado. Total de páginas: {len(documentos)}")



from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
textos = text_splitter.split_documents(documentos)

print(f"Total de fragmentos generados: {len(textos)}")


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Embeddings locales (multilingüe, funciona bien en español)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Crear la base de datos vectorial
db = Chroma.from_documents(textos, embeddings)

print("Base de datos vectorial creada correctamente.")

!pip show langchain


from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Modelo local vía Ollama
llm = OllamaLLM(model="llama3")

# Retriever (busca los fragmentos más relevantes del PDF)
retriever = db.as_retriever()

# Prompt que combina el contexto recuperado con la pregunta
prompt = ChatPromptTemplate.from_template("""
Responde la pregunta basándote únicamente en el siguiente contexto.
Si no encuentras la respuesta en el contexto, dilo claramente.

Contexto:
{context}

Pregunta: {question}
""")

def formatear_documentos(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Cadena RAG usando LCEL
qa_chain = (
    {"context": retriever | formatear_documentos, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("Cadena RAG lista para consultas.")

!pip install -q langchain langchain-community langchain-huggingface langchain-chroma langchain-ollama chromadb sentence-transformers pypdf


pregunta = "¿Cuáles son los estándares de humedad aceptados para el lote de arroz?"

respuesta = qa_chain.invoke(pregunta)

print("PREGUNTA:", pregunta)
print("\nRESPUESTA:", respuesta)

# Si quieres ver también las fuentes usadas:
docs_relevantes = retriever.invoke(pregunta)
print("\n--- Fuentes utilizadas ---")
for i, doc in enumerate(docs_relevantes, 1):
    pagina = doc.metadata.get("page", "N/A")
    print(f"{i}. Página {pagina}: {doc.page_content[:150]}...")
    
    