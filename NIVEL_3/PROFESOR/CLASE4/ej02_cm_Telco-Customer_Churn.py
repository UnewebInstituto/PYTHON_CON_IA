import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carga y Limpieza Robusta
df = pd.read_csv('./WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Conversión segura para evitar errores de asignación
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
df = df.drop('customerID', axis=1)

# 2. Codificación (Preparación para el Modelo)
# Convertimos todas las variables categóricas de una forma más limpia
# Esto soluciona el ValueError al convertir automáticamente todo a numérico
df = pd.get_dummies(df, drop_first=True)

# 3. Preparación de variables (asegurando el nombre correcto tras get_dummies)
# Al usar get_dummies, 'Churn_Yes' es el nuevo nombre de la columna target
X = df.drop('Churn_Yes', axis=1)
y = df['Churn_Yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# 4. Entrenamiento
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 5. Predicción y Evaluación
y_pred = modelo.predict(X_test)

# Visualización
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Churn', 'Churn'], 
            yticklabels=['No Churn', 'Churn'])
plt.ylabel('Real')
plt.xlabel('Predicho')
plt.title('Matriz de Confusión - Retención de Clientes')
plt.show()

print(classification_report(y_test, y_pred))