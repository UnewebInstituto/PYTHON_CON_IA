import numpy as np
# Remodelación y aplanamiento de matrices multidimensionales
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(x)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
x
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
print(x)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
x.flatten()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
a1 = x.flatten()
a1
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
a1.shape()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a1.shape()
TypeError: 'tuple' object is not callable
a1.shape
(12,)
a1[0]=99
print(a1)
[99  2  3  4  5  6  7  8  9 10 11 12]
print(x)
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
# En el caso de flatten, los cambios en el array hijo no afectarán
# al array padre
"""
CASO ravel(), los cambios en el array hijo afectan al array padre
"""
'\nCASO ravel(), los cambios en el array hijo afectan al array padre\n'
a2 = x.ravel()
print(a2)
[ 1  2  3  4  5  6  7  8  9 10 11 12]
a[0] = 98
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a[0] = 98
NameError: name 'a' is not defined. Did you mean: 'a1'?
a2[0] = 98
print(a2)
[98  2  3  4  5  6  7  8  9 10 11 12]
print(x)
[[98  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
