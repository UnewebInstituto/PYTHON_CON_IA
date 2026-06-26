import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# 1. Cargar datos
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")

# 2. Calcular el Margen de Ganancia Porcentual
# Margen = (Profit / Sales) * 100
# Si Sales es 0, evitamos división por cero usando fillna(0)
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0)

# 3. Ajustar el valor para que esté estrictamente en el rango 0-100
# Usamos MinMaxScaler para forzar cualquier valor a estar entre 0 y 100
scaler = MinMaxScaler(feature_range=(0, 100))
df['Profit_Scaled'] = scaler.fit_transform(df[['Profit_Margin']])

# 4. Ahora definimos el Target (Ejemplo: ¿Es altamente rentable? > 80 en la escala 0-100)
df['Target_Alto_Valor'] = (df['Profit_Scaled'] > 80).astype(int)

# 5. Preparamos X (Features)
# Convertimos categóricas a numéricas para que el modelo no falle
df_model = pd.get_dummies(df, columns=['Category', 'Payment Mode'], drop_first=True)
features = ['Sales', 'Quantity', 'Discount', 'Profit_Scaled'] + [c for c in df_model.columns if 'Category_' in c or 'Payment Mode_' in c]

X = df_model[features]
y = df['Target_Alto_Valor']

# 6. Entrenamiento con DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

print("Modelo entrenado con Profit escalado entre 0 y 100.")

predicciones = modelo.predict(X_test)

print(f"Precisión del modelo: {accuracy_score(y_test, predicciones)}")
