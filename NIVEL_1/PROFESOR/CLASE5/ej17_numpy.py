# Importación y exportación de un archivo CSV

import pandas as pd

x = pd.read_csv('./CLASE5/music.csv', header=0).values
                    
print(x)
                    
[['Billie Holiday' 'Jazz' 1300000 27000000]
 ['Jimmie Hendrix' 'Rock' 2700000 70000000]
 ['Miles Davis' 'Jazz' 1500000 48000000]
 ['SIA' 'Pop' 2000000 74000000]]
x1 = pd.read_csv('./CLASE5/music.csv', usecols=['Artista', 'Estilo']).values
                    
x1
                    
array([['Billie Holiday', 'Jazz'],
       ['Jimmie Hendrix', 'Rock'],
       ['Miles Davis', 'Jazz'],
       ['SIA', 'Pop']], dtype=object)
