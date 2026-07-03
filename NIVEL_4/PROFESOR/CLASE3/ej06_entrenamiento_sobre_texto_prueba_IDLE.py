Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import os
ruta_csv = './NIVEL_4/PROFESOR/CLASE3/dataset_arroz.csv'
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

    cat = input("Categoría (ej: aspecto, sabor, limpieza): ").strip()
    
    # 3. Validación de Polaridad (Solo 0 o 1)
    while True:
        pol = input("¿Es positiva (1) o negativa (0)?: ").strip()
        if pol in ['0', '1']:
            polaridad = int(pol)
            break
        print("Error: Debes ingresar solo 0 o 1.")
    
    # 4. Crear nueva fila
    nuevo_id = df['id'].max() + 1 if not df.empty else 1
    nueva_fila = {
        'id': nuevo_id,
        'texto_original': texto,
        'categoria_tecnica': cat,
        'polaridad': polaridad,
        'fuente': 'manual_proyecto'
    }
    
    # 5. Guardado seguro
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_csv(ruta_csv, index=False)
    
    print(f"\n✅ Reseña {nuevo_id} guardada con éxito.")


# Ejecutar
agregar_reseña()
--- Nuevo Etiquetado (Proyecto Data Collector) ---
Escribe la reseña del cliente: la
Error: La reseña es muy corta o está vacía. Inténtalo de nuevo.
Escribe la reseña del cliente: Los granos presentan impurezas y mal olor
Categoría (ej: aspecto, sabor, limpieza): x
¿Es positiva (1) o negativa (0)?: 0

✅ Reseña 9 guardada con éxito.
