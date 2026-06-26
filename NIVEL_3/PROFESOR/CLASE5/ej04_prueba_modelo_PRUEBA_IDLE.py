# Hacer persistente el modelo
# Se va a guardar el modelo
import joblib
# Guardar el modelo en el disco
nombre_archivo = 'modelo_calidad_arroz.pkl'
joblib.dump(modelo, nombre_archivo)
['modelo_calidad_arroz.pkl']
print(f"Modelo guardado exitosamente como: {nombre_archivo}")
Modelo guardado exitosamente como: modelo_calidad_arroz.pkl

= RESTART: C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\NIVEL_3\PROFESOR\CLASE5\ej04_prueba_modelo.py
Traceback (most recent call last):
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\NIVEL_3\PROFESOR\CLASE5\ej04_prueba_modelo.py", line 16, in <module>
    prediccion = modelo_cargado.predict(nuevo_lote)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\ensemble\_forest.py", line 903, in predict
    proba = self.predict_proba(X)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\ensemble\_forest.py", line 945, in predict_proba
    X = self._validate_X_predict(X)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\ensemble\_forest.py", line 615, in _validate_X_predict
    X = validate_data(
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\utils\validation.py", line 3013, in validate_data
    _check_feature_names(_estimator, X, reset=reset)
  File "C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\.venv\Lib\site-packages\sklearn\utils\validation.py", line 2865, in _check_feature_names
    raise ValueError(message)
ValueError: The feature names should match those that were passed during fit.
Feature names unseen at fit time:
- CLASS


= RESTART: C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\NIVEL_3\PROFESOR\CLASE5\ej04_prueba_modelo.py
Resultado del Laboratorio: Lote clasificado como OTROS.

= RESTART: C:\Users\duque\Documents\Henry Duque\UNEWEB\PYTHON_CON_IA\NIVEL_3\PROFESOR\CLASE5\ej04_prueba_modelo.py
Resultado del Laboratorio: Lote clasificado como BASMATI (Premium).
