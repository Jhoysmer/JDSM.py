import csv

def estadisticas_columnas(diccionario, nombre_salida="estadisticas.csv"):
    from statistics import mean

    columnas_numericas = {}

    for clave, valores in diccionario.items():
        try:
            
            valores_float = [float(v.replace(',', '').strip()) for v in valores if v.replace(',', '').strip()]
            columnas_numericas[clave] = valores_float
        except ValueError:
            continue

    try:
        with open(nombre_salida, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(["Columna", "Mínimo", "Máximo", "Media"])

            for columna, valores in columnas_numericas.items():
                minimo = min(valores)
                maximo = max(valores)
                media = mean(valores)
                escritor.writerow([columna, minimo, maximo, media])

        print(f"Estadísticas guardadas en {nombre_salida}")

    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
