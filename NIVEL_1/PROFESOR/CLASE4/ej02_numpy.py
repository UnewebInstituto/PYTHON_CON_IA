estudiantes = [['MARIA',23],['SUSANA',25],['YOLANDA',29]]
estudiantes
[['MARIA', 23], ['SUSANA', 25], ['YOLANDA', 29]]
# Fundamentos de arrays
a = np.array([1, 2, 3, 4, 5, 6])
a
SyntaxError: multiple statements found while compiling a single statement
a = np.array([1, 2, 3, 4, 5, 6])
a
array([1, 2, 3, 4, 5, 6])
a[0]
np.int64(1)
a[1]
np.int64(2)
for data in a:
    data

    
np.int64(1)
np.int64(2)
np.int64(3)
np.int64(4)
np.int64(5)
np.int64(6)
a[2] = 33
a[2]
np.int64(33)
for data in a:
    data

    
np.int64(1)
np.int64(2)
np.int64(33)
np.int64(4)
np.int64(5)
np.int64(6)
a[:3]
array([ 1,  2, 33])
a[3:]
array([4, 5, 6])
a[-1]
np.int64(6)
b = a[:3]
c = a[3:]
b
array([ 1,  2, 33])
c
array([4, 5, 6])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
a[1,3]
np.int64(8)
a[0,0]
np.int64(1)
a[2,3]
np.int64(12)
