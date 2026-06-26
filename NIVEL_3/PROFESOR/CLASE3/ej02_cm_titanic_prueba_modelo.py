import joblib
import pandas as pd

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

prediccion = modelo.predict(nuevo_pasajero2)
print(f"Resultado: {'Sobrevivió' if prediccion[0] == 1 else 'No Sobrevivió'}")