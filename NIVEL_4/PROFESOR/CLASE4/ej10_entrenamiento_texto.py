from google.colab import drive

from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# 1. Ruta donde guardaste tu mejor checkpoint

drive.mount('/content/drive')
ruta_modelo = "/content/drive/MyDrive/resultado_entrenamiento/checkpoint-3"

# 2. Cargar modelo y tokenizer
# Usamos el mismo modelo base que usaste para entrenar
model = AutoModelForSequenceClassification.from_pretrained(ruta_modelo)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

# 3. Reseña de prueba (escrita para "el proyecto")
resena_nueva = "El arroz llegó con mucha humedad y varios granos negros, inaceptable para la venta."

# 4. Tokenizar y predecir
inputs = tokenizer(resena_nueva, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)

# 5. Interpretar resultado
# Asumiendo que 0 es Negativo y 1 es Positivo
clases = {0: "Negativo", 1: "Positivo"}
sentimiento = clases[predictions.item()]

print(f"Reseña: {resena_nueva}")
print(f"La IA clasificó esta reseña como: {sentimiento}")