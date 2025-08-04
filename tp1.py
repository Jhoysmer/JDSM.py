def tabla(n):
    if 1 <= n <=10:
        with open(f"tabla-{n}.txt", "w") as f:
            f.writelines([f"{n} x {i} = {n*i}\n" for i in range(1, 11)])
        print(f"Tabla guardada en 'tabla-n.txt'")
    else:
        print("Numero fuera del rango (1 - 10)")

tabla(int(input("introduce un numero del 1 al 10: ")))