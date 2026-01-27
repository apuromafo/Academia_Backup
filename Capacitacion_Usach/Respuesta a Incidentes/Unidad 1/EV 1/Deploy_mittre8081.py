import os
import subprocess
import sys

def run_command(command, cwd=None):
    try:
        subprocess.check_call(command, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error ejecutando: {command}")
        sys.exit(1)

def setup_navigator():
    repo_dir = "attack-navigator"
    # Usamos 8081 para que puedas tener CARET (8080) y Navigator al mismo tiempo
    port = "8081" 
    
    if not os.path.exists(repo_dir):
        print("[+] Clonando MITRE ATT&CK Navigator...")
        run_command("git clone https://github.com/mitre-attack/attack-navigator.git")
    
    nav_app_path = os.path.join(repo_dir, "nav-app")

    # Dockerfile siguiendo estrictamente el manual (dist/browser)
    dockerfile_content = """
FROM node:18-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Según el manual: ng build --configuration production
# (npm run build suele ejecutar esto internamente)
RUN npm run build -- --configuration production

FROM nginx:stable-alpine
# Según el manual, la salida está en: dist/browser/
COPY --from=build-stage /app/dist/browser/ /usr/share/nginx/html/
# Configuración para Angular Router
RUN sed -i 's/index  index.html index.htm;/index  index.html index.htm; try_files $uri $uri\\/ \\/index.html;/g' /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
"""

    with open(os.path.join(nav_app_path, "Dockerfile"), "w") as f:
        f.write(dockerfile_content.strip())

    print("[+] Construyendo imagen de producción (dist/browser)...")
    run_command("docker build -t mitre-navigator .", cwd=nav_app_path)

    print("[+] Limpiando contenedores previos...")
    subprocess.run("docker stop navigator-app", shell=True, stderr=subprocess.DEVNULL)
    subprocess.run("docker rm navigator-app", shell=True, stderr=subprocess.DEVNULL)

    print(f"[+] Iniciando ATT&CK Navigator en http://localhost:{port}")
    run_command(f"docker run -d -p {port}:80 --name navigator-app mitre-navigator", cwd=nav_app_path)

    print("\n" + "="*50)
    print("🚀 NAVEGADOR DESPLEGADO")
    print(f"🔗 URL: http://localhost:{port}")
    print("="*50)

if __name__ == "__main__":
    setup_navigator()