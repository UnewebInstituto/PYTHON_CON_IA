# Cargar depedencias y la clase del proyecto 1
import proyecto1

import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios con distribución normal
datos_aleatorios = np.random.normal(loc=50, scale=15, size=100)

# Instancia de la clase ProcesadorEstadistico
procesador = proyecto1.ProcesadorEstadistico("Analizador-Nivel1")

# Cargar datos al procesador
procesador.cargar_datos(datos_aleatorios)

# Obtener medidas de tendencia central
metricas = procesador.obtener_tendencia_central()
print(f"Métricas obtenidas: {metricas}")

# Producir gráfico de distribución
procesador.graficar_distribucion()



