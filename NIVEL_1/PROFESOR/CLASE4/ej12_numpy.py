#Generando números aleatorios
rng.integers(5, size=(2, 4))
array([[4, 4, 3, 1],
       [3, 1, 1, 0]])
#Cómo obtener artículos únicos y recuentos
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(a)
unique_values
array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
unique_values, indices_list = np.unique(a, return_index=True)
indices_list
array([ 0,  2,  3,  4,  5,  6,  7, 12, 13, 14])
unique_values, occurrence_count = np.unique(a, return_counts=True)
occurrence_count
array([3, 2, 2, 2, 1, 1, 1, 1, 1, 1])
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
a_2d
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [ 1,  2,  3,  4]])
unique_values = np.unique(a_2d)
unique_values
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
unique_rows = np.unique(a_2d, axis=0)
unique_rows
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
unique_rows, indices, occurrence_count = np.unique(
     a_2d, axis=0, return_counts=True, return_index=True)
unique_rows
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
indices
array([0, 1, 2])
occurrence_count
array([2, 1, 1])
