import csv

def leer_cotizaciones_por_columnas(nombre_fichero):
    columnas = {}

    try:
        with open(nombre_fichero, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
         
            for campo in lector.fieldnames:
                columnas[campo] = []

            for fila in lector:
                for clave, valor in fila.items():
                    columnas[clave].append(valor)
        return columnas

    except FileNotFoundError:
        print(f"El fichero '{nombre_fichero}' no se encontró.")
        return {}
    except Exception as e:
        print(f"Error al leer el fichero: {e}")
        return {}
