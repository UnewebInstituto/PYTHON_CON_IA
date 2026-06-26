# Ej03
import pandas as pd
from sklearn.model_selection import train_test_split
# 1. Cargar el dataset
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
# 2. Ingeniería de variables: Crear la variable objetivo (Target)
# Definimos 1 si el Profit es mayor a 0 (Rentable), y 0 en caso contrario
df['is_profitable'] = (df['Profit'] > 0).astype(int)
df
      Order ID  Order Date      Customer Name  ...    Profit Payment Mode is_profitable
0        10001  2024-10-19       Kashvi Varty  ...  10525.09   Debit Card             1
1        10002  2025-08-30        Advik Desai  ...   6299.66   Debit Card             1
2        10003  2023-11-04         Rhea Kalla  ...  19850.27  Credit Card             1
3        10004  2025-05-23          Anika Sen  ...  36311.02          UPI             1
4        10005  2025-01-19        Akarsh Kaul  ...   9050.04   Debit Card             1
...        ...         ...                ...  ...       ...          ...           ...
4995     14996  2024-06-25   Nishith Kulkarni  ...  11853.15   Debit Card             1
4996     14997  2024-12-22      Aaina Chander  ...  31237.23  Credit Card             1
4997     14998  2025-04-15       Dhanush Gara  ...   7827.50   Debit Card             1
4998     14999  2024-07-08  Divyansh Malhotra  ...   6603.86  Credit Card             1
4999     15000  2024-02-04       Aarush Walla  ...   5785.85  Net Banking             1

[5000 rows x 15 columns]
# 3. Preprocesamiento: Codificación de variables categóricas
# Usamos 'drop_first=True' para evitar la multicolinealidad
df_encoded = pd.get_dummies(df, columns=['Category', 'Payment Mode', 'Region'], drop_first=True)
df_encoded
      Order ID  Order Date  ... Region_South Region_West
0        10001  2024-10-19  ...         True       False
1        10002  2025-08-30  ...        False       False
2        10003  2023-11-04  ...        False       False
3        10004  2025-05-23  ...        False       False
4        10005  2025-01-19  ...        False        True
...        ...         ...  ...          ...         ...
4995     14996  2024-06-25  ...        False       False
4996     14997  2024-12-22  ...        False       False
4997     14998  2025-04-15  ...         True       False
4998     14999  2024-07-08  ...        False       False
4999     15000  2024-02-04  ...        False        True

[5000 rows x 28 columns]
# 4. Selección de Features (X) y Target (y)
# Excluimos columnas no numéricas que no aportan valor predictivo directo o son identificadores
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
