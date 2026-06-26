import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Cargar el dataset
ruta = "C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv"
df = pd.read_csv(ruta)

# 2. Ingeniería de variables: Crear la variable objetivo (Target)
# Definimos 1 si el Profit es mayor a 0 (Rentable), y 0 en caso contrario
df['is_profitable'] = (df['Profit'] > 0).astype(int)

# 3. Preprocesamiento: Codificación de variables categóricas
# Usamos 'drop_first=True' para evitar la multicolinealidad
df_encoded = pd.get_dummies(df, columns=['Category', 'Payment Mode', 'Region'], drop_first=True)

# 4. Selección de Features (X) y Target (y)
# Excluimos columnas no numéricas que no aportan valor predictivo directo o son identificadores
cols_to_drop = [
    'Order ID', 'Order Date', 'Customer Name', 'City', 
    'Product Name', 'Sub-Category', 'Profit', 'is_profitable'
]

# Aseguramos que solo trabajamos con columnas numéricas resultantes del encoding
X = df_encoded.drop(columns=[col for col in cols_to_drop if col in df_encoded.columns])
y = df_encoded['is_profitable']

# 5. División en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Dimensiones de X_train: {X_train.shape}")
print(f"Las primeras filas de X procesadas:\n{X_train.head()}")
