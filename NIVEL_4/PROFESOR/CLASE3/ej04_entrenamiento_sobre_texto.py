import pandas as pd

# Cargar el CSV
# df = pd.read_csv('/content/drive/MyDrive/data/dataset_arroz.csv')
df = pd.read_csv('dataset_arroz.csv')

# Visualizar el balance de los datos
print(df['polaridad'].value_counts())

# Separar para entrenamiento
textos = df['texto_original']
etiquetas = df['polaridad']

print("TEXTOS:")
print(textos)

print("ETIQUETAS:")
print(etiquetas)