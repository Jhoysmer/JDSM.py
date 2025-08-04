def mostrar_tabla():
    try:
        # Pedir un número entero entre 1 y 10
        n = int(input("Introduce un número entero entre 1 y 10: "))
        if n < 1 or n > 10:
            print("El número debe estar entre 1 y 10.")
            return
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    filename = f"tabla-{n}.txt"
    try:
        with open(filename, "r") as archivo:
            contenido = archivo.read()
        print(contenido)
    except FileNotFoundError:
        print(f"El fichero {filename} no existe.")
mostrar_tabla()