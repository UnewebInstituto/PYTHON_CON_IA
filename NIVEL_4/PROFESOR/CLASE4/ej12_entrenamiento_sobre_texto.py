from transformers import pipeline

# Cargar un modelo directamente desde Hugging Face
generator = pipeline("text-generation", model="mistralai/Mistral-7B-v0.1")
prompt = "¿Cuál es el procedimiento de inspección de grano de arroz?"
response = generator(prompt, max_length=100)
print(response)