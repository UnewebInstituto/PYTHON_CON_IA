# PRUEBA DEL MODELO DE CLASIFICACIÓN
import pandas as pd
from sklearn.metrics import classification_report
# 1. Cargar datos
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
# 2. Calcular Margen y Escalar a 0-100
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0)
scaler = MinMaxScaler(feature_range=(0, 100))
df['Profit_Scaled'] = scaler.fit_transform(df[['Profit_Margin']])
# 3. Crear variable objetivo binaria:
# 1 si el margen escalado es > 80 (Alto Rendimiento), 0 si no
df['High_Performance'] = (df['Profit_Scaled'] > 80).astype(int)
df['High_Performance']
0       0
1       0
2       0
3       1
4       0
       ..
4995    0
4996    0
4997    1
4998    0
4999    0
Name: High_Performance, Length: 5000, dtype: int64

# 4. Seleccionar variables predictoras (Features)
X = df[['Sales', 'Quantity', 'Discount']]
y = df['High_Performance']
# 5. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 6. Entrenar Regresión Logística
# Nota: usamos class_weight='balanced' por si hay pocas ventas "Altamente Rentables"
clf_log = LogisticRegression(class_weight='balanced')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    clf_log = LogisticRegression(class_weight='balanced')
NameError: name 'LogisticRegression' is not defined. Did you mean: 'LinearRegression'?
from sklearn.linear_model import LogisticRegression
clf_log = LogisticRegression(class_weight='balanced')
clf_log.fit(X_train, y_train)
LogisticRegression(class_weight='balanced')
# 7. Evaluar
y_pred = clf_log.predict(X_test)
print("Reporte de clasificación para 'High_Performance':")
Reporte de clasificación para 'High_Performance':
print(classification_report(y_test, y_pred))
              precision    recall  f1-score   support

           0       0.81      0.50      0.62       809
           1       0.19      0.49      0.27       191

    accuracy                           0.50      1000
   macro avg       0.50      0.50      0.45      1000
weighted avg       0.69      0.50      0.55      1000