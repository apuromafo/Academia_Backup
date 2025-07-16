import requests
from bs4 import BeautifulSoup
import html2text
import os
import time

def obtener_urls_de_lecciones(url_base):
    """
    Rastrea la página de la lista de reproducción de web hacking para obtener todas las URLs de las lecciones.
    """
    print(f"Rastreando la página de la lista de reproducción en {url_base} para obtener las URLs...")
    try:
        response = requests.get(url_base)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encuentra la sección de lecciones por el encabezado con id="lessons"
        lessons_section = soup.find('h2', id='lessons')
        if not lessons_section:
            print("No se encontró el encabezado con id='lessons'. La estructura HTML puede haber cambiado.")
            return []
            
        # El <ul> con los enlaces es el siguiente elemento hermano del <h2>
        lessons_list = lessons_section.find_next_sibling('ul')
        
        if not lessons_list:
            print("No se encontró la lista de lecciones <ul>. Revisa la estructura HTML.")
            return []
            
        links = lessons_list.find_all('a')
        
        # Crea una lista de URLs absolutas
        urls_de_lecciones = [f"https://www.hacker101.com{link.get('href')}" for link in links if link.get('href')]
        
        print(f"  -> Encontradas {len(urls_de_lecciones)} URLs de lecciones.")
        return urls_de_lecciones
        
    except requests.exceptions.RequestException as e:
        print(f"Error al rastrear {url_base}: {e}")
        return []
        
def procesar_leccion(url):
    """
    Procesa una URL de lección individual, extrae el contenido,
    y encuentra los enlaces de YouTube.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # El contenido principal está dentro de la etiqueta <main>
        main_content = soup.find('main')
        if not main_content:
            print(f"  -> No se encontró el contenido principal en {url}")
            return None, None

        # Encontrar iframes de YouTube
        youtube_links = []
        iframes = main_content.find_all('iframe')
        for iframe in iframes:
            src = iframe.get('src', '')
            if 'youtube-nocookie.com' in src or 'http://googleusercontent.com/youtube.com/' in src:
                # Extraer la clave del video de la URL
                key = src.split('/embed/')[1].split('?')[0]
                # Construir el enlace con el formato deseado
                youtube_url = f"https://www.youtube.com/watch?v={key}"
                youtube_links.append(youtube_url)

        # Convertir el contenido a Markdown
        converter = html2text.HTML2Text()
        converter.body_width = 0
        markdown_text = converter.handle(str(main_content))

        # Agregar los enlaces de YouTube al final del Markdown
        if youtube_links:
            markdown_text += "\n\n---\n\n### Videos de YouTube\n"
            # Se usa un conjunto para evitar enlaces duplicados
            for link in sorted(list(set(youtube_links))):
                markdown_text += f"* {link}\n"
        
        # Obtener un nombre de archivo limpio de la URL
        filename_part = url.split('/')[-1] or url.split('/')[-2]
        filename = f"{filename_part.replace('.html', '')}.md"

        return markdown_text, filename

    except requests.exceptions.RequestException as e:
        print(f"  -> Error al procesar la lección {url}: {e}")
        return None, None
    except Exception as e:
        print(f"  -> Ocurrió un error inesperado al procesar {url}: {e}")
        return None, None

def main():
    """
    Función principal para coordinar el rastreo y la conversión.
    """
    url_base_playlist = "https://www.hacker101.com/playlists/web_hacking"
    urls_de_lecciones = obtener_urls_de_lecciones(url_base_playlist)
    
    if not urls_de_lecciones:
        print("No se encontraron URLs de lecciones para procesar. Saliendo.")
        return

    output_dir = "hacker101_web_hacking_lecciones"
    os.makedirs(output_dir, exist_ok=True)

    print("\nIniciando la conversión de cada lección...")
    
    for i, url in enumerate(urls_de_lecciones, 1):
        print(f"\n({i}/{len(urls_de_lecciones)}) Procesando: {url}")
        markdown_content, file_name = procesar_leccion(url)
        
        if markdown_content and file_name:
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"  -> Conversión exitosa. Archivo guardado en '{file_path}'.")
        else:
            print(f"  -> No se pudo completar la conversión para {url}.")
        
        time.sleep(1) 

    print("\nProceso finalizado. Todos los archivos están en la carpeta 'hacker101_web_hacking_lecciones'.")

if __name__ == "__main__":
    main()