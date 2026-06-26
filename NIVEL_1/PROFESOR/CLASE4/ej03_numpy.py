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

