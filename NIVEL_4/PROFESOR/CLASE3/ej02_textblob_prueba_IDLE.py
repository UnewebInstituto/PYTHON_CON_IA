# PRUEBA ej02_textblob
from textblob import TextBlob
# 1. Función de limpieza básica
def limpiar_texto(texto):
    # Convertir a minúsculas y quitar caracteres no alfabéticos simples
    texto = texto.lower()
    return texto

# 2. Análisis de sentimiento
comentarios = [
    "El arroz tiene una calidad excelente, muy blanco y limpio.",
    "El producto es aceptable, pero llegó con algunas impurezas.",
    "Pésima experiencia, el arroz estaba lleno de granos rotos."
]
comentarios
['El arroz tiene una calidad excelente, muy blanco y limpio.', 'El producto es aceptable, pero llegó con algunas impurezas.', 'Pésima experiencia, el arroz estaba lleno de granos rotos.']
for c in comentarios:
    texto_limpio = limpiar_texto(c)
    analisis = TextBlob(texto_limpio)
    
    # 'polarity' va de -1 (negativo) a 1 (positivo)
    score = analisis.sentiment.polarity
    sentimiento = "Positivo" if score > 0 else "Negativo" if score < 0 else "Neutro"
    
    print(f"Texto: {c}\nSentimiento: {sentimiento} (Score: {score:.2f})\n")

    
Texto: El arroz tiene una calidad excelente, muy blanco y limpio.
Sentimiento: Neutro (Score: 0.00)

Texto: El producto es aceptable, pero llegó con algunas impurezas.
Sentimiento: Neutro (Score: 0.00)

Texto: Pésima experiencia, el arroz estaba lleno de granos rotos.
Sentimiento: Neutro (Score: 0.00)

