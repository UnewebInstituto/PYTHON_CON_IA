import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
# 1. Cargar datos
ruta = "C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv"
df = pd.read_csv(ruta)
df
      Order ID  Order Date      Customer Name  ...     Sales    Profit Payment Mode
0        10001  2024-10-19       Kashvi Varty  ...   68958.6  10525.09   Debit Card
1        10002  2025-08-30        Advik Desai  ...   33732.0   6299.66   Debit Card
2        10003  2023-11-04         Rhea Kalla  ...  207603.2  19850.27  Credit Card
3        10004  2025-05-23          Anika Sen  ...  158610.0  36311.02          UPI
4        10005  2025-01-19        Akarsh Kaul  ...   45033.3   9050.04   Debit Card
...        ...         ...                ...  ...       ...       ...          ...
4995     14996  2024-06-25   Nishith Kulkarni  ...  182013.0  11853.15   Debit Card
4996     14997  2024-12-22      Aaina Chander  ...  350240.0  31237.23  Credit Card
4997     14998  2025-04-15       Dhanush Gara  ...   35837.7   7827.50   Debit Card
4998     14999  2024-07-08  Divyansh Malhotra  ...   48844.8   6603.86  Credit Card
4999     15000  2024-02-04       Aarush Walla  ...   69085.8   5785.85  Net Banking

[5000 rows x 14 columns]
# 2. Ingeniería de variables (Debemos crear X e y aquí)
# Calculamos el margen y creamos el target
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df
      Order ID  Order Date      Customer Name  ...    Profit Payment Mode Profit_Margin
0        10001  2024-10-19       Kashvi Varty  ...  10525.09   Debit Card     15.262911
1        10002  2025-08-30        Advik Desai  ...   6299.66   Debit Card     18.675620
2        10003  2023-11-04         Rhea Kalla  ...  19850.27  Credit Card      9.561640
3        10004  2025-05-23          Anika Sen  ...  36311.02          UPI     22.893273
4        10005  2025-01-19        Akarsh Kaul  ...   9050.04   Debit Card     20.096329
...        ...         ...                ...  ...       ...          ...           ...
4995     14996  2024-06-25   Nishith Kulkarni  ...  11853.15   Debit Card      6.512255
4996     14997  2024-12-22      Aaina Chander  ...  31237.23  Credit Card      8.918807
4997     14998  2025-04-15       Dhanush Gara  ...   7827.50   Debit Card     21.841524
4998     14999  2024-07-08  Divyansh Malhotra  ...   6603.86  Credit Card     13.520088
4999     15000  2024-02-04       Aarush Walla  ...   5785.85  Net Banking      8.374876

[5000 rows x 15 columns]
df['Target_Alto_Valor'] = (df['Profit_Margin'] > 10).astype(int) # Ajusta este umbral según necesites
df
      Order ID  Order Date  ... Profit_Margin Target_Alto_Valor
0        10001  2024-10-19  ...     15.262911                 1
1        10002  2025-08-30  ...     18.675620                 1
2        10003  2023-11-04  ...      9.561640                 0
3        10004  2025-05-23  ...     22.893273                 1
4        10005  2025-01-19  ...     20.096329                 1
...        ...         ...  ...           ...               ...
4995     14996  2024-06-25  ...      6.512255                 0
4996     14997  2024-12-22  ...      8.918807                 0
4997     14998  2025-04-15  ...     21.841524                 1
4998     14999  2024-07-08  ...     13.520088                 1
4999     15000  2024-02-04  ...      8.374876                 0

[5000 rows x 16 columns]
# Preprocesamiento: convertimos columnas categóricas a numéricas
df_model = pd.get_dummies(df, columns=['Category', 'Payment Mode'], drop_first=True)
df_model
      Order ID  Order Date  ... Payment Mode_Net Banking Payment Mode_UPI
0        10001  2024-10-19  ...                    False            False
1        10002  2025-08-30  ...                    False            False
2        10003  2023-11-04  ...                    False            False
3        10004  2025-05-23  ...                    False             True
4        10005  2025-01-19  ...                    False            False
...        ...         ...  ...                      ...              ...
4995     14996  2024-06-25  ...                    False            False
4996     14997  2024-12-22  ...                    False            False
4997     14998  2025-04-15  ...                    False            False
4998     14999  2024-07-08  ...                    False            False
4999     15000  2024-02-04  ...                     True            False

[5000 rows x 27 columns]
# Definimos X e y (aquí es donde se crean y dejan de dar error)
features = ['Sales', 'Quantity', 'Discount', 'Profit']
X = df_model[features]
X
         Sales  Quantity  Discount    Profit
0      68958.6         2         5  10525.09
1      33732.0         1        20   6299.66
2     207603.2         4        20  19850.27
3     158610.0         5        15  36311.02
4      45033.3         1        10   9050.04
...        ...       ...       ...       ...
4995  182013.0         3         0  11853.15
4996  350240.0         5         0  31237.23
4997   35837.7         1        15   7827.50
4998   48844.8         4        10   6603.86
4999   69085.8         1        10   5785.85

[5000 rows x 4 columns]
y = df_model['Target_Alto_Valor']
y
0       1
1       1
2       0
3       1
4       1
       ..
4995    0
4996    0
4997    1
4998    1
4999    0
Name: Target_Alto_Valor, Length: 5000, dtype: int64
# 3. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 4. Entrenamiento
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)
DecisionTreeClassifier()
# 5. Predicción y Evaluación
y_pred = modelo.predict(X_test)
y_pred
array([1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1,
       0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1,
       1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1,
       0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0,
       1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1,
       1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
       1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,
       1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
       1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1,
       0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1,
       0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0,
       1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
       1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1,
       1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
       1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1,
       0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0,
       1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
       0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1,
       1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1,
       1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1,
       0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
       1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1,
       1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1,
       0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1,
       1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1,
       1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1,
       1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
       0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0,
       0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
       1, 1, 1, 1, 1, 1, 1, 0, 1, 1])
cm = confusion_matrix(y_test, y_pred)
cm
array([[244,  17],
       [ 10, 729]])
"""
|  | Predicción: Negativo | Predicción: Positivo |
| --- | --- | --- |
| **Real: Negativo** | Verdadero Negativo (TN) | Falso Positivo (FP) |
| **Real: Positivo** | Falso Negativo (FN) | Verdadero Positivo (TP) |
"""
'\n|  | Predicción: Negativo | Predicción: Positivo |\n| --- | --- | --- |\n| **Real: Negativo** | Verdadero Negativo (TN) | Falso Positivo (FP) |\n| **Real: Positivo** | Falso Negativo (FN) | Verdadero Positivo (TP) |\n'
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
<Axes: >
plt.title('Matriz de Confusión')
Text(0.5, 1.0, 'Matriz de Confusión')
plt.show()
print(classification_report(y_test, y_pred))
              precision    recall  f1-score   support

           0       0.96      0.93      0.95       261
           1       0.98      0.99      0.98       739

    accuracy                           0.97      1000
   macro avg       0.97      0.96      0.96      1000
weighted avg       0.97      0.97      0.97      1000

