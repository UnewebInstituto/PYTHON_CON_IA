import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carga del dataset (asegúrate de tener el archivo winequality-red.csv)
df = pd.read_csv('winequality-red.csv')

# 2. Ingeniería de Variable Objetivo
# Transformamos la escala 3-9 a binario: 
# Calidad >= 7 se considera 'Alta Calidad' (1), de lo contrario 'Estándar' (0)
df['Es_Alta_Calidad'] = np.where(df['quality'] >= 7, 1, 0)

# 3. Preparación de X e y
X = df.drop(columns=['quality', 'Es_Alta_Calidad'])
y = df['Es_Alta_Calidad']

# 4. Configuración de Validación Cruzada Estratificada
# Usamos 5 splits para asegurar que el modelo vea suficientes vinos 'Alta Calidad'
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
modelo = RandomForestClassifier(n_estimators=150, random_state=42)

# Predicciones mediante validación cruzada
y_pred_cv = cross_val_predict(modelo, X, y, cv=skf)

# 5. Evaluación de Métricas
print("--- Reporte de Clasificación (Validación Cruzada) ---")
print(classification_report(y, y_pred_cv))

# 6. Visualización de Matriz de Confusión
cm = confusion_matrix(y, y_pred_cv)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', 
            xticklabels=['Estándar', 'Alta Calidad'], 
            yticklabels=['Estándar', 'Alta Calidad'])
plt.xlabel('Predicho')
plt.ylabel('Real')
plt.title('Matriz de Confusión: Clasificación de Vinos')
plt.show()