# Consulta segmentada de los datos
query = """
SELECT id, edad, glucosa, presion 
FROM pacientes 
WHERE edad > 50
"""
# Se usará el motor de conexión establecido con PostgreSQL
# db_engine1
df3 = pd.read_sql(query, db_engine1)
df3
    id  edad  glucosa  presion
0    1    69    85.99   101.50
1    3    78    90.78   110.15
2    8    70   114.42   116.17
3   11    55   104.46   128.67
4   13    81    78.72   124.18
5   14    77   102.86   101.13
6   17    75   110.57   125.40
7   19    66    78.00   119.89
8   20    76   113.39   124.13
9   21    59    98.42   118.59
10  22    77    85.67   128.72
11  24    79    79.02   106.56
12  25    79    94.84   128.50
13  26    64   111.26   123.94
14  27    79    95.09   119.95
15  28    68    87.08   104.29
16  29    72    96.13   134.80
17  30    81   106.91   123.97
18  32    68    84.71   117.57
19  35    56   129.18   118.72
20  38    77    87.74   135.47
21  41    70    68.63   118.89
22  43    77    99.77   106.59
23  44    61    99.59   103.78
24  46    64    84.18   133.90
25  47    52    88.63   111.45
26  48    53   106.86   109.73
27  49    67    99.03   128.83
28  53    71   121.50   101.98
29  55    71    62.52   104.49
30  56    80   122.20   114.90
31  58    61   118.48   121.95
32  59    51    96.79   114.44
33  60    79    89.66   118.72
34  62    65    90.71   140.00
35  64    79    99.67   132.01
36  65    57   118.27   121.50
37  66    70    94.16   121.41
38  69    77   129.01   129.66
39  70    58   101.21   114.89
40  73    62   110.77   116.25
41  74    82    85.73   107.09
42  78    80    62.95   100.09
43  81    52    87.44   137.81
44  82    52   110.16   113.23
45  85    58    90.62   121.84
46  89    51   100.94   136.55
47  91    65    97.80   120.87
48  93    79   114.47   113.20
49  94    54    84.03   117.37
50  95    61   101.63   117.19
51  96    52   101.59   113.96
52  97    82   113.81   114.51
53  98    64    96.60   130.97
query = """
SELECT id, edad, glucosa 
FROM pacientes 
WHERE edad >= 50 AND estado_salud = 'Enfermo'
"""
query
"\nSELECT id, edad, glucosa \nFROM pacientes \nWHERE edad >= 50 AND estado_salud = 'Enfermo'\n"
df4 = pd.read_sql(query, db_engine1)
df4
    id  edad  glucosa
0    3    78    90.78
1   11    55   104.46
2   13    81    78.72
3   14    77   102.86
4   16    50   109.12
5   19    66    78.00
6   20    76   113.39
7   21    59    98.42
8   22    77    85.67
9   29    72    96.13
10  47    52    88.63
11  55    71    62.52
12  64    79    99.67
13  65    57   118.27
14  73    62   110.77
15  81    52    87.44
16  83    50   128.08
17  85    58    90.62
18  89    51   100.94
19  90    50   107.52
20  94    54    84.03
query = "SELECT * FROM pacientes"
# Procesa bloques de 25 registros a la vez
resultado_parcial = []
for chunk in pd.read_sql(query, db_engine1, chunksize=25):
    # Realiza transformaciones o cálculos por cada bloque
    resultado_parcial_tmp = chunk.groupby('estado_salud')['edad'].mean()
    resultado_parcial.append(resultado_parcial_tmp)
    print(f"Procesado bloque de {len(chunk)} filas.")

    
Procesado bloque de 25 filas.
Procesado bloque de 25 filas.
Procesado bloque de 25 filas.
Procesado bloque de 25 filas.
resultado_parcial
[estado_salud
Enfermo    51.625000
Sano       58.777778
Name: edad, dtype: float64, estado_salud
Enfermo    34.142857
Sano       57.222222
Name: edad, dtype: float64, estado_salud
Enfermo    49.125000
Sano       54.058824
Name: edad, dtype: float64, estado_salud
Enfermo    36.466667
Sano       59.700000
Name: edad, dtype: float64]
print(resultado_parcial)
[estado_salud
Enfermo    51.625000
Sano       58.777778
Name: edad, dtype: float64, estado_salud
Enfermo    34.142857
Sano       57.222222
Name: edad, dtype: float64, estado_salud
Enfermo    49.125000
Sano       54.058824
Name: edad, dtype: float64, estado_salud
Enfermo    36.466667
Sano       59.700000
Name: edad, dtype: float64]
