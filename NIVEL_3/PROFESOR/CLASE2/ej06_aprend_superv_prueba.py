Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Importación de dependencias
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
# 1. Cargar datos
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
df
      Order ID  Order Date      Customer Name Region  ... Discount     Sales    Profit Payment Mode
0        10001  2024-10-19       Kashvi Varty  South  ...        5   68958.6  10525.09   Debit Card
1        10002  2025-08-30        Advik Desai  North  ...       20   33732.0   6299.66   Debit Card
2        10003  2023-11-04         Rhea Kalla   East  ...       20  207603.2  19850.27  Credit Card
3        10004  2025-05-23          Anika Sen   East  ...       15  158610.0  36311.02          UPI
4        10005  2025-01-19        Akarsh Kaul   West  ...       10   45033.3   9050.04   Debit Card
...        ...         ...                ...    ...  ...      ...       ...       ...          ...
4995     14996  2024-06-25   Nishith Kulkarni   East  ...        0  182013.0  11853.15   Debit Card
4996     14997  2024-12-22      Aaina Chander  North  ...        0  350240.0  31237.23  Credit Card
4997     14998  2025-04-15       Dhanush Gara  South  ...       15   35837.7   7827.50   Debit Card
4998     14999  2024-07-08  Divyansh Malhotra   East  ...       10   48844.8   6603.86  Credit Card
4999     15000  2024-02-04       Aarush Walla   West  ...       10   69085.8   5785.85  Net Banking

[5000 rows x 14 columns]
# 2. Calcular el Margen de Utilidad (Profit / Sales * 100)
# Esto convierte el valor absoluto a un porcentaje crudo
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Profit_Margin'] = df['Profit_Margin'].fillna(0) # Manejo de posibles errores de división
df
      Order ID  Order Date      Customer Name Region  ...     Sales    Profit Payment Mode Profit_Margin
0        10001  2024-10-19       Kashvi Varty  South  ...   68958.6  10525.09   Debit Card     15.262911
1        10002  2025-08-30        Advik Desai  North  ...   33732.0   6299.66   Debit Card     18.675620
2        10003  2023-11-04         Rhea Kalla   East  ...  207603.2  19850.27  Credit Card      9.561640
3        10004  2025-05-23          Anika Sen   East  ...  158610.0  36311.02          UPI     22.893273
4        10005  2025-01-19        Akarsh Kaul   West  ...   45033.3   9050.04   Debit Card     20.096329
...        ...         ...                ...    ...  ...       ...       ...          ...           ...
4995     14996  2024-06-25   Nishith Kulkarni   East  ...  182013.0  11853.15   Debit Card      6.512255
4996     14997  2024-12-22      Aaina Chander  North  ...  350240.0  31237.23  Credit Card      8.918807
4997     14998  2025-04-15       Dhanush Gara  South  ...   35837.7   7827.50   Debit Card     21.841524
4998     14999  2024-07-08  Divyansh Malhotra   East  ...   48844.8   6603.86  Credit Card     13.520088
4999     15000  2024-02-04       Aarush Walla   West  ...   69085.8   5785.85  Net Banking      8.374876

[5000 rows x 15 columns]
# 3. Normalizar el margen a un rango estrictamente entre 0 y 100
# Esto asegura que cualquier valor extremo sea ajustado a tu escala objetivo
scaler = MinMaxScaler(feature_range=(0, 100))
df['Profit_Scaled'] = scaler.fit_transform(df[['Profit_Margin']])
df['Profit_Scaled']
0       51.321636
1       68.389672
2       22.807769
3       89.483494
4       75.495089
          ...    
4995     7.556827
4996    19.592759
4997    84.223367
4998    42.605224
4999    16.872386
Name: Profit_Scaled, Length: 5000, dtype: float64
df['Profit_Margin']
0       15.262911
1       18.675620
2        9.561640
3       22.893273
4       20.096329
          ...    
4995     6.512255
4996     8.918807
4997    21.841524
4998    13.520088
4999     8.374876
Name: Profit_Margin, Length: 5000, dtype: float64
X = df[['Sales', 'Quantity', 'Discount']]
# 4. Definir features (X) y el nuevo objetivo escalado (y)
X = df[['Sales', 'Quantity', 'Discount']]
y = df['Profit_Scaled'] # Ahora y está entre 0 y 100
X
         Sales  Quantity  Discount
0      68958.6         2         5
1      33732.0         1        20
2     207603.2         4        20
3     158610.0         5        15
4      45033.3         1        10
...        ...       ...       ...
4995  182013.0         3         0
4996  350240.0         5         0
4997   35837.7         1        15
4998   48844.8         4        10
4999   69085.8         1        10

[5000 rows x 3 columns]
y
0       51.321636
1       68.389672
2       22.807769
3       89.483494
4       75.495089
          ...    
4995     7.556827
4996    19.592759
4997    84.223367
4998    42.605224
4999    16.872386
Name: Profit_Scaled, Length: 5000, dtype: float64
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 5. Entrenar la regresión
reg = LinearRegression()
X_train
          Sales  Quantity  Discount
4227  126296.00         2        20
4676  293628.00         5        20
800   214807.35         3         5
3671   13572.00         3        20
4193   21420.00         2         0
...         ...       ...       ...
4426    8998.40         4        20
466   186052.00         4         0
3092   47826.90         1        10
3772  204116.00         5        20
860    42118.40         4        20

[4000 rows x 3 columns]
y_train
4227    31.514144
4676    65.528500
800     10.973132
3671    99.753477
4193    39.709203
          ...    
4426    80.106677
466     33.379555
3092    68.349100
3772    63.914647
860     27.235508
Name: Profit_Scaled, Length: 4000, dtype: float64
# Resultado
predicciones = reg.predict(X_test)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    predicciones = reg.predict(X_test)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\linear_model\_base.py", line 355, in predict
    return super().predict(X)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\linear_model\_base.py", line 316, in predict
    return self._decision_function(X)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\linear_model\_base.py", line 292, in _decision_function
    check_is_fitted(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\utils\validation.py", line 1718, in check_is_fitted
    raise NotFittedError(msg % {"name": type(estimator).__name__})
sklearn.exceptions.NotFittedError: This LinearRegression instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.

= RESTART: C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\NIVEL_3\PROFESOR\CLASE2\ej06_aprendizaje_supervisado.py
Error cuadrático medio en escala 0-100: 833.4562437029342
Ejemplo de predicción (valor entre 0 y 100): 49.27%
reg.fit(X_train, y_train)
LinearRegression()
predicciones = reg.predict(X_test)
mse = mean_squared_error(y_test, predicciones)
print(f"Error cuadrático medio en escala 0-100: {mse}")
Error cuadrático medio en escala 0-100: 833.4562437029342
print(f"Ejemplo de predicción (valor entre 0 y 100): {predicciones[0]:.2f}%")
Ejemplo de predicción (valor entre 0 y 100): 49.27%
