#Agregar, eliminar y ordenar elementos
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
arr
array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    np.sort()
TypeError: sort() missing 1 required positional argument: 'a'
np.sort
<function sort at 0x0000024AC2FEDD30>
np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a,b))
array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
x
array([[1, 2],
       [3, 4]])
y
array([[5, 6]])
np.concatenate((x,y), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
