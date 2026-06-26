# Ejemplo Calidad Vino Tinto
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Carga del dataset (asegúrate de tener el archivo winequality-red.csv)
df = pd.read_csv('winequality-red.csv')
df
      fixed acidity  volatile acidity  citric acid  residual sugar  ...    pH  sulphates  alcohol  quality
0               7.4             0.700         0.00             1.9  ...  3.51       0.56      9.4        5
1               7.8             0.880         0.00             2.6  ...  3.20       0.68      9.8        5
2               7.8             0.760         0.04             2.3  ...  3.26       0.65      9.8        5
3              11.2             0.280         0.56             1.9  ...  3.16       0.58      9.8        6
4               7.4             0.700         0.00             1.9  ...  3.51       0.56      9.4        5
...             ...               ...          ...             ...  ...   ...        ...      ...      ...
1594            6.2             0.600         0.08             2.0  ...  3.45       0.58     10.5        5
1595            5.9             0.550         0.10             2.2  ...  3.52       0.76     11.2        6
1596            6.3             0.510         0.13             2.3  ...  3.42       0.75     11.0        6
1597            5.9             0.645         0.12             2.0  ...  3.57       0.71     10.2        5
1598            6.0             0.310         0.47             3.6  ...  3.39       0.66     11.0        6

[1599 rows x 12 columns]
# 2. Ingeniería de Variable Objetivo
# Transformamos la escala 3-9 a binario: 
# Calidad >= 7 se considera 'Alta Calidad' (1), de lo contrario 'Estándar' (0)
df['Es_Alta_Calidad'] = np.where(df['quality'] >= 7, 1, 0)
df
      fixed acidity  volatile acidity  citric acid  ...  alcohol  quality  Es_Alta_Calidad
0               7.4             0.700         0.00  ...      9.4        5                0
1               7.8             0.880         0.00  ...      9.8        5                0
2               7.8             0.760         0.04  ...      9.8        5                0
3              11.2             0.280         0.56  ...      9.8        6                0
4               7.4             0.700         0.00  ...      9.4        5                0
...             ...               ...          ...  ...      ...      ...              ...
1594            6.2             0.600         0.08  ...     10.5        5                0
1595            5.9             0.550         0.10  ...     11.2        6                0
1596            6.3             0.510         0.13  ...     11.0        6                0
1597            5.9             0.645         0.12  ...     10.2        5                0
1598            6.0             0.310         0.47  ...     11.0        6                0

[1599 rows x 13 columns]
# 3. Preparación de X e y
X = df.drop(columns=['quality', 'Es_Alta_Calidad'])
y = df['Es_Alta_Calidad']
X
      fixed acidity  volatile acidity  citric acid  residual sugar  ...  density    pH  sulphates  alcohol
0               7.4             0.700         0.00             1.9  ...  0.99780  3.51       0.56      9.4
1               7.8             0.880         0.00             2.6  ...  0.99680  3.20       0.68      9.8
2               7.8             0.760         0.04             2.3  ...  0.99700  3.26       0.65      9.8
3              11.2             0.280         0.56             1.9  ...  0.99800  3.16       0.58      9.8
4               7.4             0.700         0.00             1.9  ...  0.99780  3.51       0.56      9.4
...             ...               ...          ...             ...  ...      ...   ...        ...      ...
1594            6.2             0.600         0.08             2.0  ...  0.99490  3.45       0.58     10.5
1595            5.9             0.550         0.10             2.2  ...  0.99512  3.52       0.76     11.2
1596            6.3             0.510         0.13             2.3  ...  0.99574  3.42       0.75     11.0
1597            5.9             0.645         0.12             2.0  ...  0.99547  3.57       0.71     10.2
1598            6.0             0.310         0.47             3.6  ...  0.99549  3.39       0.66     11.0

[1599 rows x 11 columns]
y
0       0
1       0
2       0
3       0
4       0
       ..
1594    0
1595    0
1596    0
1597    0
1598    0
Name: Es_Alta_Calidad, Length: 1599, dtype: int64
# 4. Configuración de Validación Cruzada Estratificada
# Usamos 5 splits para asegurar que el modelo vea suficientes vinos 'Alta Calidad'
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
modelo = RandomForestClassifier(n_estimators=150, random_state=42)
# Predicciones mediante validación cruzada
y_pred_cv = cross_val_predict(modelo, X, y, cv=skf)
# 5. Evaluación de Métricas
print("--- Reporte de Clasificación (Validación Cruzada) ---")
--- Reporte de Clasificación (Validación Cruzada) ---
print(classification_report(y, y_pred_cv))
              precision    recall  f1-score   support

           0       0.92      0.98      0.95      1382
           1       0.76      0.49      0.60       217

    accuracy                           0.91      1599
   macro avg       0.84      0.73      0.77      1599
weighted avg       0.90      0.91      0.90      1599

# 6. Visualización de Matriz de Confusión
cm = confusion_matrix(y, y_pred_cv)
plt.figure(figsize=(6, 5))
<Figure size 600x500 with 0 Axes>
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', 
            xticklabels=['Estándar', 'Alta Calidad'], 
            yticklabels=['Estándar', 'Alta Calidad'])
<Axes: >
plt.xlabel('Predicho')
Text(0.5, 25.722222222222214, 'Predicho')
plt.ylabel('Real')
Text(45.72222222222221, 0.5, 'Real')
plt.title('Matriz de Confusión: Clasificación de Vinos')
Text(0.5, 1.0, 'Matriz de Confusión: Clasificación de Vinos')
plt.show()
