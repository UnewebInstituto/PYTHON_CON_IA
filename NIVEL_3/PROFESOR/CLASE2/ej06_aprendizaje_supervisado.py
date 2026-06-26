import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler

# 1. Cargar datos
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")

# 2. Calcular el Margen de Utilidad (Profit / Sales * 100)
# Esto convierte el valor absoluto a un porcentaje crudo
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0) # Manejo de posibles errores de división

# 3. Normalizar el margen a un rango estrictamente entre 0 y 100
# Esto asegura que cualquier valor extremo sea ajustado a tu escala objetivo
scaler = MinMaxScaler(feature_range=(0, 100))
df['Profit_Scaled'] = scaler.fit_transform(df[['Profit_Margin']])

# 4. Definir features (X) y el nuevo objetivo escalado (y)
X = df[['Sales', 'Quantity', 'Discount']]
y = df['Profit_Scaled'] # Ahora y está entre 0 y 100

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entrenar la regresión
reg = LinearRegression()
reg.fit(X_train, y_train)

# Resultado
predicciones = reg.predict(X_test)
mse = mean_squared_error(y_test, predicciones)
print(f"Error cuadrático medio en escala 0-100: {mse}")
print(f"Ejemplo de predicción (valor entre 0 y 100): {predicciones[0]:.2f}%")