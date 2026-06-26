Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Ejemplo Telco Customer Churn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Carga y Limpieza Robusta
df = pd.read_csv('./NIVEL_3/PROFESOR/CLASE4/WA_Fn-UseC_-Telco-Customer-Churn.csv')
df
      customerID  gender  SeniorCitizen  ... MonthlyCharges TotalCharges  Churn
0     7590-VHVEG  Female              0  ...          29.85        29.85     No
1     5575-GNVDE    Male              0  ...          56.95       1889.5     No
2     3668-QPYBK    Male              0  ...          53.85       108.15    Yes
3     7795-CFOCW    Male              0  ...          42.30      1840.75     No
4     9237-HQITU  Female              0  ...          70.70       151.65    Yes
...          ...     ...            ...  ...            ...          ...    ...
7038  6840-RESVB    Male              0  ...          84.80       1990.5     No
7039  2234-XADUH  Female              0  ...         103.20       7362.9     No
7040  4801-JZAZL  Female              0  ...          29.60       346.45     No
7041  8361-LTMKD    Male              1  ...          74.40        306.6    Yes
7042  3186-AJIEK    Male              0  ...         105.65       6844.5     No

[7043 rows x 21 columns]
# Conversión segura para evitar errores de asignación
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
df
      customerID  gender  SeniorCitizen  ... MonthlyCharges TotalCharges  Churn
0     7590-VHVEG  Female              0  ...          29.85        29.85     No
1     5575-GNVDE    Male              0  ...          56.95      1889.50     No
2     3668-QPYBK    Male              0  ...          53.85       108.15    Yes
3     7795-CFOCW    Male              0  ...          42.30      1840.75     No
4     9237-HQITU  Female              0  ...          70.70       151.65    Yes
...          ...     ...            ...  ...            ...          ...    ...
7038  6840-RESVB    Male              0  ...          84.80      1990.50     No
7039  2234-XADUH  Female              0  ...         103.20      7362.90     No
7040  4801-JZAZL  Female              0  ...          29.60       346.45     No
7041  8361-LTMKD    Male              1  ...          74.40       306.60    Yes
7042  3186-AJIEK    Male              0  ...         105.65      6844.50     No

[7043 rows x 21 columns]
df = df.drop('customerID', axis=1)
df
      gender  SeniorCitizen Partner  ... MonthlyCharges  TotalCharges Churn
0     Female              0     Yes  ...          29.85         29.85    No
1       Male              0      No  ...          56.95       1889.50    No
2       Male              0      No  ...          53.85        108.15   Yes
3       Male              0      No  ...          42.30       1840.75    No
4     Female              0      No  ...          70.70        151.65   Yes
...      ...            ...     ...  ...            ...           ...   ...
7038    Male              0     Yes  ...          84.80       1990.50    No
7039  Female              0     Yes  ...         103.20       7362.90    No
7040  Female              0     Yes  ...          29.60        346.45    No
7041    Male              1     Yes  ...          74.40        306.60   Yes
7042    Male              0      No  ...         105.65       6844.50    No

[7043 rows x 20 columns]
# 2. Codificación (Preparación para el Modelo)
# Convertimos todas las variables categóricas de una forma más limpia
# Esto soluciona el ValueError al convertir automáticamente todo a numérico
df = pd.get_dummies(df, drop_first=True)
df
      SeniorCitizen  tenure  ...  PaymentMethod_Mailed check  Churn_Yes
0                 0       1  ...                       False      False
1                 0      34  ...                        True      False
2                 0       2  ...                        True       True
3                 0      45  ...                       False      False
4                 0       2  ...                       False       True
...             ...     ...  ...                         ...        ...
7038              0      24  ...                        True      False
7039              0      72  ...                       False      False
7040              0      11  ...                       False      False
7041              1       4  ...                        True       True
7042              0      66  ...                       False      False

[7043 rows x 31 columns]
df.columns.to_list()
['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'gender_Male', 'Partner_Yes', 'Dependents_Yes', 'PhoneService_Yes', 'MultipleLines_No phone service', 'MultipleLines_Yes', 'InternetService_Fiber optic', 'InternetService_No', 'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No internet service', 'OnlineBackup_Yes', 'DeviceProtection_No internet service', 'DeviceProtection_Yes', 'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No internet service', 'StreamingTV_Yes', 'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_One year', 'Contract_Two year', 'PaperlessBilling_Yes', 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'Churn_Yes']
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 7043 entries, 0 to 7042
Data columns (total 31 columns):
 #   Column                                 Non-Null Count  Dtype  
---  ------                                 --------------  -----  
 0   SeniorCitizen                          7043 non-null   int64  
 1   tenure                                 7043 non-null   int64  
 2   MonthlyCharges                         7043 non-null   float64
 3   TotalCharges                           7043 non-null   float64
 4   gender_Male                            7043 non-null   bool   
 5   Partner_Yes                            7043 non-null   bool   
 6   Dependents_Yes                         7043 non-null   bool   
 7   PhoneService_Yes                       7043 non-null   bool   
 8   MultipleLines_No phone service         7043 non-null   bool   
 9   MultipleLines_Yes                      7043 non-null   bool   
 10  InternetService_Fiber optic            7043 non-null   bool   
 11  InternetService_No                     7043 non-null   bool   
 12  OnlineSecurity_No internet service     7043 non-null   bool   
 13  OnlineSecurity_Yes                     7043 non-null   bool   
 14  OnlineBackup_No internet service       7043 non-null   bool   
 15  OnlineBackup_Yes                       7043 non-null   bool   
 16  DeviceProtection_No internet service   7043 non-null   bool   
 17  DeviceProtection_Yes                   7043 non-null   bool   
 18  TechSupport_No internet service        7043 non-null   bool   
 19  TechSupport_Yes                        7043 non-null   bool   
 20  StreamingTV_No internet service        7043 non-null   bool   
 21  StreamingTV_Yes                        7043 non-null   bool   
 22  StreamingMovies_No internet service    7043 non-null   bool   
 23  StreamingMovies_Yes                    7043 non-null   bool   
 24  Contract_One year                      7043 non-null   bool   
 25  Contract_Two year                      7043 non-null   bool   
 26  PaperlessBilling_Yes                   7043 non-null   bool   
 27  PaymentMethod_Credit card (automatic)  7043 non-null   bool   
 28  PaymentMethod_Electronic check         7043 non-null   bool   
 29  PaymentMethod_Mailed check             7043 non-null   bool   
 30  Churn_Yes                              7043 non-null   bool   
dtypes: bool(27), float64(2), int64(2)
memory usage: 405.9 KB
# 3. Preparación de variables (asegurando el nombre correcto tras get_dummies)
# Al usar get_dummies, 'Churn_Yes' es el nuevo nombre de la columna target

X = df.drop('Churn_Yes', axis=1)
X
      SeniorCitizen  ...  PaymentMethod_Mailed check
0                 0  ...                       False
1                 0  ...                        True
2                 0  ...                        True
3                 0  ...                       False
4                 0  ...                       False
...             ...  ...                         ...
7038              0  ...                        True
7039              0  ...                       False
7040              0  ...                       False
7041              1  ...                        True
7042              0  ...                       False

[7043 rows x 30 columns]
y = df['Churn_Yes']
y
0       False
1       False
2        True
3       False
4        True
        ...  
7038    False
7039    False
7040    False
7041     True
7042    False
Name: Churn_Yes, Length: 7043, dtype: bool
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
# 4. Entrenamiento
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
RandomForestClassifier(random_state=42)
# 5. Predicción y Evaluación
y_pred = modelo.predict(X_test)
# Visualización
cm = confusion_matrix(y_test, y_pred)
cm
array([[1385,  167],
       [ 284,  277]])
plt.figure(figsize=(8, 6))
<Figure size 800x600 with 0 Axes>
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Churn', 'Churn'], 
            yticklabels=['No Churn', 'Churn'])
<Axes: >
plt.ylabel('Real')
Text(70.72222222222221, 0.5, 'Real')
plt.xlabel('Predicho')
Text(0.5, 36.72222222222221, 'Predicho')
plt.title('Matriz de Confusión - Retención de Clientes')
Text(0.5, 1.0, 'Matriz de Confusión - Retención de Clientes')
plt.show()
print(classification_report(y_test, y_pred))
              precision    recall  f1-score   support

       False       0.83      0.89      0.86      1552
        True       0.62      0.49      0.55       561

    accuracy                           0.79      2113
   macro avg       0.73      0.69      0.71      2113
weighted avg       0.78      0.79      0.78      2113

# GUARDAR EL MODELO ENTRENADO
import joblib # Necesario para guardar el modelo
# Guardar el modelo
joblib.dump(modelo, 'modelo_telco_customer_churn.pkl')
['modelo_telco_customer_churn.pkl']