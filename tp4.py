import urllib.request

def contar_palabras_url():
    url = input("Introduce la URL del fichero de texto: ")
    try:
        response = urllib.request.urlopen(url)
        contenido = response.read().decode('utf-8')
        palabras = contenido.split()
        print(f"El número de palabras en el archivo es: {len(palabras)}")
    except Exception as e:
        print(f"Error al acceder a la URL: {e}")

contar_palabras_url()
