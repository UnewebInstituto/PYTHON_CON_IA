# Cargar librerías necesarias
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Cargar datos
df = pd.read_csv("C:/Users/duque/Documents/Henry Duque/UNEWEB/PYTHON_CON_IA/NIVEL_2/PROFESOR/CLASE5/Ecommerce_Sales_Data_2024_2025.csv")

# Convertir fechas y asegurar tipos numéricos
df['Order Date'] = pd.to_datetime(df['Order Date'])
cols_numericas = ['Quantity', 'Unit Price', 'Discount', 'Sales', 'Profit']
df[cols_numericas] = df[cols_numericas].apply(pd.to_numeric)

# Calcular margen de beneficio
df['Profit Margin'] = (df['Profit'] / df['Sales']) * 100

# Análisis rápido: Profit por Categoría
profit_por_cat = df.groupby('Category')['Profit'].sum().reset_index()

# Agrupación multidimensional para el dashboard
tendencia_geo = df.groupby(['Order Date', 'Region', 'Payment Mode'])[['Sales', 'Profit']].sum().reset_index()

# **************************************************** #

st.title("Dashboard Ejecutivo de Ventas")

# --- 1. Filtros laterales ---
region = st.sidebar.selectbox("Selecciona Región:", df['Region'].unique())
modo_pago = st.sidebar.selectbox("Modo de Pago:", df['Payment Mode'].unique())

# Filtrado dinámico
df_f = df[(df['Region'] == region) & (df['Payment Mode'] == modo_pago)]

# --- 2. Métricas clave (KPIs) ---
col1, col2 = st.columns(2)
col1.metric("Ventas Totales", f"${df_f['Sales'].sum():,.2f}")
col2.metric("Ganancia Total", f"${df_f['Profit'].sum():,.2f}")

# --- 3. Gráfico de tendencia (Line Chart de Streamlit) ---
st.subheader("Tendencia de Ventas")
st.line_chart(df_f.groupby('Order Date')['Sales'].sum())

# --- 4. Gráfico de Dispersión (Seaborn adaptado a Streamlit) ---
st.subheader("Relación Ventas vs. Ganancia")

# Creamos la figura explícitamente para que Streamlit pueda renderizarla
fig, ax = plt.subplots(figsize=(10, 6))

sns.scatterplot(
    data=df_f, 
    x='Sales', 
    y='Profit', 
    hue='Category', 
    size='Quantity', 
    sizes=(20, 200), 
    alpha=0.7,
    ax=ax  # Importante: pasamos el eje 'ax' creado arriba
)

plt.title("Relación Ventas vs. Ganancia por Producto")
plt.xlabel("Ventas")
plt.ylabel("Ganancia")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Renderizamos en Streamlit usando st.pyplot
st.pyplot(fig)