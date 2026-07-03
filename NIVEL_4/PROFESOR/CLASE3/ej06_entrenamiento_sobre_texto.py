import pandas as pd
import os

#ruta_csv = '/content/drive/MyDrive/data/dataset_arroz.csv'
ruta_csv = 'dataset_arroz.csv'

def agregar_reseña():
    # 1. Cargar o crear el CSV
    if os.path.exists(ruta_csv):
        df = pd.read_csv(ruta_csv)
    else:
        df = pd.DataFrame(columns=['id', 'texto_original', 'categoria_tecnica', 'polaridad', 'fuente'])

    print("--- Nuevo Etiquetado (Proyecto Data Collector) ---")
    
    # 2. Validación de Texto (No vacío)
    while True:
        texto = input("Escribe la reseña del cliente: ").strip()
        if len(texto) > 5: # Validamos longitud mínima para evitar errores
            break
        print("Error: La reseña es muy corta o está vacía. Inténtalo de nuevo.")

    # 3. Validación de Categoría (Solo ciertas categorías)
    while True:
        cat_leida = input("Categoría (ej: aspecto, sabor, limpieza): ").strip()
        if cat_leida in ['aspecto', 'sabor', 'limpieza']:
            cat = cat_leida
            break
        print("Error: Categoría no válida. Inténtalo de nuevo ('aspecto', 'sabor', 'limpieza).")

    # cat = input("Categoría (ej: aspecto, sabor, limpieza): ").strip()
    
    # 4. Validación de Polaridad (Solo 0 o 1)
    while True:
        pol = input("¿Es positiva (1) o negativa (0)?: ").strip()
        if pol in ['0', '1']:
            polaridad = int(pol)
            break
        print("Error: Debes ingresar solo 0 o 1.")
    
    # 5. Crear nueva fila
    nuevo_id = df['id'].max() + 1 if not df.empty else 1
    nueva_fila = {
        'id': nuevo_id,
        'texto_original': texto,
        'categoria_tecnica': cat,
        'polaridad': polaridad,
        'fuente': 'manual_proyecto'
    }
    
    # 6. Guardado seguro
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_csv(ruta_csv, index=False)
    
    print(f"\n✅ Reseña {nuevo_id} guardada con éxito.")

# Ejecutar
agregar_reseña()
