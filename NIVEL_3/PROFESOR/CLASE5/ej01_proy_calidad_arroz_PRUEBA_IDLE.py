Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np

# 1. Carga
df = pd.read_csv('./NIVEL_3/PROFESOR/CLASE5/Rice_MSC_Dataset.csv')
df = pd.read_csv('./NIVEL_3/PROFESOR/CLASE5/Rice_MSC_Dataset.csv')
df
        AREA  PERIMETER  MAJOR_AXIS  MINOR_AXIS  ...  ALLdaub4XX  ALLdaub4YY  ALLdaub4ZZ      CLASS
0       7805    437.915    209.8215     48.0221  ...      0.3673      0.3793      0.4733    Basmati
1       7503    340.757    138.3361     69.8417  ...      0.3014      0.3144      0.3641    Arborio
2       5124    314.617    141.9803     46.5784  ...      0.3233      0.3445      0.4448    Jasmine
3       7990    437.085    201.4386     51.2245  ...      0.3880      0.4020      0.4904    Basmati
4       7433    342.893    140.3350     68.3927  ...      0.3184      0.3303      0.3928    Arborio
...      ...        ...         ...         ...  ...         ...         ...         ...        ...
74995   5551    285.911    114.1695     62.9079  ...      0.2895      0.2997      0.3455    Arborio
74996   7696    322.703    121.3900     81.1375  ...      0.3335      0.3426      0.4257  Karacadag
74997   7579    339.295    136.3125     71.2866  ...      0.3028      0.3164      0.3761    Arborio
74998  15174    489.502    200.9486     97.6282  ...      0.3970      0.4215      0.4469     Ipsala
74999  12931    452.635    185.5138     90.2651  ...      0.4162      0.4414      0.4626     Ipsala

[75000 rows x 107 columns]
valores_unicos = df['CLASS'].unique()
valores_unicos
<ArrowStringArray>
['Basmati', 'Arborio', 'Jasmine', 'Ipsala', 'Karacadag']
Length: 5, dtype: str
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
df
        AREA  PERIMETER  MAJOR_AXIS  MINOR_AXIS  ...  ALLdaub4XX  ALLdaub4YY  ALLdaub4ZZ      CLASS
0       7805    437.915    209.8215     48.0221  ...      0.3673      0.3793      0.4733    Basmati
1       7503    340.757    138.3361     69.8417  ...      0.3014      0.3144      0.3641    Arborio
2       5124    314.617    141.9803     46.5784  ...      0.3233      0.3445      0.4448    Jasmine
3       7990    437.085    201.4386     51.2245  ...      0.3880      0.4020      0.4904    Basmati
4       7433    342.893    140.3350     68.3927  ...      0.3184      0.3303      0.3928    Arborio
...      ...        ...         ...         ...  ...         ...         ...         ...        ...
74995   5551    285.911    114.1695     62.9079  ...      0.2895      0.2997      0.3455    Arborio
74996   7696    322.703    121.3900     81.1375  ...      0.3335      0.3426      0.4257  Karacadag
74997   7579    339.295    136.3125     71.2866  ...      0.3028      0.3164      0.3761    Arborio
74998  15174    489.502    200.9486     97.6282  ...      0.3970      0.4215      0.4469     Ipsala
74999  12931    452.635    185.5138     90.2651  ...      0.4162      0.4414      0.4626     Ipsala

[74703 rows x 107 columns]
# Al terminar de crear/transformar columnas, re-creamos el df para compactar la memoria
df = df.copy()
df
        AREA  PERIMETER  MAJOR_AXIS  MINOR_AXIS  ...  ALLdaub4XX  ALLdaub4YY  ALLdaub4ZZ      CLASS
0       7805    437.915    209.8215     48.0221  ...      0.3673      0.3793      0.4733    Basmati
1       7503    340.757    138.3361     69.8417  ...      0.3014      0.3144      0.3641    Arborio
2       5124    314.617    141.9803     46.5784  ...      0.3233      0.3445      0.4448    Jasmine
3       7990    437.085    201.4386     51.2245  ...      0.3880      0.4020      0.4904    Basmati
4       7433    342.893    140.3350     68.3927  ...      0.3184      0.3303      0.3928    Arborio
...      ...        ...         ...         ...  ...         ...         ...         ...        ...
74995   5551    285.911    114.1695     62.9079  ...      0.2895      0.2997      0.3455    Arborio
74996   7696    322.703    121.3900     81.1375  ...      0.3335      0.3426      0.4257  Karacadag
74997   7579    339.295    136.3125     71.2866  ...      0.3028      0.3164      0.3761    Arborio
74998  15174    489.502    200.9486     97.6282  ...      0.3970      0.4215      0.4469     Ipsala
74999  12931    452.635    185.5138     90.2651  ...      0.4162      0.4414      0.4626     Ipsala

[74703 rows x 107 columns]
# 3. Definición del Target
# Necesitamos convertir 'CLASS' a binario (Sano vs Defectuoso)
# Supongamos que tu columna CLASS tiene varios tipos de arroz.
# Definiremos 'Arroz_Premium' (1) y 'Otros/Defectuosos' (0)

# Ejemplo: si el arroz 'Normal' es el aceptado, el resto se marca como 0
# Ajusta 'Arroz_Normal' al valor real que aparezca en tu columna CLASS
valores_unicos = df['CLASS'].unique()
print("Valores únicos en la columna 'CLASS':", valores_unicos)
Valores únicos en la columna 'CLASS': <ArrowStringArray>
['Basmati', 'Arborio', 'Jasmine', 'Ipsala', 'Karacadag']
Length: 5, dtype: str
df['Calidad_Aceptable'] = np.where(df['CLASS'] == 'Basmati', 1, 0)
# 4. Eliminación de variables no predictivas
# CLASS ya no lo necesitamos al haber creado nuestra nueva variable binaria
df = df.drop(columns=['CLASS'])
df
        AREA  PERIMETER  MAJOR_AXIS  MINOR_AXIS  ...  ALLdaub4XX  ALLdaub4YY  ALLdaub4ZZ  Calidad_Aceptable
0       7805    437.915    209.8215     48.0221  ...      0.3673      0.3793      0.4733                  1
1       7503    340.757    138.3361     69.8417  ...      0.3014      0.3144      0.3641                  0
2       5124    314.617    141.9803     46.5784  ...      0.3233      0.3445      0.4448                  0
3       7990    437.085    201.4386     51.2245  ...      0.3880      0.4020      0.4904                  1
4       7433    342.893    140.3350     68.3927  ...      0.3184      0.3303      0.3928                  0
...      ...        ...         ...         ...  ...         ...         ...         ...                ...
74995   5551    285.911    114.1695     62.9079  ...      0.2895      0.2997      0.3455                  0
74996   7696    322.703    121.3900     81.1375  ...      0.3335      0.3426      0.4257                  0
74997   7579    339.295    136.3125     71.2866  ...      0.3028      0.3164      0.3761                  0
74998  15174    489.502    200.9486     97.6282  ...      0.3970      0.4215      0.4469                  0
74999  12931    452.635    185.5138     90.2651  ...      0.4162      0.4414      0.4626                  0

[74703 rows x 107 columns]
print(f"Dataset listo: {df.shape[0]} granos analizados, {df.shape[1]} características.")
Dataset listo: 74703 granos analizados, 107 características.
