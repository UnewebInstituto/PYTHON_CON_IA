import seaborn as sns
import matplotlib.pyplot as plt
# Datos de ejemplo
edades = [22, 25, 25, 30, 35, 40, 45, 50, 50, 50, 60]
edades
[22, 25, 25, 30, 35, 40, 45, 50, 50, 50, 60]
# Gráfico con Seaborn
sns.histplot(edades, kde=True, color='skyblue')
<Axes: ylabel='Count'>
plt.title("Distribución de Edades")
Text(0.5, 1.0, 'Distribución de Edades')
plt.xlabel("Edad")
Text(0.5, 0, 'Edad')
plt.ylabel("Frecuencia")
Text(0, 0.5, 'Frecuencia')
plt.show() # Simpre para mostrar el gráfico resultado.