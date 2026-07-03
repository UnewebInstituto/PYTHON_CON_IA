# Carga interactiva de reseñas
# ej05
import pandas as pd
import os
# Ruta a tu archivo en Drive
ruta_csv = 'dataset_arroz.csv'
def agregar_reseña():
    # 1. Cargar o crear el CSV
    if os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv)
    else:
        # Si no existe, creamos la estructura base
        df = pd.DataFrame(columns=['id', 'texto_original', 'categoria_tecnica', 'polaridad', 'fuente'])

    print("--- Nuevo Etiquetado de Reseñas ---")
    texto = input("Escribe la reseña del cliente: ")
    cat = input("Categoría (ej: aspecto, sabor, limpieza): ")
    polaridad = input("¿Es positiva (1) o negativa (0)?: ")
    
    # 2. Crear nueva fila
    nuevo_id = df['id'].max() + 1 if not df.empty else 1
    nueva_fila = {
        'id': nuevo_id,
        'texto_original': texto,
        'categoria_tecnica': cat,
        'polaridad': int(polaridad),
        'fuente': 'manual_proyecto'
    }
    
    # 3. Añadir y guardar
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_csv(ruta_csv, index=False)
    
    print(f"\nReseña {nuevo_id} guardada exitosamente en {ruta_csv}")


# Ejecuta esta función cada vez que quieras agregar una reseña
agregar_reseña()
--- Nuevo Etiquetado de Reseñas ---
Escribe la reseña del cliente: Muy buena apariencia y color claro
Categoría (ej: aspecto, sabor, limpieza): aspecto
¿Es positiva (1) o negativa (0)?: 1

Reseña 7 guardada exitosamente en dataset_arroz.csv
