#Indexación y segmentación
# ¿Se puede redimensionar un array?
a = np.arange(6)
a
array([0, 1, 2, 3, 4, 5])
print(a)
[0 1 2 3 4 5]
b = a.reshape(3,2)
b
array([[0, 1],
       [2, 3],
       [4, 5]])
np.reshape(a, shape=(1,6))
array([[0, 1, 2, 3, 4, 5]])
# Cómo convertir una matriz 1D en una matriz 2D (cómo agregar un nuevo eje a una matriz)
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)
a2 = a[np.newaxis, :]
a2.shape
(1, 6)
a2
array([[1, 2, 3, 4, 5, 6]])
row_vector = a[np.newaxis, :]
row_vector
array([[1, 2, 3, 4, 5, 6]])
row_vector.shape
(1, 6)
col_vector = a[:, np.newaxis]
col_vector
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
col_vector.shape
(6, 1)
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
(6,)
b = np.expand_dims(a, axis=1)
b
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
a
array([1, 2, 3, 4, 5, 6])
b.shape
(6, 1)
a.shape
(6,)
c = np.expand_dims(a, axis=0)
c
array([[1, 2, 3, 4, 5, 6]])
c.shape
(1, 6)
#Indexación y segmentación
data = np.array([1, 2, 3])
data
array([1, 2, 3])
data[1]
np.int64(2)
data[0:2]
array([1, 2])
data[1:]
array([2, 3])
data[-2:]
array([2, 3])
