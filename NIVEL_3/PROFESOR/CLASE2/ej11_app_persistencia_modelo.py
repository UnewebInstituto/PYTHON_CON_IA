import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Cargar y preprocesar
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")

# Ajustamos para que el beneficio sea mayor al 50%

df['is_profitable'] = (df['Profit'] > 0).astype(int)
df_encoded = pd.get_dummies(df, columns=['Category', 'Payment Mode', 'Region'], drop_first=True)

# Seleccionar features (deben coincidir con el orden que usaremos en la app)
features = [col for col in df_encoded.columns if col not in ['Order ID', 'Order Date', 'Customer Name', 'City', 'Product Name', 'Sub-Category', 'Profit', 'is_profitable']]
X = df_encoded[features]
y = df_encoded['is_profitable']

# Entrenar
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Guardar el modelo y la lista de columnas para asegurar consistencia
joblib.dump(rf_model, 'modelo_rentabilidad_1.pkl')
joblib.dump(features, 'columnas_modelo_1.pkl')
print("Modelo guardado exitosamente.")
