import joblib
import pandas as pd

# 1. Cargar el modelo desde el disco
modelo_cargado = joblib.load('modelo_calidad_arroz.pkl')

# 2. Simular nuevos datos (Ejemplo: una fila de un nuevo lote)
# Nota: debe tener exactamente las mismas columnas que X en tu entrenamiento
# Puedes usar un archivo .csv con nuevos datos
# nuevo_lote = pd.read_csv('datos_nuevo_lote.csv') # Ajusta según tu archivo

nuevo_lote = pd.read_csv('datos_nuevo_lote.csv') # Ajusta según tu archivo


# 3. Predicción
prediccion = modelo_cargado.predict(nuevo_lote)

if prediccion[0] == 1:
    print("Resultado del Laboratorio: Lote clasificado como BASMATI (Premium).")
else:
    print("Resultado del Laboratorio: Lote clasificado como OTROS.")
