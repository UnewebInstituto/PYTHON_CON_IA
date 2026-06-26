# Atributos de matrices
a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
a.ndim
2
a.shape
(3, 4)
len(a.shape) == a.ndim
True
a.size
12
import math
a.size == math.prod(a.shape)
True

a.size
12
math.prod(a.shape)
12
a.dtype
dtype('int64')
#Cómo crear una matriz básica
np.zeros(2)
array([0., 0.])
np.ones(2)
array([1., 1.])
np.empty(2)
array([1., 1.])
np.arange(4)
array([0, 1, 2, 3])
np.arange(2,9,2)
array([2, 4, 6, 8])
np.linspace(0,10,num=5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
np.linspace(0,10,num=7)
array([ 0.        ,  1.66666667,  3.33333333,  5.        ,  6.66666667,
        8.33333333, 10.        ])
np.linspace(0,10,num=10)
array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
np.dtype(np.linspace(0,10,num=10))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    np.dtype(np.linspace(0,10,num=10))
TypeError: Cannot construct a dtype from an array
x = np.linspace(0,10,num=10)
x
array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])
dtype(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dtype(a)
NameError: name 'dtype' is not defined. Did you mean: 'type'?
a.dtype()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.dtype()
TypeError: 'numpy.dtypes.Int64DType' object is not callable
a.dtype
dtype('int64')
x.dtype
dtype('float64')
y = np.ones(2, dtype=np.int64)
y
array([1, 1])
