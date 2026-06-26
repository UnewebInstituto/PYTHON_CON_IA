import numpy as np
import matplotlib.pyplot as plt

class ProcesadorEstadistico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = None

    def cargar_datos(self, datos):
        # Almacenamos como arreglo NumPy para eficiencia
        self.datos = np.array(datos)
        print(f"[{self.nombre}] Datos cargados: {len(self.datos)} elementos.")

    def obtener_tendencia_central(self):
        # Álgebra lineal y estadística básica vectorizada
        return {
            "media": np.mean(self.datos),
            "mediana": np.median(self.datos),
            "desviacion": np.std(self.datos)
        }

    def graficar_distribucion(self):
        plt.hist(self.datos, bins=10, color='skyblue', edgecolor='black')
        plt.title(f"Distribución de Frecuencia - {self.nombre}")
        plt.xlabel("Valor")
        plt.ylabel("Frecuencia")
        plt.show()
