#Ej04
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
# Excluimos columnas no numéricas que no aportan valor predictivo
# directo o son identificadores
cols_to_drop = [
    'Order ID', 'Order Date', 'Customer Name', 'City', 
    'Product Name', 'Sub-Category', 'Profit', 'is_profitable'
]
# Aseguramos que solo trabajamos con columnas numéricas resultantes del encoding
X = df_encoded.drop(columns=[col for col in cols_to_drop if col in df_encoded.columns])

y = df_encoded['is_profitable']
X
      Quantity  Unit Price  Discount  ...  Region_North  Region_South  Region_West
0            2       36294         5  ...         False          True        False
1            1       42165        20  ...          True         False        False
2            4       64876        20  ...         False         False        False
3            5       37320        15  ...         False         False        False
4            1       50037        10  ...         False         False         True
...        ...         ...       ...  ...           ...           ...          ...
4995         3       60671         0  ...         False         False        False
4996         5       70048         0  ...          True         False        False
4997         1       42162        15  ...         False          True        False
4998         4       13568        10  ...         False         False        False
4999         1       76762        10  ...         False         False         True

[5000 rows x 20 columns]
y
0       1
1       1
2       1
3       1
4       1
       ..
4995    1
4996    1
4997    1
4998    1
4999    1
Name: is_profitable, Length: 5000, dtype: int64
# 5. División en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Dimensiones de X_train: {X_train.shape}")
Dimensiones de X_train: (4000, 20)
print(f"Las primeras filas de X procesadas:\n{X_train.head()}")
Las primeras filas de X procesadas:
      Quantity  Unit Price  Discount  ...  Region_North  Region_South  Region_West
4227         2       78935        20  ...         False         False         True
4676         5       73407        20  ...         False         False        False
800          3       75371         5  ...         False         False         True
3671         3        5655        20  ...          True         False        False
4193         2       10710         0  ...         False         False         True

[5 rows x 20 columns]
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
# 1. Instanciar y entrenar el modelo Random Forest
# Usamos n_estimators=100 para crear 100 árboles de decisión en el "bosque"
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
RandomForestClassifier(random_state=42)
KeyboardInterrupt
# 2. Realizar predicciones
y_pred = rf_model.predict(X_test)
# 3. Generar la Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)

Warning (from warnings module):
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\metrics\_classification.py", line 614
    warnings.warn(
UserWarning: A single label was found in 'y_true' and 'y_pred'. For the confusion matrix to have the correct shape, use the 'labels' parameter to pass all known labels.

= RESTART: C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\NIVEL_3\PROFESOR\CLASE1\ej04.py
Dimensiones de X_train: (4000, 20)
Las primeras filas de X procesadas:
      Quantity  Unit Price  Discount  ...  Region_North  Region_South  Region_West
4227         2       78935        20  ...         False         False         True
4676         5       73407        20  ...         False         False        False
800          3       75371         5  ...         False         False         True
3671         3        5655        20  ...          True         False        False
4193         2       10710         0  ...         False         False         True

[5 rows x 20 columns]

Warning (from warnings module):
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\metrics\_classification.py", line 614
    warnings.warn(
UserWarning: A single label was found in 'y_true' and 'y_pred'. For the confusion matrix to have the correct shape, use the 'labels' parameter to pass all known labels.
Reporte de Clasificación:
              precision    recall  f1-score   support

           1       1.00      1.00      1.00      1000

    accuracy                           1.00      1000
   macro avg       1.00      1.00      1.00      1000
weighted avg       1.00      1.00      1.00      1000

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
# 5. Mostrar métricas detalladas (Precisión, Recall, F1-Score)
print("Repo
      
SyntaxError: unterminated string literal (detected at line 2)
print("Reporte de Clasificación:")
      
Reporte de Clasificación:
print(classification_report(y_test, y_pred))
      
              precision    recall  f1-score   support

           1       1.00      1.00      1.00      1000

    accuracy                           1.00      1000
   macro avg       1.00      1.00      1.00      1000
weighted avg       1.00      1.00      1.00      1000

