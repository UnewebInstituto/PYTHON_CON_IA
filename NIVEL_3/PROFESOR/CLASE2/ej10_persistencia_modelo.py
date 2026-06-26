import joblib
import pandas as pd

# 1. Cargar el modelo guardado
modelo_cargado = joblib.load('modelo_rentabilidad.pkl')

# 2. Supongamos que recibes nuevos datos de una venta (deben tener las mismas columnas que X_train)
# Ejemplo: Nueva venta con [Sales, Quantity, Discount, Profit_Scaled]
nueva_venta = pd.DataFrame([[500, 2, 0.1, 80]], columns=['Sales', 'Quantity', 'Discount', 'Profit_Scaled'])

# 3. Predecir
prediccion = modelo_cargado.predict(nueva_venta)

if prediccion[0] == 1:
    print("El modelo predice que esta orden será RENTABLE.")
else:
    print("El modelo predice que esta orden será NO RENTABLE.")
