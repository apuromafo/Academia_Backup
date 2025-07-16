import requests
from bs4 import BeautifulSoup
import html2text

def obtener_y_convertir_a_md(url):
    """
    Descarga el contenido de una URL, extrae el cuerpo principal
    y lo convierte a formato Markdown.
    """
    try:
        # 1. Descargar el contenido de la página
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa

        # 2. Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # 3. Encontrar el contenido principal de la página.
        #    Esto es crucial para evitar el header, footer, etc.
        #    Examinando el HTML de la página, el contenido principal
        #    está dentro de un <main>
        main_content = soup.find('main')

        if not main_content:
            print("No se pudo encontrar el elemento <main> con el contenido principal.")
            return None

        # 4. Convertir el contenido HTML a Markdown
        #    Se configura html2text para un formato más limpio
        converter = html2text.HTML2Text()
        converter.body_width = 0  # Desactiva el ajuste de línea para un mejor formato
        markdown_text = converter.handle(str(main_content))

        return markdown_text

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la página: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.hacker101.com/resources"
    
    print(f"Intentando convertir {url} a Markdown...")
    markdown_content = obtener_y_convertir_a_md(url)
    
    if markdown_content:
        # 5. Guardar el resultado en un archivo
        file_name = "hacker101_resources.md"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"\n¡Conversión exitosa! El contenido se ha guardado en '{file_name}'.")
    else:
        print("\nNo se pudo completar la conversión.")