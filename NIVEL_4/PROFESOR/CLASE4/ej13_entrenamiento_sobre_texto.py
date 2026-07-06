# Requisito 1 (Ejecutar en una celda de Google Colab)

# !apt-get update && apt-get install -y zstd


# Requisito 2 (Ejecutar en una celda de Google Colab)

# !curl -fsSL https://ollama.com/install.sh | sh


# Sección de código para entrenar un modelo de clasificación de texto usando Ollama

import subprocess
import time

# Iniciar el servidor
process = subprocess.Popen(["ollama", "serve"])
time.sleep(5)  # Esperar a que el servidor inicialice


#
from transformers import pipeline

# Cargar un modelo directamente desde Hugging Face
generator = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")
prompt = "¿Cuál es el procedimiento de inspección de grano?"
response = generator(prompt, max_length=100)
print(response)

"""
Esta sección de código tiene como objetivo **iniciar el servidor de Ollama en segundo plano** para que pueda atender las consultas de tus modelos de IA desde Python. Aquí te detallo qué hace cada parte:

* **`import subprocess` y `import time**`: Importa las librerías necesarias. `subprocess` permite ejecutar comandos del sistema operativo desde Python, y `time` permite gestionar pausas temporales en el código.
* **`process = subprocess.Popen(["ollama", "serve"])`**: Esta es la instrucción clave. Lanza el comando `ollama serve` como un proceso independiente (en segundo plano). Esto es necesario porque el servidor de Ollama necesita estar "escuchando" constantemente para poder cargar los modelos y procesar las peticiones que le envíes después desde LangChain o tu propia aplicación.
* **`time.sleep(5)`**: Esta pausa es fundamental. Como el servidor de Ollama no arranca instantáneamente, el código espera 5 segundos antes de intentar cualquier otra operación (como cargar un modelo o enviar una pregunta). Sin esta pausa, es muy probable que tu script intentara conectar con el servidor antes de que este estuviera listo, lo que causaría el error de "Connection Refused" que viste anteriormente.

En resumen: **prepara el terreno** arrancando el motor de inteligencia artificial local para que tu código pueda comunicarse con él inmediatamente después.

"""

from transformers import pipeline

# Cargar un modelo directamente desde Hugging Face
generator = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")
prompt = "¿Cuál es el procedimiento de inspección de grano?"
response = generator(prompt, max_length=100)
print(response)



"""
Esta sección de código utiliza la librería `transformers` de Hugging Face para realizar una tarea de generación de texto de manera directa, sin necesidad de configurar un servidor externo como Ollama.

Aquí te detallo qué hace cada línea:

* **`from transformers import pipeline`**: Importa la función `pipeline`, que es la herramienta más sencilla y de alto nivel de Hugging Face. Un *pipeline* agrupa automáticamente el modelo, el tokenizador (que convierte texto a números) y los procesos de inferencia en un solo objeto fácil de usar.

* **`generator = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")`**: Esta línea inicializa el motor de IA.
* `"text-generation"` especifica que quieres que el modelo cree texto a partir de una entrada.
* `model="mistralai/Mistral-7B-v0.1"` descarga (o carga desde la caché) el modelo Mistral específico. Es un modelo potente de 7 mil millones de parámetros.

* **`prompt = "¿Cuál es el procedimiento de inspección de grano?"`**: Define la pregunta o contexto que servirá como punto de partida para que la IA genere su respuesta.
* **`response = generator(prompt, max_length=100)`**: Aquí ocurre la "magia". El modelo toma el *prompt* y genera una continuación de hasta 100 *tokens* (aproximadamente 75-80 palabras). El *pipeline* maneja internamente la conversión del texto a formato numérico, el procesamiento por la red neuronal y la decodificación de vuelta a texto legible.


* **`print(response)`**: Muestra en pantalla el resultado generado por el modelo.

### ¿Por qué esta opción es diferente a la de Ollama?

A diferencia del código anterior que usamos con `subprocess.Popen(["ollama", "serve"])`:

1. **Es autocontenido:** No requiere que corras un proceso de servidor por separado. Todo sucede dentro de tu script de Python.
2. **Es nativo de Hugging Face:** Utiliza directamente la infraestructura de descarga y ejecución de modelos de la librería `transformers`.
3. 
**Ideal para prototipos:** Es la forma más rápida de probar un modelo en Google Colab para verificar si su razonamiento es adecuado para tu proyecto antes de escalar a una arquitectura más compleja como RAG.

**Ten en cuenta:** Al ser una descarga directa desde Hugging Face, la primera vez que ejecutes este código, el entorno de Colab deberá descargar los archivos del modelo (que pesan varios GB), por lo que puede tardar unos minutos en iniciar.


"""

