import numpy as np
import pandas as pd
pd.Series(np.random.randint(0, 7, size=10))
0    6
1    0
2    5
3    3
4    0
5    0
6    1
7    4
8    6
9    6
dtype: int32
s = pd.Series(np.random.randint(0, 7, size=10))
s
0    3
1    4
2    3
3    5
4    2
5    1
6    3
7    3
8    2
9    6
dtype: int32
s.value_counts()
3    4
2    2
4    1
5    1
1    1
6    1
Name: count, dtype: int64
# Métodos de cadena
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
s
0       A
1       B
2       C
3    Aaba
4    Baca
5     NaN
6    CABA
7     dog
8     cat
dtype: str
s.str.lower()
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: str
# Fusión
# Concatenar
df = pd.DataFrame(np.random.randn(10, 4))
df
          0         1         2         3
0  1.381356  1.113404 -0.313923 -0.693670
1 -0.773665 -1.512256 -0.601476  1.118995
2 -0.534362  0.246619 -0.343125 -1.768484
3  0.957522  1.124976  0.626459  0.241159
4 -0.443120 -1.204962  1.032126  1.814067
5  0.405115  0.698618 -0.166374 -0.770497
6  0.492711 -1.764612 -1.554043 -0.805663
7 -0.167849  0.804997  0.215966  2.366756
8 -0.725277  0.862644 -1.903005  0.311952
9  1.034561 -0.807976  0.509896  0.176442
dF[:3]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dF[:3]
NameError: name 'dF' is not defined. Did you mean: 'df'?
df[:3]
          0         1         2         3
0  1.381356  1.113404 -0.313923 -0.693670
1 -0.773665 -1.512256 -0.601476  1.118995
2 -0.534362  0.246619 -0.343125 -1.768484
df[3:7]
          0         1         2         3
3  0.957522  1.124976  0.626459  0.241159
4 -0.443120 -1.204962  1.032126  1.814067
5  0.405115  0.698618 -0.166374 -0.770497
6  0.492711 -1.764612 -1.554043 -0.805663
df[7:0]
Empty DataFrame
Columns: [0, 1, 2, 3]
Index: []
df[7:]
          0         1         2         3
7 -0.167849  0.804997  0.215966  2.366756
8 -0.725277  0.862644 -1.903005  0.311952
9  1.034561 -0.807976  0.509896  0.176442
pieces = [df[:3], df[3:7], df[7:]]
pieces
[          0         1         2         3
0  1.381356  1.113404 -0.313923 -0.693670
1 -0.773665 -1.512256 -0.601476  1.118995
2 -0.534362  0.246619 -0.343125 -1.768484,           0         1         2         3
3  0.957522  1.124976  0.626459  0.241159
4 -0.443120 -1.204962  1.032126  1.814067
5  0.405115  0.698618 -0.166374 -0.770497
6  0.492711 -1.764612 -1.554043 -0.805663,           0         1         2         3
7 -0.167849  0.804997  0.215966  2.366756
8 -0.725277  0.862644 -1.903005  0.311952
9  1.034561 -0.807976  0.509896  0.176442]
pd.concat(pieces)
          0         1         2         3
0  1.381356  1.113404 -0.313923 -0.693670
1 -0.773665 -1.512256 -0.601476  1.118995
2 -0.534362  0.246619 -0.343125 -1.768484
3  0.957522  1.124976  0.626459  0.241159
4 -0.443120 -1.204962  1.032126  1.814067
5  0.405115  0.698618 -0.166374 -0.770497
6  0.492711 -1.764612 -1.554043 -0.805663
7 -0.167849  0.804997  0.215966  2.366756
8 -0.725277  0.862644 -1.903005  0.311952
9  1.034561 -0.807976  0.509896  0.176442
# Unión
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
left
   key  lval
0  foo     1
1  foo     2
right
   key  rval
0  foo     4
1  foo     5
pd.merge(left, right, on="key")
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
left
   key  lval
0  foo     1
1  bar     2
right
   key  rval
0  foo     4
1  bar     5
pd.merge(left, right, on="key")
   key  lval  rval
0  foo     1     4
1  bar     2     5
# Agrupación n
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
df
     A      B         C         D
0  foo    one -1.292483  0.718898
1  bar    one -0.828798  0.069831
2  foo    two  0.179578  0.042239
3  bar  three -2.318623  0.183196
4  foo    two -0.562497 -1.358858
5  bar    two  0.240527  0.705809
6  foo    one  1.277400 -0.383967
7  foo  three  0.737853  0.618678
df.groupby("A")[["C","D"]].sum()
            C         D
A                      
bar -2.906894  0.958835
foo  0.339850 -0.363010
df.groupby(["A","B"]).sum()
                  C         D
A   B                        
bar one   -0.828798  0.069831
    three -2.318623  0.183196
    two    0.240527  0.705809
foo one   -0.015084  0.334931
    three  0.737853  0.618678
    two   -0.382919 -1.316619
# Remodelando
# Pila
arrays = [
   ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
   ["one", "two", "one", "two", "one", "two", "one", "two"],
]
arrays
[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
index
MultiIndex([('bar', 'one'),
            ('bar', 'two'),
            ('baz', 'one'),
            ('baz', 'two'),
            ('foo', 'one'),
            ('foo', 'two'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
df
                     A         B
first second                    
bar   one    -0.149322 -1.150640
      two     0.549847  1.220433
baz   one    -2.194054 -1.100742
      two     0.267964 -0.166536
foo   one     0.436974  3.100368
      two     0.773136 -0.549211
qux   one     1.305269  0.660778
      two     1.540606 -0.300607
df2 = df[:4]
df2
                     A         B
first second                    
bar   one    -0.149322 -1.150640
      two     0.549847  1.220433
baz   one    -2.194054 -1.100742
      two     0.267964 -0.166536
df2
                     A         B
first second                    
bar   one    -0.149322 -1.150640
      two     0.549847  1.220433
baz   one    -2.194054 -1.100742
      two     0.267964 -0.166536
df2.stack()
first  second   
bar    one     A   -0.149322
               B   -1.150640
       two     A    0.549847
               B    1.220433
baz    one     A   -2.194054
               B   -1.100742
       two     A    0.267964
               B   -0.166536
dtype: float64
stacked = df2.stack()
stacked
first  second   
bar    one     A   -0.149322
               B   -1.150640
       two     A    0.549847
               B    1.220433
baz    one     A   -2.194054
               B   -1.100742
       two     A    0.267964
               B   -0.166536
dtype: float64
stacked.unstack()
                     A         B
first second                    
bar   one    -0.149322 -1.150640
      two     0.549847  1.220433
baz   one    -2.194054 -1.100742
      two     0.267964 -0.166536
stacked.unstack(1)
second        one       two
first                      
bar   A -0.149322  0.549847
      B -1.150640  1.220433
baz   A -2.194054  0.267964
      B -1.100742 -0.166536
stacked.unstack(0)
first          bar       baz
second                      
one    A -0.149322 -2.194054
       B -1.150640 -1.100742
two    A  0.549847  0.267964
       B  1.220433 -0.166536
