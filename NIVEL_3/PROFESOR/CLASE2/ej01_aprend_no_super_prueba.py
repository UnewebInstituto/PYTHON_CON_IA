# APRENDIZAJE NO SUPERVISADO
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
# Cargar el dataset
ruta = "C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv"
df = pd.read_csv(ruta)

# Calcular el Margen de Ganancia Porcentual
# Margen = (Profit / Sales) * 100
# Si Sales es 0, evitamos división por cero usando fillna(0)
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0)
# Preparar los datos
df_cl = df[['Sales', 'Profit_Margin']].copy()
df_cl
         Sales  Profit_Margin
0      68958.6      15.262911
1      33732.0      18.675620
2     207603.2       9.561640
3     158610.0      22.893273
4      45033.3      20.096329
...        ...            ...
4995  182013.0       6.512255
4996  350240.0       8.918807
4997   35837.7      21.841524
4998   48844.8      13.520088
4999   69085.8       8.374876

[5000 rows x 2 columns]
scaler = StandardScaler() # Importante: K-Means es sensible a la escala
df_scaled = scaler.fit_transform(df_cl)
# 2. Encontrar el número óptimo de K (Método del Codo)
inercias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df_scaled)
    inercias.append(km.inertia_)

    
KMeans(n_clusters=1, n_init=10, random_state=42)
KMeans(n_clusters=2, n_init=10, random_state=42)
KMeans(n_clusters=3, n_init=10, random_state=42)
KMeans(n_clusters=4, n_init=10, random_state=42)
KMeans(n_clusters=5, n_init=10, random_state=42)
KMeans(n_clusters=6, n_init=10, random_state=42)
KMeans(n_clusters=7, n_init=10, random_state=42)
KMeans(n_init=10, random_state=42)
KMeans(n_clusters=9, n_init=10, random_state=42)
KMeans(n_clusters=10, n_init=10, random_state=42)
plt.plot(range(1, 11), inercias, marker='o')
[<matplotlib.lines.Line2D object at 0x000001A47B739340>]
plt.title('Método del Codo para rendimiento de las ventas')
Text(0.5, 1.0, 'Método del Codo para rendimiento de las ventas')
plt.xlabel('Número de Clústeres (K)')
Text(0.5, 0, 'Número de Clústeres (K)')
plt.ylabel('Inercia')
Text(0, 0.5, 'Inercia')
plt.show()
# 3. Aplicar K-Means (Supongamos que elegimos K=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)
# 4. Visualizar los segmentos
plt.scatter(df['Sales'], df['Profit_Margin'], c=df['Cluster'], cmap='viridis')
<matplotlib.collections.PathCollection object at 0x000001A47B772A80>
plt.title('Segmentación de Clientes - por Ventas')
Text(0.5, 1.0, 'Segmentación de Clientes - por Ventas')
plt.xlabel('Ventas')
Text(0.5, 0, 'Ventas')
plt.ylabel('Margen de Utilidad')
Text(0, 0.5, 'Margen de Utilidad')
plt.show()
