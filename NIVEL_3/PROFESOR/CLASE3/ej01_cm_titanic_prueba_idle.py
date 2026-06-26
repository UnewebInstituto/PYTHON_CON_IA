Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Ejemplo de clasificación basado en el dataset del Titanic
# Carga de dependencias
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
#1. Carga y Preprocesamiento básico (Necesario para el Titanic)
df = pd.read_csv('./NIVEL_3/PROFESOR/CLASE3/titanic_train.csv')
df
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
# Limpieza rápida: manejar nulos y convertir variables categóricas
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = df[features]
y = df['Survived']
# Usamos 5 divisiones (folds)

# 2. Configuración de la Validación Cruzada Estratificada
# Usamos 5 divisiones (folds)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
# 3. Realizar predicciones usando validación cruzada
# cross_val_predict devuelve las predicciones de cada punto cuando le tocó ser test
y_pred = cross_val_predict(modelo, X, y, cv=skf)
# 4. Evaluación
# Matriz de Confusión
cm = confusion_matrix(y, y_pred)
print("Matriz de Confusión:\n", cm)
Matriz de Confusión:
 [[477  72]
 [ 86 256]]
# Reporte detallado (Precisión y Recall)
print("\nReporte de Clasificación:\n")

Reporte de Clasificación:

print(classification_report(y, y_pred))
              precision    recall  f1-score   support

           0       0.85      0.87      0.86       549
           1       0.78      0.75      0.76       342

    accuracy                           0.82       891
   macro avg       0.81      0.81      0.81       891
weighted avg       0.82      0.82      0.82       891

# Visualización de la Matriz de Confusión
plt.figure(figsize=(6, 4))
<Figure size 600x400 with 0 Axes>
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', xticklabels=['No Sobrevió', 'Sobrevivió'], yticklabels=['No Sobrevió', 'Sobrevivió'])
<Axes: >
plt.title("Matriz de Confusión - Titanic")
Text(0.5, 1.0, 'Matriz de Confusión - Titanic')
plt.ylabel("Real")
Text(45.72222222222221, 0.5, 'Real')
plt.xlabel("Predicho")
Text(0.5, 14.722222222222216, 'Predicho')
plt.show()
# Guargar el modelo para una prueba posterior
import joblib
import pandas as pd
modelo.fit(X, y)
RandomForestClassifier(random_state=42)
# 4. Guardado del modelo y columnas
# Guardamos el modelo para no tener que reentrenarlo
joblib.dump(modelo, 'modelo_titanic.pkl')
['modelo_titanic.pkl']
# Guardamos las columnas para asegurar que app.py reciba los datos en orden
joblib.dump(features, 'columnas_titanic.pkl')
['columnas_titanic.pkl']
# Cargar el modelo ya entrenado (asegúrate de que el archivo exista)
modelo = joblib.load('modelo_titanic.pkl')
# Crear el DataFrame con los nombres de columnas exactos
nuevo_pasajero1 = pd.DataFrame([[3, 0, 22.0, 1, 0, 7.2500]], 
                              columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])
nuevo_pasajero2 = pd.DataFrame([[1,1,38.0,1,0,71.2833]], 
                              columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])

# Ahora sí puedes predecir
prediccion = modelo.predict(nuevo_pasajero1)
print(f"Resultado: {'Sobrevivió' if prediccion[0] == 1 else 'No Sobrevivió'}")
Resultado: No Sobrevivió

prediccion = modelo.predict(nuevo_pasajero2)
print(f"Resultado: {'Sobrevivió' if prediccion[0] == 1 else 'No Sobrevivió'}")
Resultado: Sobrevivió
