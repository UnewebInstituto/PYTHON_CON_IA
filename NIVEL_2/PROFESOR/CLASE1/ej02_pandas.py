# Visualización de datos
df.head()
                   A         B         C         D
2013-01-01  0.408807  0.741082 -1.290134 -0.950353
2013-01-02  1.961139 -0.861096 -1.522369  0.547394
2013-01-03  0.573022 -0.677756 -0.591325 -0.272942
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
df.tail(3)
                   A         B         C         D
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
2013-01-06  0.056708 -1.207275  1.770051  1.389452
df.index
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[us]', freq='D')
df.columns
Index(['A', 'B', 'C', 'D'], dtype='str')
df.to_numpy()
array([[ 0.40880729,  0.74108227, -1.29013393, -0.95035257],
       [ 1.96113896, -0.86109552, -1.52236942,  0.54739427],
       [ 0.57302169, -0.67775578, -0.59132458, -0.2729422 ],
       [-0.59718582, -1.21881248, -0.54360103,  1.33870336],
       [-0.59844689, -1.20577106,  1.10515641,  0.74869015],
       [ 0.05670761, -1.20727468,  1.7700511 ,  1.3894517 ]])
df2.dtypes
A           float64
B    datetime64[us]
C           float32
D             int32
E          category
F               str
dtype: object
df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
df
                   A         B         C         D
2013-01-01  0.408807  0.741082 -1.290134 -0.950353
2013-01-02  1.961139 -0.861096 -1.522369  0.547394
2013-01-03  0.573022 -0.677756 -0.591325 -0.272942
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
2013-01-06  0.056708 -1.207275  1.770051  1.389452
df.describe()
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.300674 -0.738271 -0.178704  0.466824
std    0.950484  0.758508  1.325901  0.922280
min   -0.598447 -1.218812 -1.522369 -0.950353
25%   -0.433712 -1.206899 -1.115432 -0.067858
50%    0.232757 -1.033433 -0.567463  0.648042
75%    0.531968 -0.723591  0.692967  1.191200
max    1.961139  0.741082  1.770051  1.389452
df.T
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.408807    1.961139    0.573022   -0.597186   -0.598447    0.056708
B    0.741082   -0.861096   -0.677756   -1.218812   -1.205771   -1.207275
C   -1.290134   -1.522369   -0.591325   -0.543601    1.105156    1.770051
D   -0.950353    0.547394   -0.272942    1.338703    0.748690    1.389452
df
                   A         B         C         D
2013-01-01  0.408807  0.741082 -1.290134 -0.950353
2013-01-02  1.961139 -0.861096 -1.522369  0.547394
2013-01-03  0.573022 -0.677756 -0.591325 -0.272942
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
2013-01-06  0.056708 -1.207275  1.770051  1.389452
df.sort_index(axia=1, ascending=False)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    df.sort_index(axia=1, ascending=False)
TypeError: DataFrame.sort_index() got an unexpected keyword argument 'axia'
df.sort_index(axis=1, ascending=False)
                   D         C         B         A
2013-01-01 -0.950353 -1.290134  0.741082  0.408807
2013-01-02  0.547394 -1.522369 -0.861096  1.961139
2013-01-03 -0.272942 -0.591325 -0.677756  0.573022
2013-01-04  1.338703 -0.543601 -1.218812 -0.597186
2013-01-05  0.748690  1.105156 -1.205771 -0.598447
2013-01-06  1.389452  1.770051 -1.207275  0.056708
df.sort_index(axis=2, ascending=False)
Traceback (most recent call last):
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 523, in _get_axis_number
    return cls._AXIS_TO_AXIS_NUMBER[axis]
KeyError: 2

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    df.sort_index(axis=2, ascending=False)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\frame.py", line 8546, in sort_index
    return super().sort_index(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 5159, in sort_index
    axis = self._get_axis_number(axis)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 525, in _get_axis_number
    raise ValueError(
ValueError: No axis named 2 for object type DataFrame
df.sort_values(by="B")
                   A         B         C         D
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
2013-01-06  0.056708 -1.207275  1.770051  1.389452
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
2013-01-02  1.961139 -0.861096 -1.522369  0.547394
2013-01-03  0.573022 -0.677756 -0.591325 -0.272942
2013-01-01  0.408807  0.741082 -1.290134 -0.950353
df.sort_values(by="B", ascending=False )
                   A         B         C         D
2013-01-01  0.408807  0.741082 -1.290134 -0.950353
2013-01-03  0.573022 -0.677756 -0.591325 -0.272942
2013-01-02  1.961139 -0.861096 -1.522369  0.547394
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
2013-01-06  0.056708 -1.207275  1.770051  1.389452
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
