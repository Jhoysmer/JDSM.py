import urllib.request
import gzip
import io

def mostrar_pib_pais():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portletprod/BulkDownloadListingfile=daa/sdg_08_10.tsv.gz&unzip=true"

    try:
        response = urllib.request.urlopen(url)
        compressed_data = response.read()
        decompressed_data = gzip.decompress(compressed_data)
        contenido = decompressed_data.decode('utf-8')

        pais_codigo = input("Introduce el código del país (ej. ES, DE, FR): ").upper()

        lineas = contenido.splitlines()
        encabezado = lineas[0].split('\t')
        print(f"\nAños disponibles: {' | '.join(encabezado[1:])}")

        encontrado = False
        for linea in lineas[1:]:
            if linea.startswith(pais_codigo):
                datos = linea.split('\t')
                print(f"\nPIB per cápita para {pais_codigo}:")
                for año, valor in zip(encabezado[1:], datos[1:]):
                    print(f"{año}: {valor}")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró información para el país con código '{pais_codigo}'.")

    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")

mostrar_pib_pais()
