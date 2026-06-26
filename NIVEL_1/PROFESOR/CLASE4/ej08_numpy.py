# FILTROS
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a.shape
(3, 4)
a[a < 5]
array([1, 2, 3, 4])
a[a < 7]
array([1, 2, 3, 4, 5, 6])
five_up = (a >= 5)
five_up
array([[False, False, False, False],
       [ True,  True,  True,  True],
       [ True,  True,  True,  True]])
a[five_up]
array([ 5,  6,  7,  8,  9, 10, 11, 12])
divible_by_2 = a[a%2 == 0]
divible_by_2
array([ 2,  4,  6,  8, 10, 12])
a[a%2 == 0]
array([ 2,  4,  6,  8, 10, 12])
a%2 == 0
array([[False,  True, False,  True],
       [False,  True, False,  True],
       [False,  True, False,  True]])
c = a[(a > 2) & (a < 11)]
c
array([ 3,  4,  5,  6,  7,  8,  9, 10])
five_up = (a > 5) | (a == 5)
five_up
array([[False, False, False, False],
       [ True,  True,  True,  True],
       [ True,  True,  True,  True]])
a[five_up]
array([ 5,  6,  7,  8,  9, 10, 11, 12])
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.nonzero(a < 5)
b
(array([0, 0, 0, 0]), array([0, 1, 2, 3]))
list_of_coordinates= list(zip(b[0], b[1]))
for coord in list_of_coordinates:
    coord

    
(np.int64(0), np.int64(0))
(np.int64(0), np.int64(1))
(np.int64(0), np.int64(2))
(np.int64(0), np.int64(3))
# Con la expresión declarada en b
a[b]
array([1, 2, 3, 4])
not_there = np.nonzero(a == 42)
not_there
(array([], dtype=int64), array([], dtype=int64))