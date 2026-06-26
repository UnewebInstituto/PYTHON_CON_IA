# Radiodifusión
data = np.array([1.0, 2.0])
data * 1.6
array([1.6, 3.2])
# Operaciones de matriz más útiles
data = np.array([1, 2, 3])
data.min()
np.int64(1)
data.max()
np.int64(3)
data.sum()
np.int64(6)
a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
a.sum()
np.float64(4.8595784)
a.min()
np.float64(0.05093587)
a.max()
np.float64(0.82485143)
# Creación de matrices
data = np.array([[1, 2], [3, 4], [5, 6]])
data
array([[1, 2],
       [3, 4],
       [5, 6]])
data[0,1]
np.int64(2)
data[1:3]
array([[3, 4],
       [5, 6]])
data(0:2, 0)
SyntaxError: invalid syntax
data[0:2, 0]
array([1, 3])
data.max()
np.int64(6)
data.min()
np.int64(1)
data.sum()
np.int64(21)
data = np.array([[1, 2], [5, 3], [4, 6]])
data
array([[1, 2],
       [5, 3],
       [4, 6]])
data.max(axis=0)
array([5, 6])
data.max(axis=1)
array([2, 5, 6])
data = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
data + ones
array([[2, 3],
       [4, 5]])
data
array([[1, 2],
       [3, 4]])
ones
array([[1, 1],
       [1, 1]])
data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
data
array([[1, 2],
       [3, 4],
       [5, 6]])
ones_row
array([[1, 1]])
data + ones_row
array([[2, 3],
       [4, 5],
       [6, 7]])
data * ones_row
array([[1, 2],
       [3, 4],
       [5, 6]])
data - ones_row
array([[0, 1],
       [2, 3],
       [4, 5]])
data / ones_row
array([[1., 2.],
       [3., 4.],
       [5., 6.]])
np.ones((4, 3, 2))
array([[[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]],

       [[1., 1.],
        [1., 1.],
        [1., 1.]]])
np.ones(3)
array([1., 1., 1.])
np.zeros(3)
array([0., 0., 0.])
array([0., 0., 0.])
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    array([0., 0., 0.])
NameError: name 'array' is not defined. Did you mean: 'arr1'? Or did you forget to import 'array'?
rng = np.random.default_rng()
rng
Generator(PCG64) at 0x24AC3A304A0
rng.random(3)
array([0.57905855, 0.76088999, 0.2488582 ])
rng.random(3)
array([0.53653086, 0.71586236, 0.8467803 ])
rng.random(3)
array([0.2053848 , 0.80122608, 0.53188418])
rng.random(3)
array([0.96667319, 0.58904338, 0.88890188])
np.ones((3, 2))
array([[1., 1.],
       [1., 1.],
       [1., 1.]])
np.zeros((3, 2))
array([[0., 0.],
       [0., 0.],
       [0., 0.]])
rng.random((3, 2))
array([[0.97373641, 0.27891136],
       [0.66923257, 0.49319178],
       [0.1695289 , 0.74038202]])
