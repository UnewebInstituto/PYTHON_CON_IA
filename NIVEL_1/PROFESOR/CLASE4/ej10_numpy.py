# Operaciones básicas con matrices
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data
array([1, 2])
ones
array([1, 1])
data + ones
array([2, 3])
data - ones
array([0, 1])
data * ones
array([1, 2])
data / ones
array([1., 2.])
a = np.array([1, 2, 3, 4])
a.sum()
np.int64(10)
print(a.sum())
10
b = np.array([[1, 1], [2, 2]])
b
array([[1, 1],
       [2, 2]])
b.sum(axis=0)
array([3, 3])
b.sum(axis=1)
array([2, 4])