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
