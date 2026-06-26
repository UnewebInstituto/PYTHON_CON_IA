Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
from sqlalchemy import create_engine
db_engine1 = create_engine('postgresql+psycopg2://postgres:1234567@localhost:5432/nivel2_clase5')
type(db_engine1)
<class 'sqlalchemy.engine.base.Engine'>
df1 = pd.read_sql("SELECT * FROM pacientes", db_engine1)
df1
     id  edad  glucosa  presion estado_salud
0     1    69    85.99   101.50         Sano
1     2    32   111.76   131.69      Enfermo
2     3    78    90.78   110.15      Enfermo
3     4    38   104.99   109.06         Sano
4     5    41    79.29    91.21         Sano
..  ...   ...      ...      ...          ...
95   96    52   101.59   113.96         Sano
96   97    82   113.81   114.51         Sano
97   98    64    96.60   130.97         Sano
98   99    20   109.80   141.13      Enfermo
99  100    18   116.54   115.02      Enfermo

[100 rows x 5 columns]
