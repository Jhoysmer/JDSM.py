def mostrar_linea_tabla():
    import os

    try:
        n = int(input("Introduce un número n (entre 1 y 10): "))
        m = int(input("Introduce un número m (entre 1 y 10): "))
        if not (1 <= n <= 10 and 1 <= m <= 10):
            print("Ambos números deben estar entre 1 y 10.")
            return

        nombre_fichero = f"tabla-{n}.txt"

        if not os.path.isfile(nombre_fichero):
            print(f"El fichero '{nombre_fichero}' no existe.")
            return

        with open(nombre_fichero, "r") as f:
            lineas = f.readlines()
            if m <= len(lineas):
                print(f"Línea {m} del fichero: {lineas[m - 1].strip()}")
            else:
                print(f"El fichero no tiene {m} líneas.")
    except ValueError:
        print("Debes ingresar números válidos.")

mostrar_linea_tabla()
