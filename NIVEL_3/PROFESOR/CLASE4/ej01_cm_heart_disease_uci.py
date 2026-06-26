import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import classification_report, confusion_matrix

# 1. Carga
df = pd.read_csv('heart_disease_uci.csv')

# 2. Limpieza de datos
df = df.drop('id', axis=1) # Eliminamos id

# Imputación de valores faltantes
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# 3. Transformación de categóricas a numéricas
# Esto convierte 'sex', 'cp', etc., en columnas binarias (0/1)
df_encoded = pd.get_dummies(df, drop_first=True)

# 4. Definición de variables
# 'num' es nuestra variable objetivo
X = df_encoded.drop('num', axis=1)
y = df_encoded['num']

# 5. Validación Cruzada Estratificada y Entrenamiento
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Predicciones mediante validación cruzada
y_pred = cross_val_predict(modelo, X, y, cv=skf)

# 6. Reporte de Evaluación
print("--- Reporte de Clasificación Clínica ---")
print(classification_report(y, y_pred))

# 7. Matriz de Confusión
cm = confusion_matrix(y, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title("Matriz de Confusión - Diagnóstico Cardíaco")
plt.xlabel("Predicción")
plt.ylabel("Realidad")
plt.show()
