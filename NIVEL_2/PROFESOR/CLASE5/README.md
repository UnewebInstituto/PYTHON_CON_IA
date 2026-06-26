# Dashboard Ejecutivo de Ventas

Este proyecto es un informe interactivo desarrollado con **Streamlit** para analizar las tendencias de ventas de una tienda de comercio electrónico, permitiendo filtrar datos por región y modo de pago, además de visualizar la relación entre ventas y ganancias.

## 1. Instalación de Dependencias

Para ejecutar este proyecto, asegúrate de tener instalado Python 3.x. Se recomienda utilizar un entorno virtual.

### Pasos:

1. **Clonar o descargar el repositorio:**
   Asegúrate de tener el archivo `app.py` y el archivo de datos `Ecommerce_Sales_Data_2024_2025.csv` en la misma carpeta.

2. **Crear y activar un entorno virtual (recomendado):**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\\Scripts\\activate

```

3. **Instalar las librerías necesarias:**
Ejecuta el siguiente comando en tu terminal para instalar las dependencias requeridas:
```bash
pip install streamlit pandas matplotlib seaborn

```

4. **Ejecutar la aplicación:**
Una vez instaladas las dependencias, lanza la aplicación con:
```bash
streamlit run app.py

```

Esto abrirá automáticamente tu navegador en `http://localhost:8501`.

---

## 2. Hallazgos Interesantes en los Datos

Durante el análisis exploratorio (EDA) del dataset `Ecommerce_Sales_Data_2024_2025.csv`, se descubrieron los siguientes puntos clave:

* **Estacionalidad:** Se observa un incremento significativo en el volumen de ventas hacia finales de año, lo cual es consistente con las temporadas de festividades y promociones masivas.
* **Correlación Ventas-Ganancia:** Mediante el gráfico de dispersión, se identificó que no siempre los productos con mayor volumen de ventas (`Sales`) son los más rentables (`Profit`). Existen categorías con altas ventas pero márgenes de ganancia estrechos debido a descuentos elevados.
* **Influencia del Modo de Pago:** El análisis segmentado permite notar diferencias en el comportamiento de compra según el `Payment Mode`, sugiriendo que ciertos métodos de pago están más asociados a compras de mayor valor unitario.
* **Rentabilidad por Categoría:** Algunas categorías muestran una mayor dispersión en los beneficios, indicando una necesidad de optimización de precios o reducción de costos operativos en sub-categorías específicas.
