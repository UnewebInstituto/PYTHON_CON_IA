# Asistente RAG local (Ollama + LangChain + ChromaDB + Streamlit)

Chatbot que responde preguntas basándose en tus propios documentos
(PDF, DOCX, TXT), ejecutando el LLM completamente en local con Ollama.

## Requisitos previos

1. **Ollama instalado y corriendo** en tu máquina.
   Descarga: https://ollama.com

2. **Modelo descargado** (ajustado para equipos con 8 GB RAM y sin GPU dedicada):
   ```bash
   ollama pull phi3:mini
   ```
   Verifica que Ollama esté sirviendo en `http://localhost:11434` (por defecto).

   > 💡 Si tu equipo tiene más RAM (16 GB+) o GPU dedicada, puedes usar
   > un modelo más grande como `ollama pull llama3` y cambiar
   > `OLLAMA_MODEL = "llama3"` en `app.py` para mejor calidad de respuesta.

3. **Python 3.10+**

## Instalación

```bash
cd rag_chatbot
python -m venv .venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

```bash
streamlit run app.py
```

Se abrirá en tu navegador (normalmente `http://localhost:8501`).

## Uso

1. En la barra lateral, sube uno o varios documentos (PDF, DOCX o TXT).
2. Pulsa **"Procesar documentos"**. Esto:
   - Extrae el texto de cada archivo
   - Lo divide en fragmentos (chunks)
   - Genera embeddings multilingües (HuggingFace)
   - Los indexa en ChromaDB (persistidos en la carpeta `chroma_db/`)
3. Escribe tus preguntas en el chat. El asistente responderá basándose
   únicamente en el contenido de los documentos subidos.

## Personalización rápida

Todos los parámetros clave están al inicio de `app.py`:

| Variable           | Qué controla                                      |
|--------------------|----------------------------------------------------|
| `OLLAMA_MODEL`     | Qué modelo de Ollama usar (llama3, mistral, etc.)  |
| `EMBEDDING_MODEL`  | Modelo de embeddings de HuggingFace                |
| `CHUNK_SIZE`       | Tamaño de cada fragmento de texto                  |
| `CHUNK_OVERLAP`    | Solapamiento entre fragmentos consecutivos         |
| `TOP_K`            | Nº de fragmentos recuperados por cada pregunta     |

## Notas sobre escalabilidad

- Este proyecto está pensado para uso local/prototipo. Para producción,
  considera:
  - Migrar la lógica RAG a un endpoint **FastAPI** independiente de la UI
  - Sustituir Ollama por **vLLM** o **TGI** si necesitas mayor throughput
  - Usar un vector store gestionado (Qdrant, Pinecone, Weaviate) si el
    volumen de documentos crece mucho
  - Añadir logging de preguntas/respuestas para monitoreo y mejora continua

## Notas sobre la primera ejecución

- La **primera vez** que proceses documentos, verás la app "lenta" y en la
  terminal aparecerá una barra de progreso descargando `model.safetensors`
  (~470 MB). Es la descarga única del modelo de embeddings desde Hugging
  Face — depende de tu velocidad de internet, no de tu RAM ni del LLM.
  Una vez descargado, queda cacheado en `~/.cache/huggingface` (o el
  equivalente en Windows: `C:\Users\<usuario>\.cache\huggingface`) y las
  siguientes ejecuciones cargan el modelo casi instantáneamente.
- Es normal ver en consola tracebacks de `ModuleNotFoundError: No module
  named 'torchvision'`. Son inofensivos: Streamlit examina módulos de
  `transformers` que no usa tu app. El archivo `.streamlit/config.toml`
  incluido desactiva ese watcher para limpiar la consola. Si prefieres
  mantener la recarga automática al editar `app.py`, elimina o comenta
  la línea `fileWatcherType = "none"` de ese archivo (verás de nuevo el
  ruido en consola, pero sin afectar el funcionamiento).

## Recomendaciones para equipos con recursos limitados (8 GB RAM, sin GPU)

Si notas respuestas lentas o el equipo se congela al usar el chatbot:

- Cierra aplicaciones pesadas (navegador con muchas pestañas, editores, etc.)
  mientras uses el chatbot — con 8 GB totales, cada GB libre cuenta.
- Si `phi3:mini` sigue siendo lento, prueba modelos aún más ligeros:
  ```bash
  ollama pull gemma2:2b     # el más liviano
  ollama pull llama3.2:3b   # alternativa similar en tamaño
  ```
  y cambia `OLLAMA_MODEL` en `app.py` de acuerdo al que elijas.
- Procesa pocos documentos a la vez al inicio para validar que todo
  funciona antes de indexar colecciones grandes.
- El primer uso de un modelo de embeddings es más lento porque Hugging
  Face lo descarga y lo cachea localmente; las siguientes ejecuciones
  serán más rápidas.

## Solución de problemas comunes

- **Error de conexión con Ollama**: asegúrate de que el servicio esté
  corriendo (`ollama serve` o la app de Ollama abierta).
- **Modelo no encontrado**: ejecuta `ollama pull llama3` (o el modelo que
  hayas configurado en `OLLAMA_MODEL`).
- **Documentos en otros idiomas**: el modelo de embeddings usado
  (`paraphrase-multilingual-mpnet-base-v2`) soporta múltiples idiomas,
  incluido español.
