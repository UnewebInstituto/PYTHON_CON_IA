Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
df = pd.read_csv('./NIVEL_3/PROFESOR/CLASE4/heart_disease_uci.csv')
df
      id  age     sex  ...   ca               thal  num
0      1   63    Male  ...  0.0       fixed defect    0
1      2   67    Male  ...  3.0             normal    2
2      3   67    Male  ...  2.0  reversable defect    1
3      4   37    Male  ...  0.0             normal    0
4      5   41  Female  ...  0.0             normal    0
..   ...  ...     ...  ...  ...                ...  ...
915  916   54  Female  ...  NaN                NaN    1
916  917   62    Male  ...  NaN                NaN    0
917  918   55    Male  ...  NaN       fixed defect    2
918  919   58    Male  ...  NaN                NaN    0
919  920   62    Male  ...  NaN                NaN    1

[920 rows x 16 columns]
df.columns.to_list()
['id', 'age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
df.head()
   id  age     sex  ...   ca               thal  num
0   1   63    Male  ...  0.0       fixed defect    0
1   2   67    Male  ...  3.0             normal    2
2   3   67    Male  ...  2.0  reversable defect    1
3   4   37    Male  ...  0.0             normal    0
4   5   41  Female  ...  0.0             normal    0

[5 rows x 16 columns]
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 920 entries, 0 to 919
Data columns (total 16 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   id        920 non-null    int64  
 1   age       920 non-null    int64  
 2   sex       920 non-null    str    
 3   dataset   920 non-null    str    
 4   cp        920 non-null    str    
 5   trestbps  861 non-null    float64
 6   chol      890 non-null    float64
 7   fbs       830 non-null    object 
 8   restecg   918 non-null    str    
 9   thalch    865 non-null    float64
 10  exang     865 non-null    object 
 11  oldpeak   858 non-null    float64
 12  slope     611 non-null    str    
 13  ca        309 non-null    float64
 14  thal      434 non-null    str    
 15  num       920 non-null    int64  
dtypes: float64(5), int64(3), object(2), str(6)
memory usage: 156.4+ KB
### Desarrollo del modelo para dataset heart disease uci
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import classification_report, confusion_matrix
# 1. Carga
df = pd.read_csv('./NIVEL_3/PROFESOR/CLASE4/heart_disease_uci.csv')
# 2. Limpieza de datos
df = df.drop('id', axis=1) # Eliminamos id
df.columns.to_list()
['age', 'sex', 'dataset', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
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
X
     age  trestbps   chol  thalch  ...  slope_flat  slope_upsloping  thal_normal  thal_reversable defect
0     63     145.0  233.0   150.0  ...       False            False        False                   False
1     67     160.0  286.0   108.0  ...        True            False         True                   False
2     67     120.0  229.0   129.0  ...        True            False        False                    True
3     37     130.0  250.0   187.0  ...       False            False         True                   False
4     41     130.0  204.0   172.0  ...       False             True         True                   False
..   ...       ...    ...     ...  ...         ...              ...          ...                     ...
915   54     127.0  333.0   154.0  ...        True            False         True                   False
916   62     130.0  139.0   140.0  ...        True            False         True                   False
917   55     122.0  223.0   100.0  ...        True            False        False                   False
918   58     130.0  385.0   140.0  ...        True            False         True                   False
919   62     120.0  254.0    93.0  ...        True            False         True                   False

[920 rows x 21 columns]
y = df_encoded['num']
y
0      0
1      2
2      1
3      0
4      0
      ..
915    1
916    0
917    2
918    0
919    1
Name: num, Length: 920, dtype: int64
# 5. Validación Cruzada Estratificada y Entrenamiento
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
# Predicciones mediante validación cruzada
y_pred = cross_val_predict(modelo, X, y, cv=skf)
# 6. Reporte de Evaluación
print("--- Reporte de Clasificación Clínica ---")
--- Reporte de Clasificación Clínica ---
print(classification_report(y, y_pred))
              precision    recall  f1-score   support

           0       0.72      0.83      0.77       411
           1       0.48      0.51      0.49       265
           2       0.27      0.21      0.24       109
           3       0.25      0.17      0.20       107
           4       0.17      0.04      0.06        28

    accuracy                           0.56       920
   macro avg       0.38      0.35      0.35       920
weighted avg       0.53      0.56      0.54       920

# 7. Matriz de Confusión
cm = confusion_matrix(y, y_pred)
plt.figure(figsize=(7, 5))
<Figure size 700x500 with 0 Axes>
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
<Axes: >
plt.title("Matriz de Confusión - Diagnóstico Cardíaco")
Text(0.5, 1.0, 'Matriz de Confusión - Diagnóstico Cardíaco')
plt.xlabel("Predicción")
Text(0.5, 25.722222222222214, 'Predicción')
plt.ylabel("Realidad")
Text(58.222222222222214, 0.5, 'Realidad')
plt.show()
