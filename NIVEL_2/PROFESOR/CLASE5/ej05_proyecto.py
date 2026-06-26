Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# PROYECTO NIVEL 2
import pandas as pd
df = pd.read_csv("./NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv')
                 
SyntaxError: unterminated string literal (detected at line 1)
df = pd.read_csv("./NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
                 
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
"""
CAMPOS DEL DATASET:
Order ID,Order Date,Customer Name,Region,City,Category,Sub-Category,Product Name,Quantity,Unit Price,Discount,Sales,Profit,Payment Mode
"""
                 
'\nCAMPOS DEL DATASET:\nOrder ID,Order Date,Customer Name,Region,City,Category,Sub-Category,Product Name,Quantity,Unit Price,Discount,Sales,Profit,Payment Mode\n'
df['fecha'] = pd.to_datetime(df['Order Date'])
                 
df
                 
      Order ID  Order Date  ... Payment Mode      fecha
0        10001  2024-10-19  ...   Debit Card 2024-10-19
1        10002  2025-08-30  ...   Debit Card 2025-08-30
2        10003  2023-11-04  ...  Credit Card 2023-11-04
3        10004  2025-05-23  ...          UPI 2025-05-23
4        10005  2025-01-19  ...   Debit Card 2025-01-19
...        ...         ...  ...          ...        ...
4995     14996  2024-06-25  ...   Debit Card 2024-06-25
4996     14997  2024-12-22  ...  Credit Card 2024-12-22
4997     14998  2025-04-15  ...   Debit Card 2025-04-15
4998     14999  2024-07-08  ...  Credit Card 2024-07-08
4999     15000  2024-02-04  ...  Net Banking 2024-02-04

[5000 rows x 15 columns]
df = df.dropna(subset=['Price', 'Sales'])
                 
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df = df.dropna(subset=['Price', 'Sales'])
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 7801, in dropna
    raise KeyError(np.array(subset)[check].tolist())
KeyError: ['Price']
df = df.dropna(subset=['Unit Price', 'Sales'])
df
      Order ID  Order Date  ... Payment Mode      fecha
0        10001  2024-10-19  ...   Debit Card 2024-10-19
1        10002  2025-08-30  ...   Debit Card 2025-08-30
2        10003  2023-11-04  ...  Credit Card 2023-11-04
3        10004  2025-05-23  ...          UPI 2025-05-23
4        10005  2025-01-19  ...   Debit Card 2025-01-19
...        ...         ...  ...          ...        ...
4995     14996  2024-06-25  ...   Debit Card 2024-06-25
4996     14997  2024-12-22  ...  Credit Card 2024-12-22
4997     14998  2025-04-15  ...   Debit Card 2025-04-15
4998     14999  2024-07-08  ...  Credit Card 2024-07-08
4999     15000  2024-02-04  ...  Net Banking 2024-02-04

[5000 rows x 15 columns]
import pandas as pd
df = pd.read_csv("./NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
# Convertir fechas y asegurar tipos numéricos
df['Order Date'] = pd.to_datetime(df['Order Date'])
cols_numericas = ['Quantity', 'Unit Price', 'Discount', 'Sales', 'Profit']
df[cols_numericas] = df[cols_numericas].apply(pd.to_numeric)
# Calcular margen de beneficio
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100
df
      Order ID Order Date      Customer Name  ...    Profit Payment Mode Profit Margin
0        10001 2024-10-19       Kashvi Varty  ...  10525.09   Debit Card     15.262911
1        10002 2025-08-30        Advik Desai  ...   6299.66   Debit Card     18.675620
2        10003 2023-11-04         Rhea Kalla  ...  19850.27  Credit Card      9.561640
3        10004 2025-05-23          Anika Sen  ...  36311.02          UPI     22.893273
4        10005 2025-01-19        Akarsh Kaul  ...   9050.04   Debit Card     20.096329
...        ...        ...                ...  ...       ...          ...           ...
4995     14996 2024-06-25   Nishith Kulkarni  ...  11853.15   Debit Card      6.512255
4996     14997 2024-12-22      Aaina Chander  ...  31237.23  Credit Card      8.918807
4997     14998 2025-04-15       Dhanush Gara  ...   7827.50   Debit Card     21.841524
4998     14999 2024-07-08  Divyansh Malhotra  ...   6603.86  Credit Card     13.520088
4999     15000 2024-02-04       Aarush Walla  ...   5785.85  Net Banking      8.374876

[5000 rows x 15 columns]
# Análisis rápido: Profit por Categoría
profit_por_cat = df.groupby('Category')['Profit'].sum().reset_index()
# Agrupación multidimensional para el dashboard
tendencia_geo = df.groupby(['Order Date', 'Region', 'Payment Mode'])[['Sales', 'Profit']].sum().reset_index()
tendencia_geo
     Order Date Region Payment Mode      Sales    Profit
0    2023-10-04   East          COD   18518.40   2273.75
1    2023-10-04  North   Debit Card    6458.40    724.54
2    2023-10-04  South          COD   39026.00   6959.45
3    2023-10-04  South  Credit Card   56847.00   4259.92
4    2023-10-04  South  Net Banking   77522.40  10882.22
...         ...    ...          ...        ...       ...
4239 2025-10-02  North   Debit Card   70674.30  17235.76
4240 2025-10-02  South  Net Banking   81936.00   6887.13
4241 2025-10-03  North  Net Banking  102049.20   9696.14
4242 2025-10-03   West  Net Banking   80057.25  13932.28
4243 2025-10-03   West          UPI   54671.00  12774.27

[4244 rows x 5 columns]
import matplotlib.pyplot as plt
import seaborn as sns
# Configuración de estética
plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
scatter = sns.scatterplot(
    data=df, 
    x='Sales', 
    y='Profit', 
    hue='Category', 
    size='Quantity', 
    sizes=(20, 200),  # Define el rango de tamaños de los puntos
    alpha=0.7         # Transparencia para ver puntos superpuestos
)
# Títulos y etiquetas
plt.title("Relación Ventas vs. Ganancia por Producto")
Text(0.5, 1.0, 'Relación Ventas vs. Ganancia por Producto')
plt.xlabel("Ventas")
Text(0.5, 0, 'Ventas')
plt.ylabel("Ganancia")
Text(0, 0.5, 'Ganancia')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Mueve la leyenda fuera del gráfico
<matplotlib.legend.Legend object at 0x0000018F7AAE6B40>
plt.tight_layout()
plt.show()
