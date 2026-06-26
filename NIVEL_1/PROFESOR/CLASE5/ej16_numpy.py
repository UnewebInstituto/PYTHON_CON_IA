#Trabajando con guardado y recuperación de matrices con numpy 
#como archivos
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
[1 2 3 4 5 6]
np.save('./CLASE5/filename.npy',a)
b = np.load('./CLASE5/filename.npy')
b
array([1, 2, 3, 4, 5, 6])
print(b)
[1 2 3 4 5 6]
csv_arr = np.array([1,2,3,4,5,6,7,8])
print(csv_arr)
[1 2 3 4 5 6 7 8]
np.savetxt('./CLASE5/new_file.csv',csv_arr)
np.loadtxt('./CLASE5/new_file.csv')
array([1., 2., 3., 4., 5., 6., 7., 8.])