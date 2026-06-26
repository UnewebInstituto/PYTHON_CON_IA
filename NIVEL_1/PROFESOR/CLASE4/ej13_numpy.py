# Transposición y remodelación de una matriz
data.reshape(2, 3)
array([[1, 2, 3],
       [4, 5, 6]])
data.reshape(2, 3)
array([[1, 2, 3],
       [4, 5, 6]])
data.reshape(3, 2)
array([[1, 2],
       [3, 4],
       [5, 6]])
arr = np.arange(6).reshape((2, 3))
arr
array([[0, 1, 2],
       [3, 4, 5]])
arr.transpose()
array([[0, 3],
       [1, 4],
       [2, 5]])
arr.T
array([[0, 3],
       [1, 4],
       [2, 5]])
# Cómo invertir una matriz
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr)
reversed_arr
array([8, 7, 6, 5, 4, 3, 2, 1])
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
arr_2d
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
np.flip(arr_2d)
array([[12, 11, 10,  9],
       [ 8,  7,  6,  5],
       [ 4,  3,  2,  1]])
reversed_arr_rows = np.flip(arr_2d, axis=0)
reversed_arr_rows
array([[ 9, 10, 11, 12],
       [ 5,  6,  7,  8],
       [ 1,  2,  3,  4]])
reversed_arr_columns = np.flip(arr_2d, axis=1)
reversed_arr_columns
array([[ 4,  3,  2,  1],
       [ 8,  7,  6,  5],
       [12, 11, 10,  9]])
arr_2d[1] = np.flip(arr_2d[1])
arr_2d[1]
array([8, 7, 6, 5])
arr_2d[:,1] = np.flip(arr_2d[:,1])
arr_2d
array([[ 1, 10,  3,  4],
       [ 8,  7,  6,  5],
       [ 9,  2, 11, 12]])
arr_2d[:,1] = np.flip(arr_2d[:,2])
arr_2d
array([[ 1, 11,  3,  4],
       [ 8,  6,  6,  5],
       [ 9,  3, 11, 12]])
