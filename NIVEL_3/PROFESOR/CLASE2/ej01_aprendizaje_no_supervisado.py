import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Carga de datos, ingeniería de variables y preprocesamiento se mantienen igual.

# 1. Cargar el dataset
ruta = "C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv"
df = pd.read_csv(ruta)

# 2. Calcular el Margen de Ganancia Porcentual
# Margen = (Profit / Sales) * 100
# Si Sales es 0, evitamos división por cero usando fillna(0)
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0)

# 1. Preparar los datos
df_cl = df[['Sales', 'Profit_Margin']].copy()
scaler = StandardScaler() # Importante: K-Means es sensible a la escala
df_scaled = scaler.fit_transform(df_cl)

# 2. Encontrar el número óptimo de K (Método del Codo)
inercias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(df_scaled)
    inercias.append(km.inertia_)

plt.plot(range(1, 11), inercias, marker='o')
plt.title('Método del Codo para Determinar el Número Óptimo de Clústeres')
plt.xlabel('Número de Clústeres (K)')
plt.ylabel('Inercia')
plt.show()

# 3. Aplicar K-Means (Supongamos que elegimos K=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# 4. Visualizar los segmentos
plt.scatter(df['Sales'], df['Profit_Margin'], c=df['Cluster'], cmap='viridis')
plt.title('Segmentación de Clientes')
plt.xlabel('Ventas')
plt.ylabel('Margen de Utilidad')
plt.show()
