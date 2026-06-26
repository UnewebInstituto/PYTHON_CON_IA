import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar datos
ruta = "C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv"
df = pd.read_csv(ruta)

# 2. Ingeniería de variables (Debemos crear X e y aquí)
# Calculamos el margen y creamos el target
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
df['Target_Alto_Valor'] = (df['Profit_Margin'] > 10).astype(int) # Ajusta este umbral según necesites

# Preprocesamiento: convertimos columnas categóricas a numéricas
df_model = pd.get_dummies(df, columns=['Category', 'Payment Mode'], drop_first=True)

# Definimos X e y (aquí es donde se crean y dejan de dar error)
features = ['Sales', 'Quantity', 'Discount', 'Profit']
X = df_model[features]
y = df_model['Target_Alto_Valor']

# 3. Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entrenamiento
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# 5. Predicción y Evaluación
y_pred = modelo.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusión')
plt.show()

print(classification_report(y_test, y_pred))