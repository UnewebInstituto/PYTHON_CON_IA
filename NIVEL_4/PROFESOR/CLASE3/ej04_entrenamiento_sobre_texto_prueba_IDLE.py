Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
df = pd.read_csv('./NIVEL_4/PROFESOR/CLASE3/dataset_arroz.csv')
df
   id  ...    fuente
0   1  ...       web
1   2  ...  encuesta
2   3  ...       app
3   4  ...       web
4   5  ...  encuesta
5   6  ...       web

[6 rows x 5 columns]
# Visualizar el balance de los datos
print(df['polaridad'].value_counts())
polaridad
1    3
0    3
Name: count, dtype: int64
# Separar para entrenamiento
textos = df['texto_original']
textos
0           Excelente uniformidad y color cristalino
1        El grano presenta alto porcentaje de yesado
2      Mucho contenido de granos rotos en el empaque
3    El arroz tiene una calidad excelente muy blanco
4                       Sabor neutro y buena cocción
5        Demasiadas impurezas y restos de cascarilla
Name: texto_original, dtype: str
type(textos)
<class 'pandas.Series'>
etiquetas = df['polaridad']
etiquetas
0    1
1    0
2    0
3    1
4    1
5    0
Name: polaridad, dtype: int64
print("TEXTOS:")
TEXTOS:
print(textos)
0           Excelente uniformidad y color cristalino
1        El grano presenta alto porcentaje de yesado
2      Mucho contenido de granos rotos en el empaque
3    El arroz tiene una calidad excelente muy blanco
4                       Sabor neutro y buena cocción
5        Demasiadas impurezas y restos de cascarilla
Name: texto_original, dtype: str
print("ETIQUETAS:")
ETIQUETAS:
print(etiquetas)
0    1
1    0
2    0
3    1
4    1
5    0
Name: polaridad, dtype: int64
print(textos)
0           Excelente uniformidad y color cristalino
1        El grano presenta alto porcentaje de yesado
2      Mucho contenido de granos rotos en el empaque
3    El arroz tiene una calidad excelente muy blanco
4                       Sabor neutro y buena cocción
5        Demasiadas impurezas y restos de cascarilla
Name: texto_original, dtype: str
