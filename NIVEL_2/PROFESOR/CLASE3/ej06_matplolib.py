Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
# 1. Creamos datos de ejemplo (X = peso/estatura, y = categoria)
# 20 personas, 2 caracteristicas cada una
X = np.random.rand(20, 2) * 100
y = np.random.choice([0, 1], size=20)
X
array([[71.19324573,  7.70290884],
       [55.80993361, 66.7064115 ],
       [34.69624824, 20.7123791 ],
       [45.44468811, 84.54677684],
       [64.99303839, 73.65690742],
       [29.00716055, 67.44830432],
       [85.5981237 , 43.52983036],
       [14.6968446 , 28.25578775],
       [ 7.69617025, 44.17615035],
       [48.57810381, 65.98131141],
       [80.05849425, 81.87932976],
       [77.12896849, 82.09932587],
       [74.37962701, 94.39271726],
       [25.73718161, 35.26523929],
       [55.96264682, 84.00447294],
       [17.46966833, 45.30723507],
       [76.958365  , 35.00581289],
       [49.62839507,  5.60251302],
       [15.74177333, 56.4384474 ],
       [35.1517367 , 43.45167479]])
y
array([1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1])
# 2. Dividimos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 3. Normalizamos los datos para que tengan la misma escala
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# 4. Elegimos el modelo (k-NN en este caso)

modelo = KNeighborsClassifier(n_neighbors=3)
# 5. Entrenamos
modelo.fit(X_train, y_train)
KNeighborsClassifier(n_neighbors=3)
# 6. Predecimos y evaluamos
predicciones = modelo.predict(X_test)
print(f"Precisión del modelo: {accuracy_score(y_test, predicciones) * 100}%")
Precisión del modelo: 50.0%
# USO DE LA LIBRERÍAS O DEPENDENCIAS matplotlib O seaborn
import seaborn as sns
import matplotlib.pyplot as plt
# Datos de ejemplo
edades = [22, 25, 25, 30, 35, 40, 45, 50, 50, 50, 60]
edades
[22, 25, 25, 30, 35, 40, 45, 50, 50, 50, 60]
# Gráfico con Seaborn
sns.histplot(edades, kde=True, color='skyblue')
<Axes: ylabel='Count'>
plt.title("Distribución de Edades")
Text(0.5, 1.0, 'Distribución de Edades')
plt.xlabel("Edad")
Text(0.5, 0, 'Edad')
plt.ylabel("Frecuencia")
Text(0, 0.5, 'Frecuencia')
plt.show() # Simpre para mostrar el gráfico resultado.
# 2do. Ejemplo matplotlib y seaborn
import pandas as pd
# Creamos un dataset
df = pd.DataFrame({'Edad': [20, 30, 40], 'Presion': [120, 130, 140], 'Glucosa': [80, 90, 110]})
df
   Edad  Presion  Glucosa
0    20      120       80
1    30      130       90
2    40      140      110
# Matriz de correlación
correlacion = df.corr()
correlacion
             Edad   Presion   Glucosa
Edad     1.000000  1.000000  0.981981
Presion  1.000000  1.000000  0.981981
Glucosa  0.981981  0.981981  1.000000
# Heatmap (Mapa de calor)
sns.heatmap(correlacion, annot=True, cmap='coolwarm')
<Axes: >
plt.title("Mapa de Calor de Correlaciones")
Text(0.5, 1.0, 'Mapa de Calor de Correlaciones')
plt.show()
plt.show()
# 3er. Ejemplo matplotlib y seaborn
df
   Edad  Presion  Glucosa
0    20      120       80
1    30      130       90
2    40      140      110
sns.scatterplot(data=df, x='Glucosa', y='Presion', hue='Edad', size='Edad')
<Axes: xlabel='Glucosa', ylabel='Presion'>
plt.title("Relación Glucosa vs Presión por Edad")
Text(0.5, 1.0, 'Relación Glucosa vs Presión por Edad')
plt.show()
plt.show()
df
   Edad  Presion  Glucosa
0    20      120       80
1    30      130       90
2    40      140      110
sns.scatterplot(data=df, x='Glucosa', y='Presion', hue='Edad', size='Edad')
<Axes: xlabel='Glucosa', ylabel='Presion'>
plt.title("Relación Glucosa vs Presión por Edad")
Text(0.5, 1.0, 'Relación Glucosa vs Presión por Edad')
plt.show()
# 4to. Ejemplo
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 1. Creamos un dataset simulado más rico
np.random.seed(42)
df = pd.DataFrame({
    'Glucosa': np.random.normal(100, 15, 100),
    'Presion': np.random.normal(120, 10, 100),
    'Edad': np.random.randint(20, 70, 100),
    'Estado': np.random.choice(['Sano', 'Enfermo'], 100)
})
df
       Glucosa     Presion  Edad   Estado
0   107.450712  105.846293    21  Enfermo
1    97.926035  115.793547    45  Enfermo
2   109.715328  116.572855    36  Enfermo
3   122.845448  111.977227    59  Enfermo
4    96.487699  118.387143    52     Sano
..         ...         ...   ...      ...
95   78.047276  123.853174    33     Sano
96  104.441804  111.161426    47  Enfermo
97  103.915829  121.537251    24  Enfermo
98  100.076702  120.582087    66     Sano
99   96.481193  108.570297    68     Sano

[100 rows x 4 columns]
# 2. Generamos el pairplot
# 'hue' permite diferenciar visualmente por categoría
sns.pairplot(df, hue='Estado', palette='viridis', diag_kind='kde')
<seaborn.axisgrid.PairGrid object at 0x0000025BE9CD5B50>
plt.suptitle("Análisis de Relaciones: Pairplot del Dataset", y=1.02)
Text(0.5, 1.02, 'Análisis de Relaciones: Pairplot del Dataset')
plt.show()
df
       Glucosa     Presion  Edad   Estado
0   107.450712  105.846293    21  Enfermo
1    97.926035  115.793547    45  Enfermo
2   109.715328  116.572855    36  Enfermo
3   122.845448  111.977227    59  Enfermo
4    96.487699  118.387143    52     Sano
..         ...         ...   ...      ...
95   78.047276  123.853174    33     Sano
96  104.441804  111.161426    47  Enfermo
97  103.915829  121.537251    24  Enfermo
98  100.076702  120.582087    66     Sano
99   96.481193  108.570297    68     Sano

[100 rows x 4 columns]
sns.pairplot(df, hue='Estado', palette='viridis', diag_kind='kde')
<seaborn.axisgrid.PairGrid object at 0x0000025BEA2D4890>
plt.suptitle("Análisis de Relaciones: Pairplot del Dataset", y=1.02)
Text(0.5, 1.02, 'Análisis de Relaciones: Pairplot del Dataset')
plt.show()
# Ejemplos de Matplotlib
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
[<matplotlib.lines.Line2D object at 0x0000025BF53CB0E0>]
plt.show()
# Ej02 Matplotlib
fig = plt.figure()             # an empty figure with no Axes
fig, ax = plt.subplots()       # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
plt.show()
b = np.matrix([[1, 2], [3, 4]])
b
matrix([[1, 2],
        [3, 4]])
b_asarray = np.asarray(b)
b_asarray
array([[1, 2],
       [3, 4]])
# Ej03 Matplotlib
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data
{'a': array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 'c': array([20, 44, 20, 45,  6, 34, 34, 23,  3, 49, 36, 42, 18, 11,  8, 37, 11,
        3,  5, 48,  9,  3, 33, 32, 31,  0, 26, 37,  0, 17, 23, 25, 24,  6,
       23, 19, 34, 10, 42, 11, 47,  9, 39,  3, 24, 38, 42, 10, 35, 47],
      dtype=int32), 'd': array([ 1.31086051, -0.51744207, -0.01665814,  0.46917225,  0.77677809,
       -1.88469769, -0.12758733, -0.51931744,  0.73514322,  1.34685132,
        0.55025505, -0.22905116,  0.66123163, -0.53636847, -0.48194438,
        0.31272356, -3.12183853, -1.35847701, -0.14263821, -0.21699693,
       -0.032868  ,  1.83214468,  0.35235984,  0.23664513,  1.47854807,
        1.55430657, -1.11060898,  0.82378856,  0.66527469,  0.71476639,
       -1.23078705,  2.09540213, -0.60321948,  1.61355306, -0.25398405,
       -1.51587877, -0.11722652,  0.49542836, -0.70259085,  0.39506954,
       -1.12327902, -1.71555479, -0.27110515,  0.08624074, -1.09047119,
        0.11254301, -0.95364447,  0.05022319, -0.4831606 ,  1.3339033 ])}


fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    ax.scatter('a', 'b', c='c', s='d', data=data)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\matplotlib\_api\deprecation.py", line 453, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\matplotlib\__init__.py", line 1553, in inner
    return func(*new_args, **new_kwargs)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\matplotlib\axes\_axes.py", line 4936, in scatter
    raise ValueError("x and y must be the same size")
ValueError: x and y must be the same size
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
data['b']
array([  4.8018808 ,  -6.4972666 , -11.2077656 ,   6.322316  ,
         1.33391659,  11.36202025,  -5.18315173,   9.64545151,
         8.93059413,  -2.9619809 ,   1.010722  ,  10.5460328 ,
         6.02832418,  13.15619153,   7.92816087,  22.2140083 ,
        20.64277678,  25.26559419,  18.93012033,  -3.62283088,
        29.90723646,   8.2618424 ,   8.1226306 ,  24.55220778,
        24.73672481,  35.29148044,  19.39618445,  20.81129384,
        26.1046295 ,  23.53964929,  46.2580496 ,  29.97454235,
        17.69996036,  41.7538301 ,  32.48260765,  31.30030868,
        36.13983623,  36.18332016,  48.92477345,  44.27782523,
        57.41677485,  35.53675523,  58.57367953,  49.73629965,
        43.15151999,  28.47595654,  52.43563731,  37.8567097 ,
        51.49878342,  49.98087623])
data['d']
array([131.08605149,  51.74420745,   1.66581368,  46.91722512,
        77.67780947, 188.46976928,  12.75873335,  51.9317436 ,
        73.51432203, 134.68513218,  55.02550534,  22.90511577,
        66.12316262,  53.63684671,  48.19443761,  31.27235627,
       312.18385278, 135.84770113,  14.26382069,  21.69969255,
         3.28680039, 183.21446831,  35.23598407,  23.66451326,
       147.85480652, 155.43065697, 111.06089767,  82.37885628,
        66.52746882,  71.47663897, 123.0787053 , 209.54021272,
        60.32194818, 161.35530599,  25.39840502, 151.58787722,
        11.72265226,  49.54283589,  70.25908475,  39.50695356,
       112.32790207, 171.55547852,  27.11051464,   8.62407388,
       109.04711851,  11.25430131,  95.36444665,   5.02231944,
        48.31606025, 133.39032998])

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
<matplotlib.collections.PathCollection object at 0x0000025BF5407080>
ax.set_xlabel('entry a')
Text(0.5, 0, 'entry a')
ax.set_ylabel('entry b')
Text(0, 0.5, 'entry b')
plt.show()
# Ej04 Matplotlib
x = np.linspace(0, 2, 100)  # Sample data.
x
array([0.        , 0.02020202, 0.04040404, 0.06060606, 0.08080808,
       0.1010101 , 0.12121212, 0.14141414, 0.16161616, 0.18181818,
       0.2020202 , 0.22222222, 0.24242424, 0.26262626, 0.28282828,
       0.3030303 , 0.32323232, 0.34343434, 0.36363636, 0.38383838,
       0.4040404 , 0.42424242, 0.44444444, 0.46464646, 0.48484848,
       0.50505051, 0.52525253, 0.54545455, 0.56565657, 0.58585859,
       0.60606061, 0.62626263, 0.64646465, 0.66666667, 0.68686869,
       0.70707071, 0.72727273, 0.74747475, 0.76767677, 0.78787879,
       0.80808081, 0.82828283, 0.84848485, 0.86868687, 0.88888889,
       0.90909091, 0.92929293, 0.94949495, 0.96969697, 0.98989899,
       1.01010101, 1.03030303, 1.05050505, 1.07070707, 1.09090909,
       1.11111111, 1.13131313, 1.15151515, 1.17171717, 1.19191919,
       1.21212121, 1.23232323, 1.25252525, 1.27272727, 1.29292929,
       1.31313131, 1.33333333, 1.35353535, 1.37373737, 1.39393939,
       1.41414141, 1.43434343, 1.45454545, 1.47474747, 1.49494949,
       1.51515152, 1.53535354, 1.55555556, 1.57575758, 1.5959596 ,
       1.61616162, 1.63636364, 1.65656566, 1.67676768, 1.6969697 ,
       1.71717172, 1.73737374, 1.75757576, 1.77777778, 1.7979798 ,
       1.81818182, 1.83838384, 1.85858586, 1.87878788, 1.8989899 ,
       1.91919192, 1.93939394, 1.95959596, 1.97979798, 2.        ])
# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the Axes.
[<matplotlib.lines.Line2D object at 0x0000025BF5138590>]
ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
[<matplotlib.lines.Line2D object at 0x0000025BFD4254C0>]
ax.plot(x, x**3, label='cubic')  # ... and some more.
[<matplotlib.lines.Line2D object at 0x0000025BFD4279E0>]
ax.set_xlabel('x label')  # Add an x-label to the Axes.
Text(0.5, 0, 'x label')
ax.set_ylabel('y label')  # Add a y-label to the Axes.
Text(0, 0.5, 'y label')
ax.set_title("Simple Plot")  # Add a title to the Axes.
Text(0.5, 1.0, 'Simple Plot')
ax.legend()  # Add a legend.
<matplotlib.legend.Legend object at 0x0000025BF6FCB7A0>
plt.show()
# Ej05 Matplotlib
x
array([0.        , 0.02020202, 0.04040404, 0.06060606, 0.08080808,
       0.1010101 , 0.12121212, 0.14141414, 0.16161616, 0.18181818,
       0.2020202 , 0.22222222, 0.24242424, 0.26262626, 0.28282828,
       0.3030303 , 0.32323232, 0.34343434, 0.36363636, 0.38383838,
       0.4040404 , 0.42424242, 0.44444444, 0.46464646, 0.48484848,
       0.50505051, 0.52525253, 0.54545455, 0.56565657, 0.58585859,
       0.60606061, 0.62626263, 0.64646465, 0.66666667, 0.68686869,
       0.70707071, 0.72727273, 0.74747475, 0.76767677, 0.78787879,
       0.80808081, 0.82828283, 0.84848485, 0.86868687, 0.88888889,
       0.90909091, 0.92929293, 0.94949495, 0.96969697, 0.98989899,
       1.01010101, 1.03030303, 1.05050505, 1.07070707, 1.09090909,
       1.11111111, 1.13131313, 1.15151515, 1.17171717, 1.19191919,
       1.21212121, 1.23232323, 1.25252525, 1.27272727, 1.29292929,
       1.31313131, 1.33333333, 1.35353535, 1.37373737, 1.39393939,
       1.41414141, 1.43434343, 1.45454545, 1.47474747, 1.49494949,
       1.51515152, 1.53535354, 1.55555556, 1.57575758, 1.5959596 ,
       1.61616162, 1.63636364, 1.65656566, 1.67676768, 1.6969697 ,
       1.71717172, 1.73737374, 1.75757576, 1.77777778, 1.7979798 ,
       1.81818182, 1.83838384, 1.85858586, 1.87878788, 1.8989899 ,
       1.91919192, 1.93939394, 1.95959596, 1.97979798, 2.        ])
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
plt.figure(figsize=(5, 2.7), layout='constrained')
<Figure size 500x270 with 0 Axes>
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
[<matplotlib.lines.Line2D object at 0x0000025BF708A750>]
plt.plot(x, x**2, label='quadratic')  # etc.
[<matplotlib.lines.Line2D object at 0x0000025BF70898E0>]
plt.plot(x, x**3, label='cubic')

[<matplotlib.lines.Line2D object at 0x0000025BF708A4E0>]
plt.xlabel('x label')
Text(0.5, 0, 'x label')
plt.ylabel('y label')
Text(0, 0.5, 'y label')
plt.title("Simple Plot")
Text(0.5, 1.0, 'Simple Plot')
plt.legend()
<matplotlib.legend.Legend object at 0x0000025BF7044D70>
plt.show()
# Ej06 Matplotlib
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
data1
array([ 9.20133074e-01,  4.16248081e-01,  6.88298652e-01, -3.27091982e-02,
        5.42544505e-01, -5.88782966e-03, -1.36174511e+00, -3.17451269e-01,
       -2.32676449e+00,  8.79554336e-01, -6.85958787e-01, -1.19423245e+00,
       -1.22019276e+00, -8.51083359e-01,  6.73740039e-01,  6.35835705e-01,
        8.35274905e-01,  1.81992918e-01,  1.23229074e+00, -9.96841814e-01,
       -8.04237843e-01,  1.83322987e+00,  8.40462099e-02, -4.66226311e-01,
       -4.58791439e-01, -6.23694657e-01,  6.45132873e-01, -1.85158063e+00,
        8.43342331e-01,  1.09386676e+00,  4.56575777e-01,  2.73130831e-01,
       -1.91682051e+00,  1.62999085e-01,  9.20437057e-01, -6.67275456e-01,
       -4.66619092e-02, -6.13770999e-01, -3.74933938e-01,  5.16940818e-01,
        5.38914484e-01,  1.52495903e-03, -1.07786263e-01,  6.90346916e-01,
        1.48077994e+00,  9.05456081e-01,  1.63013950e+00,  5.30195841e-02,
       -1.67786677e+00, -3.06046411e-01, -1.61530935e-01,  1.12748366e+00,
       -2.78086673e-02,  2.90107302e-02, -8.38883358e-01, -9.97609243e-01,
        1.96853367e-01, -1.56702295e+00,  7.68129015e-02,  2.29493807e-01,
        1.16447260e+00,  1.35605750e-02, -1.13170017e+00, -6.98519887e-01,
       -1.28332743e+00, -1.03435213e+00,  8.58721686e-01, -1.12860543e+00,
        4.25096719e-01,  1.01614134e+00, -3.13862515e+00, -4.92030627e-01,
        1.61015246e+00,  4.73977616e-01, -2.31153107e+00, -4.53181151e-01,
       -8.31669424e-01, -2.63129533e-01, -2.53374464e-01,  1.04640986e-01,
       -3.38437494e-01, -1.14802757e+00, -5.27721883e-01, -1.20810654e-01,
        1.74285870e-01, -6.38896397e-01, -8.50784286e-02,  1.62689650e+00,
        7.29508205e-01,  3.87368364e-01,  1.36074597e-01,  1.58593446e-01,
       -8.73646159e-02, -7.31171220e-01,  1.24671148e+00,  7.12343049e-01,
       -1.17256327e+00,  4.38951572e-01, -5.25698140e-01,  4.52146820e-01])


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
[<matplotlib.lines.Line2D object at 0x0000025BF7028A40>]
plt.show()
my_plotter(ax2, data3, data4, {'marker': 'o'})
[<matplotlib.lines.Line2D object at 0x0000025BFBDDFCE0>]
plt.show()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
[<matplotlib.lines.Line2D object at 0x0000025BF53D4920>]
my_plotter(ax2, data3, data4, {'marker': 'o'})
[<matplotlib.lines.Line2D object at 0x0000025BF53D7500>]
plt.show()
# Ej07 Matplotlib
fig, ax = plt.subplots(figsize=(5, 2.7))
data1
array([ 9.20133074e-01,  4.16248081e-01,  6.88298652e-01, -3.27091982e-02,
        5.42544505e-01, -5.88782966e-03, -1.36174511e+00, -3.17451269e-01,
       -2.32676449e+00,  8.79554336e-01, -6.85958787e-01, -1.19423245e+00,
       -1.22019276e+00, -8.51083359e-01,  6.73740039e-01,  6.35835705e-01,
        8.35274905e-01,  1.81992918e-01,  1.23229074e+00, -9.96841814e-01,
       -8.04237843e-01,  1.83322987e+00,  8.40462099e-02, -4.66226311e-01,
       -4.58791439e-01, -6.23694657e-01,  6.45132873e-01, -1.85158063e+00,
        8.43342331e-01,  1.09386676e+00,  4.56575777e-01,  2.73130831e-01,
       -1.91682051e+00,  1.62999085e-01,  9.20437057e-01, -6.67275456e-01,
       -4.66619092e-02, -6.13770999e-01, -3.74933938e-01,  5.16940818e-01,
        5.38914484e-01,  1.52495903e-03, -1.07786263e-01,  6.90346916e-01,
        1.48077994e+00,  9.05456081e-01,  1.63013950e+00,  5.30195841e-02,
       -1.67786677e+00, -3.06046411e-01, -1.61530935e-01,  1.12748366e+00,
       -2.78086673e-02,  2.90107302e-02, -8.38883358e-01, -9.97609243e-01,
        1.96853367e-01, -1.56702295e+00,  7.68129015e-02,  2.29493807e-01,
        1.16447260e+00,  1.35605750e-02, -1.13170017e+00, -6.98519887e-01,
       -1.28332743e+00, -1.03435213e+00,  8.58721686e-01, -1.12860543e+00,
        4.25096719e-01,  1.01614134e+00, -3.13862515e+00, -4.92030627e-01,
        1.61015246e+00,  4.73977616e-01, -2.31153107e+00, -4.53181151e-01,
       -8.31669424e-01, -2.63129533e-01, -2.53374464e-01,  1.04640986e-01,
       -3.38437494e-01, -1.14802757e+00, -5.27721883e-01, -1.20810654e-01,
        1.74285870e-01, -6.38896397e-01, -8.50784286e-02,  1.62689650e+00,
        7.29508205e-01,  3.87368364e-01,  1.36074597e-01,  1.58593446e-01,
       -8.73646159e-02, -7.31171220e-01,  1.24671148e+00,  7.12343049e-01,
       -1.17256327e+00,  4.38951572e-01, -5.25698140e-01,  4.52146820e-01])


x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
[<matplotlib.lines.Line2D object at 0x0000025BF420EBD0>]
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
[<matplotlib.lines.Line2D object at 0x0000025BF420FD40>]
l.set_linestyle(':')
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    l.set_linestyle(':')
NameError: name 'l' is not defined
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
plt.show()
# Ej08 Matplotlib
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
<matplotlib.collections.PathCollection object at 0x0000025BE9E00A10>
plt.show()
# Ej09 Matplotlib
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
[<matplotlib.lines.Line2D object at 0x0000025BF74FDB80>]
ax.plot(data2, 'd', label='data2')
[<matplotlib.lines.Line2D object at 0x0000025BF74FD490>]
ax.plot(data3, 'v', label='data3')
[<matplotlib.lines.Line2D object at 0x0000025BF74FECF0>]
ax.plot(data4, 's', label='data4')
[<matplotlib.lines.Line2D object at 0x0000025BE9E02BD0>]
ax.legend()
<matplotlib.legend.Legend object at 0x0000025BF744ECC0>
plt.show()
# Ej10 Matplotlib
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
x
array([125.43814618, 130.81596451, 137.160627  , ...,  97.32782399,
       112.09877291, 100.48670236], shape=(10000,))
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)
ax.set_xlabel('Length [cm]')
Text(0.5, 0, 'Length [cm]')
ax.set_ylabel('Probability')
Text(0, 0.5, 'Probability')
ax.set_title('Aardvark lengths\n (not really)')
Text(0.5, 1.0, 'Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
Text(75, 0.025, '$\\mu=115,\\ \\sigma=15$')
ax.axis([55, 175, 0, 0.03])
(np.float64(55.0), np.float64(175.0), np.float64(0.0), np.float64(0.03))
ax.grid(True)
plt.show()
# Ej11 Matplotlib
fig, ax = plt.subplots(figsize=(5, 2.7))
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
Text(3, 1.5, 'local max')
ax.set_ylim(-2, 2)
(-2.0, 2.0)
plt.show()
# Ej12 Matplotlib
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(np.arange(len(data1)), data1, label='data1')
[<matplotlib.lines.Line2D object at 0x0000025BF45D4E00>]
ax.plot(np.arange(len(data2)), data2, label='data2')
[<matplotlib.lines.Line2D object at 0x0000025BF45D7200>]
ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
[<matplotlib.lines.Line2D object at 0x0000025BF45D7530>]
ax.legend()
<matplotlib.legend.Legend object at 0x0000025BE9F363C0>
plt.show()
# Ej13 Matplotlib
fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(len(data1))  # make an ordinal for this
data
{'a': array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), 'c': array([20, 44, 20, 45,  6, 34, 34, 23,  3, 49, 36, 42, 18, 11,  8, 37, 11,
        3,  5, 48,  9,  3, 33, 32, 31,  0, 26, 37,  0, 17, 23, 25, 24,  6,
       23, 19, 34, 10, 42, 11, 47,  9, 39,  3, 24, 38, 42, 10, 35, 47],
      dtype=int32), 'd': array([131.08605149,  51.74420745,   1.66581368,  46.91722512,
        77.67780947, 188.46976928,  12.75873335,  51.9317436 ,
        73.51432203, 134.68513218,  55.02550534,  22.90511577,
        66.12316262,  53.63684671,  48.19443761,  31.27235627,
       312.18385278, 135.84770113,  14.26382069,  21.69969255,
         3.28680039, 183.21446831,  35.23598407,  23.66451326,
       147.85480652, 155.43065697, 111.06089767,  82.37885628,
        66.52746882,  71.47663897, 123.0787053 , 209.54021272,
        60.32194818, 161.35530599,  25.39840502, 151.58787722,
        11.72265226,  49.54283589,  70.25908475,  39.50695356,
       112.32790207, 171.55547852,  27.11051464,   8.62407388,
       109.04711851,  11.25430131,  95.36444665,   5.02231944,
        48.31606025, 133.39032998]), 'b': array([  4.8018808 ,  -6.4972666 , -11.2077656 ,   6.322316  ,
         1.33391659,  11.36202025,  -5.18315173,   9.64545151,
         8.93059413,  -2.9619809 ,   1.010722  ,  10.5460328 ,
         6.02832418,  13.15619153,   7.92816087,  22.2140083 ,
        20.64277678,  25.26559419,  18.93012033,  -3.62283088,
        29.90723646,   8.2618424 ,   8.1226306 ,  24.55220778,
        24.73672481,  35.29148044,  19.39618445,  20.81129384,
        26.1046295 ,  23.53964929,  46.2580496 ,  29.97454235,
        17.69996036,  41.7538301 ,  32.48260765,  31.30030868,
        36.13983623,  36.18332016,  48.92477345,  44.27782523,
        57.41677485,  35.53675523,  58.57367953,  49.73629965,
        43.15151999,  28.47595654,  52.43563731,  37.8567097 ,
        51.49878342,  49.98087623])}
data = 10**data1
data
array([8.32018674e+00, 2.60764268e+00, 4.87863865e+00, 9.27450633e-01,
       3.48774324e+00, 9.86534257e-01, 4.34765317e-02, 4.81447273e-01,
       4.71232801e-03, 7.57799539e+00, 2.06082547e-01, 6.39392525e-02,
       6.02292197e-02, 1.40901832e-01, 4.71780557e+00, 4.32350240e+00,
       6.84344695e+00, 1.52052274e+00, 1.70722492e+01, 1.00729850e-01,
       1.56950302e-01, 6.81129775e+01, 1.21351796e+00, 3.41801284e-01,
       3.47703099e-01, 2.37851198e-01, 4.41705567e+00, 1.40740591e-02,
       6.97175844e+00, 1.24127143e+01, 2.86138158e+00, 1.87555943e+00,
       1.21109858e-02, 1.45545601e+00, 8.32601247e+00, 2.15141674e-01,
       8.98127699e-01, 2.43348683e-01, 4.21760654e-01, 3.28806821e+00,
       3.45871266e+00, 1.00351752e+00, 7.80213997e-01, 4.90170212e+00,
       3.02538007e+01, 8.04370400e+00, 4.26716566e+01, 1.12984686e+00,
       2.09958386e-02, 4.94257865e-01, 6.89396486e-01, 1.34116947e+01,
       9.37975150e-01, 1.06908129e+00, 1.44916101e-01, 1.00552010e-01,
       1.57345152e+00, 2.71004841e-02, 1.19347383e+00, 1.69626541e+00,
       1.46040261e+01, 1.03171697e+00, 7.38413844e-02, 2.00207394e-01,
       5.20801908e-02, 9.23948718e-02, 7.22306771e+00, 7.43694505e-02,
       2.66131768e+00, 1.03786613e+01, 7.26732941e-04, 3.22084165e-01,
       4.07523316e+01, 2.97836292e+00, 4.88055187e-03, 3.52223922e-01,
       1.47343362e-01, 5.45595108e-01, 5.57988870e-01, 1.27245076e+00,
       4.58735665e-01, 7.11168367e-02, 2.96673064e-01, 7.57162935e-01,
       1.49377735e+00, 2.29669647e-01, 8.22094176e-01, 4.23542017e+01,
       5.36424006e+00, 2.43987942e+00, 1.36796377e+00, 1.44076598e+00,
       8.17777927e-01, 1.85707216e-01, 1.76486495e+01, 5.15635784e+00,
       6.72104383e-02, 2.74758775e+00, 2.98058739e-01, 2.83234936e+00])
axs[0].plot(xdata, data)
[<matplotlib.lines.Line2D object at 0x0000025BE9ED19D0>]
axs[1].set_yscale('log')
axs[1].plot(xdata, data)
[<matplotlib.lines.Line2D object at 0x0000025BE9ED0EC0>]
plt.show()
# Ej14 Localizadores y formateadores de marcas
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(xdata, data1)
[<matplotlib.lines.Line2D object at 0x0000025BF702B0E0>]
axs[0].set_title('Automatic ticks')
Text(0.5, 1.0, 'Automatic ticks')
axs[1].plot(xdata, data1)
[<matplotlib.lines.Line2D object at 0x0000025BF702BD70>]
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
[<matplotlib.axis.XTick object at 0x0000025BF7046AB0>, <matplotlib.axis.XTick object at 0x0000025BF706F260>, <matplotlib.axis.XTick object at 0x0000025BFBDDDA00>, <matplotlib.axis.XTick object at 0x0000025BF702A990>]
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
[<matplotlib.axis.YTick object at 0x0000025BF7045A90>, <matplotlib.axis.YTick object at 0x0000025BF706C6E0>, <matplotlib.axis.YTick object at 0x0000025BF7062D50>]
axs[1].set_title('Manual ticks')
Text(0.5, 1.0, 'Manual ticks')
plt.show()
# Ej15 Representación gráfica de fechas y cadenas
KeyboardInterrupt
from matplotlib.dates import ConciseDateFormatter
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                  np.timedelta64(1, 'h'))
data = np.cumsum(np.random.randn(len(dates)))
ax.plot(dates, data)
[<matplotlib.lines.Line2D object at 0x0000025BF579D850>]
ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))
plt.show()
# Ej16 Representación gráfica de fechas y cadenas (CATEGORÍAS)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
ax.bar(categories, np.random.rand(len(categories)))
<BarContainer object of 4 artists>
plt.show()
# Ej17 Objetos de eje adicionales
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
l1, = ax1.plot(t, s)
ax2 = ax1.twinx()
l2, = ax2.plot(t, range(len(t)), 'C1')
ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])
<matplotlib.legend.Legend object at 0x0000025BF57C1EE0>
ax3.plot(t, s)
[<matplotlib.lines.Line2D object at 0x0000025BF417B590>]
ax3.set_xlabel('Angle [rad]')
Text(0.5, 0, 'Angle [rad]')
ax4 = ax3.secondary_xaxis('top', (np.rad2deg, np.deg2rad))
ax4.set_xlabel('Angle [°]')
Text(0.5, 0, 'Angle [°]')
plt.show()
# Ej18 Datos con mapa de colores
from matplotlib.colors import LogNorm
X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)
fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
<matplotlib.colorbar.Colorbar object at 0x0000025BFBE47890>
axs[0, 0].set_title('pcolormesh()')
Text(0.5, 1.0, 'pcolormesh()')
co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
<matplotlib.colorbar.Colorbar object at 0x0000025BFBE9D8E0>
axs[0, 1].set_title('contourf()')
Text(0.5, 1.0, 'contourf()')
pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma', norm=LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
<matplotlib.colorbar.Colorbar object at 0x0000025BFBE9D220>
axs[1, 0].set_title('imshow() with LogNorm()')
Text(0.5, 1.0, 'imshow() with LogNorm()')
pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
<matplotlib.colorbar.Colorbar object at 0x0000025BFD3F46B0>
axs[1, 1].set_title('scatter()')
Text(0.5, 1.0, 'scatter()')
plt.show()
