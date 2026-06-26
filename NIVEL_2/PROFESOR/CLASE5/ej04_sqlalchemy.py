# Variables de entorno para acceso a BBDD (PASSWORD)

Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.environ.get('DB_PASSWORD')
'1234567'
connection_str = f'postgresql+psycopg2://posgres:{DB_PASSWORD}@localhost:5432/nivel2_prueba'
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    connection_str = f'postgresql+psycopg2://posgres:{DB_PASSWORD}@localhost:5432/nivel2_prueba'
NameError: name 'DB_PASSWORD' is not defined
db_pass = os.environ.get('DB_PASSWORD')
connection_str = f'postgresql+psycopg2://posgres:{db_pass}@localhost:5432/nivel2_prueba'
connection_str
'postgresql+psycopg2://posgres:1234567@localhost:5432/nivel2_prueba'
db_engine1 = create_engine(connection_str)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    db_engine1 = create_engine(connection_str)
NameError: name 'create_engine' is not defined
from sqlalchemy import create_engine
db_engine1 = create_engine(connection_str)
connection_str = f'postgresql+psycopg2://posgres:{db_pass}@localhost:5432/nivel2_clase5'
connection_str
'postgresql+psycopg2://posgres:1234567@localhost:5432/nivel2_clase5'
from sqlalchemy import create_engine
db_engine1 = create_engine(connection_str)
sql = "select * from pacientes"
import pandas as pd
df1 = pd.read_sql(sql, db_engine1)
Traceback (most recent call last):
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 144, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 3319, in raw_connection
    return self.pool.connect()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 448, in connect
    return _ConnectionFairy._checkout(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 1272, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 712, in checkout
    rec = pool._do_get()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\impl.py", line 178, in _do_get
    with util.safe_reraise():
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\impl.py", line 176, in _do_get
    return self._create_connection()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 389, in _create_connection
    return _ConnectionRecord(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 674, in __init__
    self.__connect()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 900, in __connect
    with util.safe_reraise():
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 896, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\create.py", line 667, in connect
    return dialect.connect(*cargs_tup, **cparams)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 630, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)  # type: ignore[no-any-return]  # NOQA: E501
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "posgres"


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    df1 = pd.read_sql(sql, db_engine1)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\io\sql.py", line 700, in read_sql
    with pandasSQL_builder(con) as pandas_sql:
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\io\sql.py", line 908, in pandasSQL_builder
    return SQLDatabase(con, schema, need_transaction)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\pandas\io\sql.py", line 1649, in __init__
    con = self.exit_stack.enter_context(con.connect())
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 3295, in connect
    return self._connection_cls(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 146, in __init__
    Connection._handle_dbapi_exception_noconnection(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 2450, in _handle_dbapi_exception_noconnection
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 144, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 3319, in raw_connection
    return self.pool.connect()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 448, in connect
    return _ConnectionFairy._checkout(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 1272, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 712, in checkout
    rec = pool._do_get()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\impl.py", line 178, in _do_get
    with util.safe_reraise():
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\impl.py", line 176, in _do_get
    return self._create_connection()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 389, in _create_connection
    return _ConnectionRecord(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 674, in __init__
    self.__connect()
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 900, in __connect
    with util.safe_reraise():
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\util\langhelpers.py", line 122, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\pool\base.py", line 896, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\create.py", line 667, in connect
    return dialect.connect(*cargs_tup, **cparams)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 630, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)  # type: ignore[no-any-return]  # NOQA: E501
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\psycopg2\__init__.py", line 135, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (::1), port 5432 failed: FATAL:  password authentication failed for user "posgres"

(Background on this error at: https://sqlalche.me/e/20/e3q8)
connection_str
'postgresql+psycopg2://posgres:1234567@localhost:5432/nivel2_clase5'
connection_str = f'postgresql+psycopg2://postgres:{db_pass}@localhost:5432/nivel2_clase5'
db_engine1 = create_engine(connection_str)
sql = "select * from pacientes"
df1 = pd.read_sql(sql, db_engine1)
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
