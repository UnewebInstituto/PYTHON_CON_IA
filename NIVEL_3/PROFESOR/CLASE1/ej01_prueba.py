Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Carga de dependencias
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
# 1. Cargar datos
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
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
# 2. Calcular el Margen de Ganancia Porcentual
# Margen = (Profit / Sales) * 100
# Si Sales es 0, evitamos división por cero usando fillna(0)
10525.09/68958.6 * 100
15.262911370010409
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0)
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
# 3. Ajustar el valor para que esté estrictamente en el rango 0-100
# Usamos MinMaxScaler para forzar cualquier valor a estar entre 0 y 100
scaler = MinMaxScaler(feature_range=(0, 100))
scaler
MinMaxScaler(feature_range=(0, 100))
df['Profit_Scaled'] = scaler.fit_transform(df[['Profit_Margin']])
df
      Order ID  Order Date  ... Profit_Margin Profit_Scaled
0        10001  2024-10-19  ...     15.262911     51.321636
1        10002  2025-08-30  ...     18.675620     68.389672
2        10003  2023-11-04  ...      9.561640     22.807769
3        10004  2025-05-23  ...     22.893273     89.483494
4        10005  2025-01-19  ...     20.096329     75.495089
...        ...         ...  ...           ...           ...
4995     14996  2024-06-25  ...      6.512255      7.556827
4996     14997  2024-12-22  ...      8.918807     19.592759
4997     14998  2025-04-15  ...     21.841524     84.223367
4998     14999  2024-07-08  ...     13.520088     42.605224
4999     15000  2024-02-04  ...      8.374876     16.872386

[5000 rows x 16 columns]
# 4. Ahora definimos el Target (Ejemplo: ¿Es altamente rentable? > 80 en la escala 0-100)
df['Target_Alto_Valor'] = (df['Profit_Scaled'] > 80).astype(int)
df
      Order ID  Order Date  ... Profit_Scaled Target_Alto_Valor
0        10001  2024-10-19  ...     51.321636                 0
1        10002  2025-08-30  ...     68.389672                 0
2        10003  2023-11-04  ...     22.807769                 0
3        10004  2025-05-23  ...     89.483494                 1
4        10005  2025-01-19  ...     75.495089                 0
...        ...         ...  ...           ...               ...
4995     14996  2024-06-25  ...      7.556827                 0
4996     14997  2024-12-22  ...     19.592759                 0
4997     14998  2025-04-15  ...     84.223367                 1
4998     14999  2024-07-08  ...     42.605224                 0
4999     15000  2024-02-04  ...     16.872386                 0

[5000 rows x 17 columns]
# Convertimos categóricas a numéricas para que el modelo no falle

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

[5000 rows x 28 columns]
features = ['Sales', 'Quantity', 'Discount', 'Profit_Scaled'] + [c for c in df_model.columns if 'Category_' in c or 'Payment Mode_' in c]
features
['Sales', 'Quantity', 'Discount', 'Profit_Scaled', 'Category_Books', 'Category_Clothing', 'Category_Electronics', 'Category_Furniture', 'Category_Groceries', 'Category_Home Decor', 'Category_Kitchen', 'Category_Sports', 'Category_Toys', 'Payment Mode_Credit Card', 'Payment Mode_Debit Card', 'Payment Mode_Net Banking', 'Payment Mode_UPI']
X = df_model[features]
y = df['Target_Alto_Valor']
X
         Sales  Quantity  ...  Payment Mode_Net Banking  Payment Mode_UPI
0      68958.6         2  ...                     False             False
1      33732.0         1  ...                     False             False
2     207603.2         4  ...                     False             False
3     158610.0         5  ...                     False              True
4      45033.3         1  ...                     False             False
...        ...       ...  ...                       ...               ...
4995  182013.0         3  ...                     False             False
4996  350240.0         5  ...                     False             False
4997   35837.7         1  ...                     False             False
4998   48844.8         4  ...                     False             False
4999   69085.8         1  ...                      True             False

[5000 rows x 17 columns]
y
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
Name: Target_Alto_Valor, Length: 5000, dtype: int64
# 6. Entrenamiento con DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train
          Sales  Quantity  ...  Payment Mode_Net Banking  Payment Mode_UPI
4227  126296.00         2  ...                      True             False
4676  293628.00         5  ...                     False              True
800   214807.35         3  ...                      True             False
3671   13572.00         3  ...                     False             False
4193   21420.00         2  ...                     False             False
...         ...       ...  ...                       ...               ...
4426    8998.40         4  ...                     False             False
466   186052.00         4  ...                     False              True
3092   47826.90         1  ...                     False              True
3772  204116.00         5  ...                     False             False
860    42118.40         4  ...                     False             False

[4000 rows x 17 columns]
X_test
         Sales  Quantity  ...  Payment Mode_Net Banking  Payment Mode_UPI
1501    6343.0         1  ...                     False              True
2586  297496.0         4  ...                     False             False
2653   90024.0         3  ...                      True             False
1055  223760.0         4  ...                     False             False
705   235236.0         5  ...                      True             False
...        ...       ...  ...                       ...               ...
4711    6586.4         1  ...                     False              True
2313  129490.7         2  ...                     False             False
3214   34569.0         5  ...                      True             False
2732    4054.5         5  ...                     False              True
1926   98708.0         2  ...                     False              True

[1000 rows x 17 columns]
y_train
4227    0
4676    0
800     0
3671    1
4193    0
       ..
4426    1
466     0
3092    0
3772    0
860     0
Name: Target_Alto_Valor, Length: 4000, dtype: int64
y_test
1501    0
2586    0
2653    1
1055    0
705     1
       ..
4711    0
2313    0
3214    0
2732    0
1926    0
Name: Target_Alto_Valor, Length: 1000, dtype: int64
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)
DecisionTreeClassifier()
print("Modelo entrenado con Profit escalado entre 0 y 100.")
Modelo entrenado con Profit escalado entre 0 y 100.
predicciones = modelo.predict(X_test)
print(f"Precisión del modelo: {accuracy_score(y_test, predicciones)}")
Precisión del modelo: 1.0
