
import numpy from np
SyntaxError: Did you mean to use 'from ... import ...' instead?
import numpy as np
import pandas as pd
import matplotlib plt
SyntaxError: invalid syntax
import matplotlib as plt
import parquet
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    import parquet
ModuleNotFoundError: No module named 'parquet'
import pyarrow
import parquet
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import parquet
ModuleNotFoundError: No module named 'parquet'
df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
df.to_parquet("./NIVEL_2/PROFESOR/CLASE2/foo.parquet")
In [141]: df.to_excel("./NIVEL_2/PROFESOR/CLASE2/foo.xlsx", sheet_name="Sheet1")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    In [141]: df.to_excel("./NIVEL_2/PROFESOR/CLASE2/foo.xlsx", sheet_name="Sheet1")
NameError: name 'In' is not defined
df.to_excel("./NIVEL_2/PROFESOR/CLASE2/foo.xlsx", sheet_name="Sheet1")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df.to_excel("./NIVEL_2/PROFESOR/CLASE2/foo.xlsx", sheet_name="Sheet1")
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 2312, in to_excel
    formatter.write(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\io\formats\excel.py", line 1003, in write
    writer = ExcelWriter(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 58, in __init__
    from openpyxl.workbook import Workbook
ModuleNotFoundError: No module named 'openpyxl'
df.to_excel("./NIVEL_2/PROFESOR/CLASE2/foo.xlsx", sheet_name="Sheet1")
  


pd.Series([False, True, False])
  
0    False
1     True
2    False
dtype: bool
if pd.Series([False, True, False]):
  print("Si hay un valor True")

  
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    if pd.Series([False, True, False]):
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\core\generic.py", line 1513, in __bool__
    raise ValueError(
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
