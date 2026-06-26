# Dependencias necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carga y Limpieza (Mantenemos tu lógica original)
df = pd.read_csv('Rice_MSC_Dataset.csv')

def limpiar_lote(df):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mean())
    return df.drop_duplicates()

df = limpiar_lote(df)
# Al terminar de crear/transformar columnas, re-creamos el df para compactar la memoria
df = df.copy()

# 2. Ingeniería de Variable Objetivo (Target Binario)
# Definimos Basmati como 1 (Premium/Aceptable) y el resto como 0
df['Calidad_Aceptable'] = np.where(df['CLASS'] == 'Basmati', 1, 0)
X = df.drop(columns=['CLASS', 'Calidad_Aceptable'])
y = df['Calidad_Aceptable']

# 3. Entrenamiento y Validación
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 4. Validación Cruzada Estratificada (Evaluación Robusta)
# Esto asegura que cada lote sea evaluado equitativamente
skf = StratifiedKFold(n_splits=5)
y_pred_cv = cross_val_predict(modelo, X, y, cv=skf)

# 5. Métricas de Evaluación
print("--- Reporte de Clasificación (Validación Cruzada) ---")
print(classification_report(y, y_pred_cv))

# Visualización de la Matriz de Confusión
cm = confusion_matrix(y, y_pred_cv)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', 
            xticklabels=['Otros', 'Basmati'], 
            yticklabels=['Otros', 'Basmati'])
plt.xlabel('Predicho')
plt.ylabel('Real')
plt.title('Matriz de Confusión: Clasificación Premium (Basmati)')
plt.show()