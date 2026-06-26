# Dependencias
import pandas as pd
import numpy as np

# 1. Carga
df = pd.read_csv('Rice_MSC_Dataset.csv')

valores_unicos = df['CLASS'].unique()
print('--- CLASES DE ARROZ EN LA MUESTRA ---')
print(valores_unicos)


# 2. Limpieza de datos (Laboratorio)
# Verificar nulos es obligatorio. Si hay nulos en análisis de calidad, 
# el lote no puede ser clasificado.
def limpiar_lote(df):
    # Imputar nulos por la media del atributo (o eliminar filas si es crítico)
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())
    # Eliminar posibles duplicados que ensucien el análisis de lotes
    df = df.drop_duplicates()
    return df

df = limpiar_lote(df)
# Al terminar de crear/transformar columnas, re-creamos el df para compactar la memoria
df = df.copy()

valores_unicos = df['CLASS'].unique()
print("Valores únicos en la columna 'CLASS':", valores_unicos)
# Valores únicos en la columna 'CLASS':
# 'Basmati', 'Arborio', 'Jasmine', 'Ipsala', 'Karacadag'

df['Calidad_Aceptable'] = np.where(df['CLASS'] == 'Basmati', 1, 0)

# 4. Eliminación de variables no predictivas
# CLASS ya no lo necesitamos al haber creado nuestra nueva variable binaria
df = df.drop(columns=['CLASS'])

print(f"Dataset listo: {df.shape[0]} granos analizados, {df.shape[1]} características.")

