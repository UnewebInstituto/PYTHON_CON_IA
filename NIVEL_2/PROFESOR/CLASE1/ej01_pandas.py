Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import pandas as pd
# Creación de objetos
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
print(s)
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
s[0]
np.float64(1.0)
dates = pd.date_range("20130101", periods=6)
dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[us]', freq='D')
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df
                   A         B         C         D
2013-01-01  0.408807  0.741082 -1.290134 -0.950353
2013-01-02  1.961139 -0.861096 -1.522369  0.547394
2013-01-03  0.573022 -0.677756 -0.591325 -0.272942
2013-01-04 -0.597186 -1.218812 -0.543601  1.338703
2013-01-05 -0.598447 -1.205771  1.105156  0.748690
2013-01-06  0.056708 -1.207275  1.770051  1.389452
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
df2.dtypes
A           float64
B    datetime64[us]
C           float32
D             int32
E          category
F               str
dtype: object
