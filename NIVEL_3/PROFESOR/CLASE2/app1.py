import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import joblib

# 1. Cargar el modelo y columnas de entrenamiento (se ejecuta una vez)
@st.cache_resource
def cargar_modelo():
    modelo = joblib.load('modelo_rentabilidad_1.pkl')
    columnas = joblib.load('columnas_modelo_1.pkl')
    return modelo, columnas

# 2. Cargar datos (cache para mejorar rendimiento)
"""
Por razones prácticas, se ha tomado el mismo archivo de entrenamiento para la demo. En un caso real, se usaría un dataset diferente (idealmente de producción) para evaluar el modelo en datos no vistos.
"""
@st.cache_data
def cargar_datos():
    df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

modelo, columnas_esperadas = cargar_modelo()
df = cargar_datos()

st.title("Dashboard Ejecutivo de Ventas con Predicción")

# --- 1. Filtros laterales ---
region = st.sidebar.selectbox("Selecciona Región:", df['Region'].unique())
modo_pago = st.sidebar.selectbox("Modo de Pago:", df['Payment Mode'].unique())

# Filtrado dinámico
df_f = df[(df['Region'] == region) & (df['Payment Mode'] == modo_pago)]

# --- 2. Métricas clave (KPIs) ---
col1, col2 = st.columns(2)
col1.metric("Ventas Totales", f"${df_f['Sales'].sum():,.2f}")
col2.metric("Ganancia Total", f"${df_f['Profit'].sum():,.2f}")

# --- 3. Lógica para predecir sobre los datos filtrados ---
if st.button("Analizar Rentabilidad del Filtro Actual"):
    if not df_f.empty:
        # A. Preparar los datos del filtro de forma idéntica al entrenamiento
        # Si el modelo se entrenó con get_dummies, aplicamos lo mismo aquí:
        df_proc = pd.get_dummies(df_f, columns=['Category', 'Payment Mode', 'Region'])
        
        # B. Asegurar que tenga las mismas columnas que el modelo vio en el entrenamiento
        df_proc = df_proc.reindex(columns=columnas_esperadas, fill_value=0)
        
        # C. Realizar predicción
        prediccion = modelo.predict(df_proc)
        
        # D. Evaluación de resultado (promedio del segmento)
        if prediccion.mean() > 0.5:
            st.success(f"El modelo predice que este segmento es RENTABLE (Confianza promedio: {prediccion.mean():.2f})")
        else:
            st.error(f"El modelo predice que este segmento NO es rentable (Confianza promedio: {prediccion.mean():.2f})")
    else:
        st.warning("No hay datos suficientes para realizar la predicción con los filtros actuales.")

# --- 4. Visualizaciones ---
st.subheader("Tendencia de Ventas")
st.line_chart(df_f.groupby('Order Date')['Sales'].sum())

st.subheader("Relación Ventas vs. Ganancia")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=df_f, x='Sales', y='Profit', hue='Category', 
    size='Quantity', sizes=(20, 200), alpha=0.7, ax=ax
)
st.pyplot(fig)