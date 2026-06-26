import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
# pip install imblearn
from imblearn.over_sampling import SMOTE

# 1. Carga en Google Colab
df = pd.read_csv('creditcard.csv')
# Prueba en idlelib
#df = pd.read_csv('creditcard_test.csv')
#X = df.drop('Class', axis=1)
#y = df['Class']

# Opción: Eliminar las filas donde 'Class' es NaN
# Esto asegura que X e y tengan el mismo tamaño y sean numéricos
df_limpio = df.dropna(subset=['Class'])

# Re-define tus variables con el dataframe limpio
X = df_limpio.drop('Class', axis=1)
y = df_limpio['Class']

# 2. Balanceo con SMOTE
# Por omisión k_neighbors=6 Google Colab
smote = SMOTE(random_state=42)
# Para la prueba idlelib
# smote = SMOTE(k_neighbors=2, random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# 3. Entrenamiento del modelo final
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_res, y_res)

# 4. Guardado del modelo y columnas
joblib.dump(modelo, 'modelo_fraude.pkl')
joblib.dump(X.columns.tolist(), 'columnas_fraude.pkl')

# 5. Generación de Matriz de Confusión para reporte
y_pred = cross_val_predict(modelo, X_res, y_res, cv=5)
cm = confusion_matrix(y_res, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds')
plt.title("Matriz de Confusión - Detección de Fraude")
plt.savefig('matriz_fraude.png')
plt.show()

