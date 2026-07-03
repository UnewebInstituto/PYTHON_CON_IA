from transformers import pipeline

# 1. Cargamos un pipeline de análisis de sentimiento
# Este modelo es multilingüe y funciona excelente con español
classifier = pipeline("sentiment-analysis", model="pysentimiento/robertuito-sentiment-analysis")

# 2. Definimos nuestras reseñas sobre el arroz
comentarios = [
    "El grano de arroz está excelente, muy blanco y con gran textura.",
    "Estoy muy decepcionado, el producto llegó con muchas impurezas y restos de cascarilla.",
    "El arroz es aceptable, el sabor es estándar.",
    "Excelente uniformidad y color cristalino.",
    "El grano presenta alto porcentaje de yesado.",
    "Mucho contenido de granos rotos en el empaque.",
    "El arroz tiene una calidad excelente muy blanco.",
    "Sabor neutro y buena cocción.",
    "Demasiadas impurezas y restos de cascarilla.",
    "Muy buena apariencia y color claro.",
    "Muy mala apariencia y color obscuro.",
    "Los granos presentan impurezas y mal olor.",
    "Muy buen sabor y consistencia del grano.",
]

# 3. Clasificación
for c in comentarios:
    resultado = classifier(c)
    print(f"Texto: {c}")
    print(f"Sentimiento: {resultado[0]['label']}, Confianza: {resultado[0]['score']:.2f}\n")
