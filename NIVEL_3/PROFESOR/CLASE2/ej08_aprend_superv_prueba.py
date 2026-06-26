import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler

# 1. Cargar y procesar métrica de rendimiento (0-100)

df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")

df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0)

scaler = MinMaxScaler(feature_range=(0, 100))
df['Profit_Scaled'] = scaler.fit_transform(df[['Profit_Margin']])

# 2. Definir target binario (1 si es Alta Rentabilidad, 0 si no)
df['High_Performance'] = (df['Profit_Scaled'] > 80).astype(int)

# 3. Preparar X e y
# Incluimos Sales, Quantity, Discount y el valor escalado
X = df[['Sales', 'Quantity', 'Discount', 'Profit_Scaled']]
y = df['High_Performance']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Árbol de Decisión (Fácil de interpretar para reglas de negocio)
tree = DecisionTreeClassifier(max_depth=4, class_weight='balanced')
tree.fit(X_train, y_train)

# 5. Random Forest (Mayor capacidad predictiva)
forest = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
forest.fit(X_train, y_train)

print(f"Precisión del Árbol de Decisión: {tree.score(X_test, y_test):.2f}")
print(f"Precisión del Random Forest: {forest.score(X_test, y_test):.2f}")