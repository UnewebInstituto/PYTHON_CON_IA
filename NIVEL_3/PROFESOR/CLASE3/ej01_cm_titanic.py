import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
import joblib # Necesario para guardar el modelo

# 1. Carga y Preprocesamiento básico (Necesario para el Titanic)
df = pd.read_csv('titanic_train.csv')
# Limpieza rápida: manejar nulos y convertir variables categóricas
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

"""
Variables utilizadas en el dataset del Titanic:
* **Pclass**: Clase de pasajero (1ª, 2ª o 3ª clase).
* **Sex**: Sexo (Género del pasajero).
* **Age**: Edad.
* **SibSp**: Número de hermanos/cónyuges a bordo (*Sibling/Spouse*).
* **Parch**: Número de padres/hijos a bordo (*Parent/Children*).
* **Fare**: Tarifa (Precio del boleto).
"""

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = df[features]
y = df['Survived']

# 2. Configuración de la Validación Cruzada Estratificada
# Usamos 5 divisiones (folds)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
"""
Estas dos líneas de código son los cimientos de una evaluación robusta de tu modelo de aprendizaje automático. Aquí te detallo qué hace cada una:

1. skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
Esta instrucción configura la estrategia de Validación Cruzada Estratificada.

n_splits=5: Divide tus datos en 5 partes (o folds). En cada iteración, el modelo usará 4 partes para aprender y 1 parte para evaluarse a sí mismo. Esto se repite 5 veces hasta que todos los datos han servido como prueba al menos una vez.

Stratified (Estratificada): Es la parte más importante. Garantiza que la proporción de pasajeros que "Sobrevivieron" vs. "No Sobrevivieron" sea la misma en cada una de las 5 divisiones. Esto evita sesgos y asegura que el modelo vea ejemplos de ambas clases en cada iteración.

shuffle=True: Mezcla los datos de forma aleatoria antes de dividirlos. Esto es crucial para romper cualquier orden que el dataset pudiera traer (por ejemplo, si los datos estuvieran ordenados por fecha o apellido).

random_state=42: Fija una "semilla" para el generador de números aleatorios. Esto garantiza que cada vez que ejecutes el código, la división sea exactamente la misma, lo que permite que tus experimentos sean reproducibles.

2. modelo = RandomForestClassifier(n_estimators=100, random_state=42)
Esta instrucción crea la instancia del modelo que vas a entrenar.

RandomForestClassifier: Es un algoritmo de tipo "ensamble". En lugar de confiar en un solo árbol de decisión, crea un "bosque" de múltiples árboles y toma la decisión final combinando las respuestas de todos. Es muy potente porque corrige los errores que un solo árbol podría cometer.

n_estimators=100: Define que el "bosque" estará compuesto por 100 árboles de decisión individuales. A mayor número de árboles, mayor estabilidad, aunque aumenta el costo computacional.

random_state=42: Al igual que en la validación cruzada, esto asegura que el proceso interno de selección de muestras (para construir cada árbol) sea consistente. Si ejecutas el código mañana, los resultados serán idénticos.
"""

# 3. entrenamos el modelo con todo el dataset para luego guardarlo
modelo.fit(X, y) 

# 4. Guardado del modelo y columnas
# Guardamos el modelo para no tener que reentrenarlo
joblib.dump(modelo, 'modelo_titanic.pkl')
# Guardamos las columnas para asegurar que app.py reciba los datos en orden
joblib.dump(features, 'columnas_titanic.pkl')


# 5. Realizar predicciones usando validación cruzada
# cross_val_predict devuelve las predicciones de cada punto cuando le tocó ser test
y_pred = cross_val_predict(modelo, X, y, cv=skf)

# 6. Evaluación
# Matriz de Confusión
cm = confusion_matrix(y, y_pred)
print("Matriz de Confusión:\n", cm)

# 

# Reporte detallado (Precisión y Recall)
print("\nReporte de Clasificación:\n")
print(classification_report(y, y_pred))

# Visualización de la Matriz de Confusión
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=['No Sobrevió', 'Sobrevivió'], yticklabels=['No Sobrevió', 'Sobrevivió'])
plt.title("Matriz de Confusión - Titanic")
plt.ylabel("Real")
plt.xlabel("Predicho")
plt.show()
