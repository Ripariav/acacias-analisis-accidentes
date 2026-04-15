import pandas as pd
import os

def clean_accident_data(input_path, output_path):
    print(f"--- Iniciando limpieza de datos desde {input_path} ---")
    
    # Cargar el dataset original
    try:
        df = pd.read_csv(input_path, encoding='latin1')
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return

    # 1. Eliminar columnas innecesarias si existen
    if "Codigo_Accidente" in df.columns:
        df = df.drop(columns=["Codigo_Accidente"])
    
    # 2. Limpieza de fechas
    df["Fecha_Ocurrencia"] = pd.to_datetime(df["Fecha_Ocurrencia"], errors='coerce')
    df["Día"] = df["Fecha_Ocurrencia"].dt.day
    df["Mes"] = df["Fecha_Ocurrencia"].dt.month
    df["Año"] = df["Fecha_Ocurrencia"].dt.year
    
    # 3. Limpieza de Muertes (reemplazar 'NO APLICA' por 0)
    df['Muertes'] = df['Muertes'].replace('NO APLICA', 0).fillna(0).astype(int)
    
    # 4. Limpieza de Barrios y corrección de codificación
    # Mapeo de correcciones comunes para "latin1" mal interpretado
    correcciones = {
        'SAN JOSÃ\x89': 'SAN JOSÉ',
        'SIN INFORMACIÃ\x93N DEL BARRIO': 'No registra',
        'VILLAVICENCIO': 'No registra',
        'VÃ\x8d A GRANADA-VILLAVICENCIO': 'Vía Granada-Villavicencio',
        'ARANJUEZ': 'ARANJUEZ',
        'CENTRO': 'CENTRO',
        'BACHUE': 'BACHUÉ'
    }
    
    df['Barrio'] = df['Barrio'].replace(correcciones)
    # Limpieza general de espacios y mayúsculas
    df['Barrio'] = df['Barrio'].str.strip().str.upper()
    
    # 5. Crear Columnas de Mortalidad
    df['Mortalidad'] = df['Muertes'] > 0
    df['Mortalidad_label'] = df['Mortalidad'].map({True: "Con mortalidad", False: "Sin mortalidad"})
    
    # 6. Mapeo de meses a nombres (para que se vea mejor en el dashboard)
    meses_nombres = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    df['Mes_Nombre'] = df['Mes'].map(meses_nombres)

    # Guardar el dataset limpio
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"--- Datos guardados exitosamente en {output_path} ---")
    return df

if __name__ == "__main__":
    clean_accident_data('data/accidentes.csv', 'data/accidentesLimpio.csv')
