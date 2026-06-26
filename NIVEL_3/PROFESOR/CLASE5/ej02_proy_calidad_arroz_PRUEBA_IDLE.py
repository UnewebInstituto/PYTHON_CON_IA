# Modificación para entrenamiento del modelo.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Carga y Limpieza (Mantenemos tu lógica original)
df = pd.read_csv('Rice_MSC_Dataset.csv')
def limpiar_lote(df):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())
    return df.drop_duplicates()

df = limpiar_lote(df)

# Al terminar de crear/transformar columnas, re-creamos el df para compactar la memoria
df = df.copy()
# 2. Ingeniería de Variable Objetivo (Target Binario)
# Definimos Basmati como 1 (Premium/Aceptable) y el resto como 0
df['Calidad_Aceptable'] = np.where(df['CLASS'] == 'Basmati', 1, 0)
df
        AREA  PERIMETER  ...      CLASS  Calidad_Aceptable
0       7805    437.915  ...    Basmati                  1
1       7503    340.757  ...    Arborio                  0
2       5124    314.617  ...    Jasmine                  0
3       7990    437.085  ...    Basmati                  1
4       7433    342.893  ...    Arborio                  0
...      ...        ...  ...        ...                ...
74995   5551    285.911  ...    Arborio                  0
74996   7696    322.703  ...  Karacadag                  0
74997   7579    339.295  ...    Arborio                  0
74998  15174    489.502  ...     Ipsala                  0
74999  12931    452.635  ...     Ipsala                  0

[74703 rows x 108 columns]
X = df.drop(columns=['CLASS', 'Calidad_Aceptable'])
X
        AREA  PERIMETER  MAJOR_AXIS  ...  ALLdaub4XX  ALLdaub4YY  ALLdaub4ZZ
0       7805    437.915    209.8215  ...      0.3673      0.3793      0.4733
1       7503    340.757    138.3361  ...      0.3014      0.3144      0.3641
2       5124    314.617    141.9803  ...      0.3233      0.3445      0.4448
3       7990    437.085    201.4386  ...      0.3880      0.4020      0.4904
4       7433    342.893    140.3350  ...      0.3184      0.3303      0.3928
...      ...        ...         ...  ...         ...         ...         ...
74995   5551    285.911    114.1695  ...      0.2895      0.2997      0.3455
74996   7696    322.703    121.3900  ...      0.3335      0.3426      0.4257
74997   7579    339.295    136.3125  ...      0.3028      0.3164      0.3761
74998  15174    489.502    200.9486  ...      0.3970      0.4215      0.4469
74999  12931    452.635    185.5138  ...      0.4162      0.4414      0.4626

[74703 rows x 106 columns]
y = df['Calidad_Aceptable']
y
0        1
1        0
2        0
3        1
4        0
        ..
74995    0
74996    0
74997    0
74998    0
74999    0
Name: Calidad_Aceptable, Length: 74703, dtype: int64
# 3. Entrenamiento y Validación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
RandomForestClassifier(random_state=42)
# 4. Validación Cruzada Estratificada (Evaluación Robusta)
# Esto asegura que cada lote sea evaluado equitativamente
skf = StratifiedKFold(n_splits=5)
y_pred_cv = cross_val_predict(modelo, X, y, cv=skf)
# 5. Métricas de Evaluación
print("--- Reporte de Clasificación (Validación Cruzada) ---")
--- Reporte de Clasificación (Validación Cruzada) ---
print(classification_report(y, y_pred_cv))
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     59703
           1       1.00      1.00      1.00     15000

    accuracy                           1.00     74703
   macro avg       1.00      1.00      1.00     74703
weighted avg       1.00      1.00      1.00     74703

# Visualización de la Matriz de Confusión
cm = confusion_matrix(y, y_pred_cv)
plt.figure(figsize=(6, 5))
<Figure size 600x500 with 0 Axes>
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', 
            xticklabels=['Otros', 'Basmati'], 
            yticklabels=['Otros', 'Basmati'])
<Axes: >

plt.xlabel('Predicho')
Text(0.5, 25.722222222222214, 'Predicho')
plt.ylabel('Real')
Text(45.722222222222214, 0.5, 'Real')
plt.title('Matriz de Confusión: Clasificación Premium (Basmati)')
Text(0.5, 1.0, 'Matriz de Confusión: Clasificación Premium (Basmati)')
plt.show()
