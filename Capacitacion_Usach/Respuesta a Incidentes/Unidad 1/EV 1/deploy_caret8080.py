import os
import subprocess
import sys

def run_command(command, cwd=None):
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error: {command}")
        sys.exit(1)

def setup_caret():
    repo_dir = "caret"
    port = "8080"
    
    # 1. Configuración de Nginx
    nginx_conf = """
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;
    location / {
        try_files $uri $uri/ /index.html;
    }
    location = /favicon.ico { log_not_found off; access_log off; }
}
"""
    # Preparar archivos
    if not os.path.exists(repo_dir):
        print("[+] Clonando repositorio...")
        run_command("git clone https://github.com/mitre-attack/caret.git")

    with open(os.path.join(repo_dir, "nginx_custom.conf"), "w") as f:
        f.write(nginx_conf)

    dockerfile_content = """
FROM node:10-stretch AS build-stage
RUN npm install -g gulp bower
WORKDIR /app
COPY package*.json ./
COPY bower.json ./
RUN npm install
RUN bower install --allow-root
COPY . .
RUN gulp build

FROM nginx:stable-alpine
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx_custom.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
"""
    with open(os.path.join(repo_dir, "Dockerfile"), "w") as f:
        f.write(dockerfile_content.strip())

    # 2. Construcción
    print(f"[+] Iniciando Build de Docker para CARET...")
    run_command(f"docker build -t mitre-caret .", cwd=repo_dir)

    # 3. Limpieza y Ejecución
    subprocess.run("docker stop caret-app", shell=True, stderr=subprocess.DEVNULL)
    subprocess.run("docker rm caret-app", shell=True, stderr=subprocess.DEVNULL)

    print(f"[+] Levantando contenedor en puerto {port}...")
    run_command(f"docker run -d -p {port}:80 --name caret-app mitre-caret", cwd=repo_dir)

    # Info de salida scannable
    print("\n" + "="*50)
    print("🚀 DESPLIEGUE EXITOSO")
    print("-"*50)
    print(f"🔗 URL local:    http://localhost:{port}")
    print(f"🐳 Contenedor:   caret-app")
    print(f"📂 Status:       Running (Nginx)")
    print("="*50)
    print("[TIP] Si no ves datos, revisa la consola F12 por errores de API.")

if __name__ == "__main__":
    setup_caret()