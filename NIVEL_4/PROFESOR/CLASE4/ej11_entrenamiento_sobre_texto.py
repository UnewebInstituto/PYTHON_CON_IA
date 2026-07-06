from transformers import pipeline

# Uso de un modelo open source eficiente para generación de texto
generator = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")
prompt = "Analiza la calidad del arroz basándote en la textura del grano"
response = generator(prompt, max_length=50)
print(response)