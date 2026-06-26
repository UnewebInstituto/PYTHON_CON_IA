import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
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
# 5. División en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# CORRECCIÓN 1: Usamos 'class_weight="balanced"'
# Esto obliga al Random Forest a dar más importancia a la clase minoritari
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
rf_model.fit(X_train, y_train)
RandomForestClassifier(class_weight='balanced', random_state=42)
# 2. Realizar predicciones
y_pred = rf_model.predict(X_test)
# CORRECCIÓN 2: Pasamos el parámetro 'labels=[0, 1]'
# Esto garantiza que la matriz siempre tenga el formato 2x2, incluso si falta una clase
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
# 4. Visualización de la Matriz de Confusión
plt.figure(figsize=(8, 6))
<Figure size 800x600 with 0 Axes>
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Rentable', 'Rentable'], 
            yticklabels=['No Rentable', 'Rentable'])
<Axes: >
plt.title('Matriz de Confusión - Clasificación de Rentabilidad')
Text(0.5, 1.0, 'Matriz de Confusión - Clasificación de Rentabilidad')
plt.xlabel('Predicción del Modelo')
Text(0.5, 36.72222222222221, 'Predicción del Modelo')
plt.ylabel('Valor Real')
Text(70.72222222222221, 0.5, 'Valor Real')
plt.show()
# 5. Mostrar métricas detalladas
# 5. Mostrar métricas detalladas
print("Reporte de Clasificación:")
Reporte de Clasificación:
print(classification_report(y_test, y_pred, labels=[0, 1], zero_division=0))
              precision    recall  f1-score   support

           0       0.00      0.00      0.00         0
           1       1.00      1.00      1.00      1000

    accuracy                           1.00      1000
   macro avg       0.50      0.50      0.50      1000
weighted avg       1.00      1.00      1.00      1000

