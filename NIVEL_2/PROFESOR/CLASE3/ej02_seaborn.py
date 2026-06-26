# 2do. Ejemplo matplotlib y seaborn
import pandas as pd
# Creamos un dataset
df = pd.DataFrame({'Edad': [20, 30, 40], 'Presion': [120, 130, 140], 'Glucosa': [80, 90, 110]})
df
   Edad  Presion  Glucosa
0    20      120       80
1    30      130       90
2    40      140      110
# Matriz de correlación
correlacion = df.corr()
correlacion
             Edad   Presion   Glucosa
Edad     1.000000  1.000000  0.981981
Presion  1.000000  1.000000  0.981981
Glucosa  0.981981  0.981981  1.000000
# Heatmap (Mapa de calor)
sns.heatmap(correlacion, annot=True, cmap='coolwarm')
<Axes: >
plt.title("Mapa de Calor de Correlaciones")
Text(0.5, 1.0, 'Mapa de Calor de Correlaciones')
plt.show()
