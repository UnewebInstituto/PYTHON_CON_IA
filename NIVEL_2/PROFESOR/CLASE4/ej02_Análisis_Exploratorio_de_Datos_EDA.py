# EDA: ANÁLISIS EXPLORATORIO DE DATOS
import pandas as pd
# Carga de datos
df = pd.read_csv('./NIVEL_2/PROFESOR/CLASE4/datos_pacientes.csv')
df
     ID  Edad  Glucosa  Presion Estado_Salud
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
# Inspección básica
print(df.info())
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            100 non-null    int64  
 1   Edad          100 non-null    int64  
 2   Glucosa       100 non-null    float64
 3   Presion       100 non-null    float64
 4   Estado_Salud  100 non-null    str    
dtypes: float64(2), int64(2), str(1)
memory usage: 4.6 KB
None
print(df.describe())
               ID        Edad     Glucosa     Presion
count  100.000000  100.000000  100.000000  100.000000
mean    50.500000   50.800000  100.438000  118.498200
std     29.011492   21.068431   14.000142   10.947856
min      1.000000   18.000000   62.520000   91.210000
25%     25.750000   31.750000   91.282500  111.190000
50%     50.500000   52.000000  100.570000  118.030000
75%     75.250000   70.000000  110.262500  124.777500
max    100.000000   82.000000  132.380000  142.730000
print(df.head())
   ID  Edad  Glucosa  Presion Estado_Salud
0   1    69    85.99   101.50         Sano
1   2    32   111.76   131.69      Enfermo
2   3    78    90.78   110.15      Enfermo
3   4    38   104.99   109.06         Sano
4   5    41    79.29    91.21         Sano
sns.boxplot(x='Estado_Salud', y='Glucosa', data=df)
<Axes: xlabel='Estado_Salud', ylabel='Glucosa'>
plt.title("Distribución de Glucosa por Estado de Salud")
Text(0.5, 1.0, 'Distribución de Glucosa por Estado de Salud')
plt.show()
# Carga de datos con basura (garbage)
df1 = pd.read_csv('./NIVEL_2/PROFESOR/CLASE4/datos_pacientes_garbage.csv')
# Inspección básica
print(df.info())
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            100 non-null    int64  
 1   Edad          100 non-null    int64  
 2   Glucosa       100 non-null    float64
 3   Presion       100 non-null    float64
 4   Estado_Salud  100 non-null    str    
dtypes: float64(2), int64(2), str(1)
memory usage: 4.6 KB
None
print(df1.info())
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            100 non-null    int64  
 1   Edad          100 non-null    int64  
 2   Glucosa       100 non-null    float64
 3   Presion       100 non-null    float64
 4   Estado_Salud  90 non-null     str    
dtypes: float64(2), int64(2), str(1)
memory usage: 4.5 KB
None
print(df1.describe())
               ID        Edad     Glucosa      Presion
count  100.000000  100.000000  100.000000   100.000000
mean    50.500000   50.800000  100.438000   234.488200
std     29.011492   21.068431   14.000142   617.791357
min      1.000000   18.000000   62.520000    91.210000
25%     25.750000   31.750000   91.282500   111.190000
50%     50.500000   52.000000  100.570000   118.720000
75%     75.250000   70.000000  110.262500   128.425000
max    100.000000   82.000000  132.380000  5000.000000
print(df.head())
   ID  Edad  Glucosa  Presion Estado_Salud
0   1    69    85.99   101.50         Sano
1   2    32   111.76   131.69      Enfermo
2   3    78    90.78   110.15      Enfermo
3   4    38   104.99   109.06         Sano
4   5    41    79.29    91.21         Sano
# Ver cuánto porcentaje de datos falta por columna
nulos = df.isnull().mean() * 100
nulos
ID              0.0
Edad            0.0
Glucosa         0.0
Presion         0.0
Estado_Salud    0.0
dtype: float64
nulos = df1.isnull().mean() * 100
print(df1.head())
   ID  Edad  Glucosa  Presion Estado_Salud
0   1    69    85.99   101.50         Sano
1   2    32   111.76   131.69      Enfermo
2   3    78    90.78   110.15      Enfermo
3   4    38   104.99   109.06         Sano
4   5    41    79.29    91.21         Sano
nulos = df1.isnull().mean() * 100
nulos
ID               0.0
Edad             0.0
Glucosa          0.0
Presion          0.0
Estado_Salud    10.0
dtype: float64
df1.fillna(df.median(), inplace=True)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    df1.fillna(df.median(), inplace=True)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 14594, in median
    result = super().median(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 11843, in median
    return self._stat_function(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 11785, in _stat_function
    return self._reduce(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13633, in _reduce
    res = df._mgr.reduce(blk_func)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\managers.py", line 1681, in reduce
    res_blocks = [blk.reduce(func) for blk in self.blocks]
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\blocks.py", line 358, in reduce
    result = func(self.values)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13561, in blk_func
    return values._reduce(name, skipna=skipna, keepdims=True, **kwds)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py", line 563, in _reduce
    raise TypeError(f"Cannot perform reduction '{name}' with string dtype")
TypeError: Cannot perform reduction 'median' with string dtype
df1 = pd.read_csv('./NIVEL_2/PROFESOR/CLASE4/datos_pacientes_garbage.csv')
print(df1.info())
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            100 non-null    int64  
 1   Edad          100 non-null    int64  
 2   Glucosa       100 non-null    float64
 3   Presion       90 non-null     float64
 4   Estado_Salud  100 non-null    str    
dtypes: float64(2), int64(2), str(1)
memory usage: 4.6 KB
None
print(df1.describe())
               ID        Edad     Glucosa     Presion
count  100.000000  100.000000  100.000000   90.000000
mean    50.500000   50.800000  100.438000  118.986778
std     29.011492   21.068431   14.000142   10.893811
min      1.000000   18.000000   62.520000  100.090000
25%     25.750000   31.750000   91.282500  111.672500
50%     50.500000   52.000000  100.570000  118.655000
75%     75.250000   70.000000  110.262500  124.972500
max    100.000000   82.000000  132.380000  142.730000

nulos = df1.isnull().mean() * 100
nulos
ID               0.0
Edad             0.0
Glucosa          0.0
Presion         10.0
Estado_Salud     0.0
dtype: float64
df1
  
     ID  Edad  Glucosa  Presion Estado_Salud
0     1    69    85.99   101.50         Sano
1     2    32   111.76   131.69      Enfermo
2     3    78    90.78      NaN      Enfermo
3     4    38   104.99      NaN         Sano
4     5    41    79.29      NaN         Sano
..  ...   ...      ...      ...          ...
95   96    52   101.59   113.96         Sano
96   97    82   113.81   114.51         Sano
97   98    64    96.60   130.97         Sano
98   99    20   109.80   141.13      Enfermo
99  100    18   116.54   115.02      Enfermo

[100 rows x 5 columns]
df1.fillna(df.median(), inplace=True)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    df1.fillna(df.median(), inplace=True)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 14594, in median
    result = super().median(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 11843, in median
    return self._stat_function(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 11785, in _stat_function
    return self._reduce(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13633, in _reduce
    res = df._mgr.reduce(blk_func)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\managers.py", line 1681, in reduce
    res_blocks = [blk.reduce(func) for blk in self.blocks]
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\blocks.py", line 358, in reduce
    result = func(self.values)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13561, in blk_func
    return values._reduce(name, skipna=skipna, keepdims=True, **kwds)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py", line 563, in _reduce
    raise TypeError(f"Cannot perform reduction '{name}' with string dtype")
TypeError: Cannot perform reduction 'median' with string dtype
df1.fillna(df1.median(), inplace=True)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    df1.fillna(df1.median(), inplace=True)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 14594, in median
    result = super().median(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 11843, in median
    return self._stat_function(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 11785, in _stat_function
    return self._reduce(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13633, in _reduce
    res = df._mgr.reduce(blk_func)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\managers.py", line 1681, in reduce
    res_blocks = [blk.reduce(func) for blk in self.blocks]
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\blocks.py", line 358, in reduce
    result = func(self.values)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13561, in blk_func
    return values._reduce(name, skipna=skipna, keepdims=True, **kwds)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py", line 563, in _reduce
    raise TypeError(f"Cannot perform reduction '{name}' with string dtype")
TypeError: Cannot perform reduction 'median' with string dtype
df1.fillna(df1.median(numeric_only=True), inplace=True)
     ID  Edad  Glucosa  Presion Estado_Salud
0     1    69    85.99  101.500         Sano
1     2    32   111.76  131.690      Enfermo
2     3    78    90.78  118.655      Enfermo
3     4    38   104.99  118.655         Sano
4     5    41    79.29  118.655         Sano
..  ...   ...      ...      ...          ...
95   96    52   101.59  113.960         Sano
96   97    82   113.81  114.510         Sano
97   98    64    96.60  130.970         Sano
98   99    20   109.80  141.130      Enfermo
99  100    18   116.54  115.020      Enfermo

[100 rows x 5 columns]
df1 = pd.read_csv('./NIVEL_2/PROFESOR/CLASE4/datos_pacientes_garbage.csv')
print(df1.info())
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            100 non-null    int64  
 1   Edad          100 non-null    int64  
 2   Glucosa       100 non-null    float64
 3   Presion       90 non-null     float64
 4   Estado_Salud  100 non-null    str    
dtypes: float64(2), int64(2), str(1)
memory usage: 4.6 KB
None
print(df1.describe())
  
               ID        Edad     Glucosa      Presion
count  100.000000  100.000000  100.000000    90.000000
mean    50.500000   50.800000  100.438000   273.876222
std     29.011492   21.068431   14.000142   839.881363
min      1.000000   18.000000   62.520000   100.090000
25%     25.750000   31.750000   91.282500   111.672500
50%     50.500000   52.000000  100.570000   118.805000
75%     75.250000   70.000000  110.262500   125.685000
max    100.000000   82.000000  132.380000  5000.000000
nulos = df1.isnull().mean() * 100
nulos
ID               0.0
Edad             0.0
Glucosa          0.0
Presion         10.0
Estado_Salud     0.0
dtype: float64
df1.fillna(df1.mean(numeric_only=True), inplace=True)
     ID  Edad  Glucosa      Presion Estado_Salud
0     1    69    85.99   101.500000         Sano
1     2    32   111.76   131.690000      Enfermo
2     3    78    90.78   273.876222      Enfermo
3     4    38   104.99   273.876222         Sano
4     5    41    79.29   273.876222         Sano
..  ...   ...      ...          ...          ...
95   96    52   101.59  4800.000000         Sano
96   97    82   113.81   114.510000         Sano
97   98    64    96.60  4500.000000         Sano
98   99    20   109.80   141.130000      Enfermo
99  100    18   116.54  5000.000000      Enfermo

[100 rows x 5 columns]
df1 = pd.read_csv('./NIVEL_2/PROFESOR/CLASE4/datos_pacientes_garbage.csv')
print(df1.info())
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   ID            100 non-null    int64  
 1   Edad          100 non-null    int64  
 2   Glucosa       100 non-null    float64
 3   Presion       90 non-null     float64
 4   Estado_Salud  100 non-null    str    
dtypes: float64(2), int64(2), str(1)
memory usage: 4.6 KB
None
print(df1.describe())
               ID        Edad     Glucosa      Presion
count  100.000000  100.000000  100.000000    90.000000
mean    50.500000   50.800000  100.438000   273.876222
std     29.011492   21.068431   14.000142   839.881363
min      1.000000   18.000000   62.520000   100.090000
25%     25.750000   31.750000   91.282500   111.672500
50%     50.500000   52.000000  100.570000   118.805000
75%     75.250000   70.000000  110.262500   125.685000
max    100.000000   82.000000  132.380000  5000.000000
nulos = df1.isnull().mean() * 100
nulos
ID               0.0
Edad             0.0
Glucosa          0.0
Presion         10.0
Estado_Salud     0.0
dtype: float64
df1.fillna(df1.median(numeric_only=True), inplace=True)
     ID  Edad  Glucosa   Presion Estado_Salud
0     1    69    85.99   101.500         Sano
1     2    32   111.76   131.690      Enfermo
2     3    78    90.78   118.805      Enfermo
3     4    38   104.99   118.805         Sano
4     5    41    79.29   118.805         Sano
..  ...   ...      ...       ...          ...
95   96    52   101.59  4800.000         Sano
96   97    82   113.81   114.510         Sano
97   98    64    96.60  4500.000         Sano
98   99    20   109.80   141.130      Enfermo
99  100    18   116.54  5000.000      Enfermo

[100 rows x 5 columns]
import seaborn as sns
import matplotlib.pyplot as plt
# Boxplot para ver la distribución y outliers de la presión arteria
# Boxplot para ver la distribución y outliers de la presión arterial
sns.boxplot(x=df1['Presion'])
<Axes: xlabel='Presion'>
plt.title("Detección de Outliers en Presión")
Text(0.5, 1.0, 'Detección de Outliers en Presión')
plt.show()
# Mapa de calor de correlaciones
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 13133, in corr
    mat = data.to_numpy(dtype=float, na_value=np.nan, copy=False)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 2081, in to_numpy
    result = self._mgr.as_array(dtype=dtype, copy=copy, na_value=na_value)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\managers.py", line 1872, in as_array
    arr = self._interleave(dtype=dtype, na_value=na_value)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\internals\managers.py", line 1925, in _interleave
    arr = blk.values.to_numpy(  # type: ignore[union-attr]
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\arrays\arrow\array.py", line 1729, in to_numpy
    result = result.astype(dtype, copy=False)
ValueError: could not convert string to float: 'Sano'
df
  
     ID  Edad  Glucosa  Presion Estado_Salud
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
sns.pairplot(df, hue='Estado_Salud')
  
<seaborn.axisgrid.PairGrid object at 0x0000011E42C60470>

plt.show()
  


sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
  
<Axes: >
plt.show()
  
plt.show()
  
sns.pairplot(df, hue='Estado_Salud')
  
<seaborn.axisgrid.PairGrid object at 0x0000011E42C60470>
plt.show()
  
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
  
<Axes: >
plt.show()
  
