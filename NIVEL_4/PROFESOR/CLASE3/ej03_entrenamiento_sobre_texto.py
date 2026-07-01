from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Dataset de ejemplo (en producción, esto vendría de un archivo .csv)
datos = [
    ("grano partido y con impurezas", 0),
    ("arroz de primera, muy blanco", 1),
    ("contiene muchos granos yesosos", 0),
    ("aspecto cristalino y granos enteros", 1)
]
textos, etiquetas = zip(*datos)

# 2. Pipeline: Vectorización (Convertir texto a números) + Clasificador (Naive Bayes)
# TfidfVectorizer: Da importancia a palabras técnicas específicas ("yesoso")
# eliminando las comunes ("el", "de").
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# 3. Entrenamiento
model.fit(textos, etiquetas)

# 4. Predicción
nuevo_comentario = ["el arroz tiene muchas impurezas"]
resultado = model.predict(nuevo_comentario)
print(f"Predicción (1=Alta, 0=Baja): {resultado[0]}")
