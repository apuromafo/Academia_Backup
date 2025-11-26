#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import argparse
import sys
import time
import requests
import os
import shutil
import urllib3

# Suprimimos los warnings de SSL por defecto de requests desde el inicio
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ====================================================================
# 🌍 Diccionario Centralizado de Strings (i18n Ready)
# ====================================================================

STRINGS = {
    # --- Configuración/Constantes del Script ---
    "PWNDOC_PORT": 8443,
    "BACKEND_SERVICE": "pwndoc-backend",
    "TIMEOUT_SECONDS": 180,
    "INITIAL_WAIT": 20, # Pausa inicial después de levantar los contenedores
    "PWNDOC_REPO_URL": "https://github.com/pwndoc/pwndoc.git",
    "PWNDOC_DIR_NAME": "pwndoc", # Nombre de la carpeta que crea git clone

    # --- Textos del Script (ES - Español) ---
    "ES": {
        # run_command
        "RUNNING_COMMAND": "\n--- Ejecutando: {} ---",
        "WARN_STDERR": "Advertencias/Salida de error (no fatal): {}",
        "ERROR_CRITICAL": "\n!!! ERROR al ejecutar el comando: {} !!!",
        "ERROR_STDERR_OUT": "Salida de error:\n{}",
        "TIP_DOCKER_COMPOSE": "💡 Tip: Asegúrate de estar en el directorio raíz de pwndoc donde se encuentra docker-compose.yml.",
        "ERROR_NOT_FOUND": "\n!!! ERROR: {} no se encontró. Asegúrate de que esté instalado y en tu PATH. !!!",
        "ERROR_COMMAND_NOT_FOUND": "\n!!! ERROR: Comando no encontrado: {} !!!",
        "INTERRUPTED": "\nOperación interrumpida por el usuario.",
        "TIMEOUT_ERROR": "\n!!! ERROR: El comando {} ha excedido el tiempo de ejecución (300s). !!!",

        # check_docker_daemon
        "VERIFY_DOCKER_DAEMON": "🔍 Verificando el estado del Docker Daemon...",
        "DOCKER_OK": "✅ Docker Daemon está accesible.",
        "ERROR_DOCKER_CRITICAL": "❌ **¡ERROR CRÍTICO!** Fallo de conexión al Docker Daemon.",
        "TIP_DOCKER_START": "⭐ Por favor, inicia **Docker Desktop** o el **servicio Docker** y vuelve a intentarlo.",
        "ERROR_DOCKER_DETAIL": "Detalle del error:\n{}",
        "ERROR_DOCKER_TIMEOUT": "❌ **¡ERROR CRÍTICO!** La verificación del Docker Daemon agotó el tiempo de espera.",
        "ERROR_DOCKER_UNEXPECTED": "❌ ERROR Inesperado durante la verificación del Daemon: {}",

        # check_pwndoc_status
        "WAITING_FOR_SERVICE": "\n⏳ Esperando a que el servicio Pwndoc esté listo en {}...",
        "INITIAL_WAIT_MSG": "   (Pausa inicial de {} segundos para la inicialización)",
        "CONTINUE_VERIFY": "... Continuar verificación.",
        "PWNDOC_OK": "\n🎉 **¡Servicio Pwndoc OK!** El sitio web principal respondió correctamente.",
        "ACCESS_URL": "📋 Accede a Pwndoc en tu navegador en: **{}**",
        "PWNDOC_TIMEOUT_FAIL": "\n❌ **¡ERROR!** El servicio Pwndoc no estuvo disponible en {} segundos.",

        # setup_pwndoc_directory
        "DOCKER_COMPOSE_NOT_FOUND": "\n⚠️ El archivo 'docker-compose.yml' no se encuentra en el directorio actual.",
        "CLONING_REPO": "🌐 Clonando el repositorio de pwndoc en la carpeta '{}'...",
        "CHDIR_SUCCESS": "✅ Se ha cambiado el directorio de trabajo a: {}",
        "DIR_FOUND_CHDIR": "\n⭐ Se encontró la carpeta '{}'. Cambiando el directorio de trabajo.",
        "SETUP_FAIL": "❌ No se pudo configurar el directorio de pwndoc. Abortando.",

        # build_and_run
        "BUILD_AND_RUN_START": "Iniciando: Construyendo imágenes y levantando contenedores (en segundo plano)...",
        "ORCHESTRATION_SUCCESS": "\n✅ Proceso de Orquestación Finalizado con Éxito.",
        "HTTPS_NOTICE": "Aviso: El acceso es HTTPS (https://localhost:{}).",
        "SECURITY_REMINDER": "Recordatorio: Debes cambiar los certificados SSL y el secreto JWT para producción.",
        "VALIDATION_FAILED": "\n❌ La validación del servicio Pwndoc falló después de levantarse. Ver logs con 'logs'.",
        "UP_COMMAND_FAILED": "\n❌ El comando 'docker-compose up' falló. Revisa los logs de error anteriores.",

        # show_logs
        "SHOWING_LOGS": "Mostrando logs en tiempo real para el servicio: {}",

        # stop_containers
        "STOPPING_CONTAINERS": "Deteniendo contenedores de pwndoc...",

        # start_containers
        "STARTING_CONTAINERS": "Iniciando contenedores de pwndoc...",

        # remove_containers
        "REMOVING_CONTAINERS": "Eliminando contenedores, redes y volúmenes de pwndoc...",

        # update_application
        "UPDATE_CRITICAL_ERROR": "\n❌ **ERROR CRÍTICO:** No se encontró 'docker-compose.yml'.",
        "UPDATE_TIP": "⭐ Para actualizar, debes ejecutar este script DENTRO de la carpeta 'pwndoc'. Abortando.",
        "UPDATE_START": "--- Proceso de Actualización de pwndoc ---",
        "UPDATE_DOWN_WARN": "⚠️ No se pudo detener completamente la aplicación (puede que no estuviera corriendo), continuando...",
        "UPDATE_GIT_PULL": "\nActualizando código fuente con git pull...",
        "UPDATE_GIT_PULL_FAIL": "❌ No se pudo realizar el git pull. Abortando actualización.",
        "UPDATE_BUILD_START": "\nReconstruyendo y levantando la aplicación con el nuevo código...",
        "UPDATE_COMPLETE": "\n*** 🎉 ¡Actualización de pwndoc completada! ***\n",
        
        # main
        "PARSER_DESCRIPTION": "Orquestador en Python para la aplicación pwndoc (multi-contenedor) con docker-compose. Acceso en https://localhost:{}.",
        "PARSER_HELP_ACTIONS": (
            "Acciones disponibles (Ejecutar desde el directorio del orquestador):\n"
            "  up    : Verifica Docker, CLONA/MUEVE a pwndoc, construye imágenes y valida el servicio (docker-compose up -d --build)\n"
            "  logs  : Muestra logs en tiempo real del backend.\n"
            "  stop  : Detiene los contenedores.\n"
            "  start : Verifica Docker, inicia los contenedores detenidos y valida el servicio.\n"
            "  down  : Baja y elimina contenedores/redes/volúmenes por defecto.\n"
            "  update: Detiene, actualiza el código fuente con git pull, y vuelve a levantar (DEBE EJECUTARSE DENTRO DE LA CARPETA PWNDOC)."
        ),
        "ACTION_PRECHECK_FAIL": "\n❌ **ERROR CRÍTICO:** No se encontró el archivo 'docker-compose.yml' y tampoco la carpeta 'pwndoc'.",
        "ACTION_PRECHECK_TIP": "⭐ Para ejecutar esta acción, debes estar dentro del directorio 'pwndoc' o ejecutar 'up' primero.",
    }
}

# Variable para el idioma (por defecto español)
LANG = STRINGS["ES"]

# ====================================================================
# ⚙️ Constantes de Configuración (Extraídas del diccionario)
# ====================================================================

PWNDOC_PORT = STRINGS["PWNDOC_PORT"]
BACKEND_SERVICE = STRINGS["BACKEND_SERVICE"]
TIMEOUT_SECONDS = STRINGS["TIMEOUT_SECONDS"]
INITIAL_WAIT = STRINGS["INITIAL_WAIT"]
PWNDOC_REPO_URL = STRINGS["PWNDOC_REPO_URL"]
PWNDOC_DIR_NAME = STRINGS["PWNDOC_DIR_NAME"]


# --- Funciones Auxiliares Comunes ---

def run_command(command, check=True):
    """
    Ejecuta un comando en el shell y maneja la salida y los errores.
    """
    command_str = " ".join(command)
    # Excluir logs de la impresión inicial para comandos interactivos
    if command[0] != "docker-compose" or command[1] != "logs":
        print(LANG["RUNNING_COMMAND"].format(command_str))
        
    try:
        result = subprocess.run(
            command, 
            check=check, 
            text=True, 
            capture_output=(command[0] != "docker-compose" or command[1] != "logs"),
            timeout=300 # Aumentado el timeout para que la clonación/build tenga tiempo
        )
        
        # Si capturamos la salida, la imprimimos
        if result.stdout and (command[0] != "docker-compose" or command[1] != "logs"):
            print(result.stdout)
        
        # Si hubo un error no fatal o advertencia
        if result.stderr and check and (command[0] != "docker-compose" or command[1] != "logs"):
             print(LANG["WARN_STDERR"].format(result.stderr))
             
        return result

    except subprocess.CalledProcessError as e:
        print(LANG["ERROR_CRITICAL"].format(command_str))
        print(LANG["ERROR_STDERR_OUT"].format(e.stderr))
        print(LANG["TIP_DOCKER_COMPOSE"])
        sys.exit(1)
    except FileNotFoundError:
        # Captura errores de "comando no encontrado"
        if command[0] in ["docker-compose", "git"]:
            print(LANG["ERROR_NOT_FOUND"].format(command[0]))
        else:
            print(LANG["ERROR_COMMAND_NOT_FOUND"].format(command[0]))
        sys.exit(1)
    except KeyboardInterrupt:
        print(LANG["INTERRUPTED"])
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print(LANG["TIMEOUT_ERROR"].format(command_str))
        sys.exit(1)
    return None

def check_docker_daemon():
    """Verifica si Docker está accesible antes de empezar."""
    print(LANG["VERIFY_DOCKER_DAEMON"])
    try:
        subprocess.run(
            ["docker", "info"], 
            check=True, 
            text=True, 
            capture_output=True,
            timeout=10
        )
        print(LANG["DOCKER_OK"])
        return True
    except subprocess.CalledProcessError as e:
        print(LANG["ERROR_DOCKER_CRITICAL"])
        if "error during connect" in e.stderr.lower() or "connection refused" in e.stderr.lower():
            print(LANG["TIP_DOCKER_START"])
        else:
            print(LANG["ERROR_DOCKER_DETAIL"].format(e.stderr))
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print(LANG["ERROR_DOCKER_TIMEOUT"])
        sys.exit(1)
    except Exception as e:
        print(LANG["ERROR_DOCKER_UNEXPECTED"].format(e))
        sys.exit(1)
        
def check_pwndoc_status(port):
    """Verifica si el servicio web de Pwndoc está respondiendo."""
    service_url = f"https://localhost:{port}"
    start_time = time.time()
    print(LANG["WAITING_FOR_SERVICE"].format(service_url))
    
    # Pausa inicial para dar tiempo a la base de datos/backend a iniciarse
    print(LANG["INITIAL_WAIT_MSG"].format(INITIAL_WAIT), end="", flush=True)
    time.sleep(INITIAL_WAIT)
    print(LANG["CONTINUE_VERIFY"])
    
    while time.time() - start_time < TIMEOUT_SECONDS:
        try:
            # Deshabilitamos la verificación de SSL ya que usa un certificado autofirmado por defecto
            response = requests.get(service_url, verify=False, timeout=10) 
            
            # Pwndoc debería devolver un 200 para la página de login
            if response.status_code == 200 and "pwndoc" in response.text.lower():
                print(LANG["PWNDOC_OK"])
                print(LANG["ACCESS_URL"].format(service_url))
                return True

            print(f"|", end="", flush=True) # Mostrar progreso
            time.sleep(5)

        except requests.exceptions.ConnectionError:
            print(".", end="", flush=True) # Mostrar progreso
            time.sleep(5)
        except requests.exceptions.Timeout:
            print("T", end="", flush=True) # Mostrar progreso por timeout
            time.sleep(10)
        except requests.exceptions.RequestException as e:
            # Evitar imprimir errores de SSL aquí, ya que el certificado es autofirmado
            if "certificate verify failed" not in str(e):
                print(f"E", end="", flush=True) # Mostrar progreso por error de request
            else:
                print("S", end="", flush=True) # SSL error (esperado)
            time.sleep(5)
            
    print(LANG["PWNDOC_TIMEOUT_FAIL"].format(TIMEOUT_SECONDS))
    return False

def setup_pwndoc_directory():
    """Clona el repositorio si no existe la carpeta 'pwndoc'."""
    # 1. Comprobar si ya estamos en un directorio pwndoc (donde está docker-compose.yml)
    if os.path.exists("docker-compose.yml"):
        return True # Ya estamos en el lugar correcto

    # 2. Si no estamos allí, comprobar si la carpeta pwndoc ya existe en el directorio actual
    if not os.path.isdir(PWNDOC_DIR_NAME):
        print(LANG["DOCKER_COMPOSE_NOT_FOUND"])
        print(LANG["CLONING_REPO"].format(PWNDOC_DIR_NAME))
        
        # Clonar el repositorio
        run_command(["git", "clone", PWNDOC_REPO_URL, PWNDOC_DIR_NAME])
        
        # Mover al nuevo directorio
        os.chdir(PWNDOC_DIR_NAME)
        print(LANG["CHDIR_SUCCESS"].format(os.getcwd()))
        return True
    
    # 3. Si la carpeta existe, mover a ella
    else:
        print(LANG["DIR_FOUND_CHDIR"].format(PWNDOC_DIR_NAME))
        os.chdir(PWNDOC_DIR_NAME)
        print(LANG["CHDIR_SUCCESS"].format(os.getcwd()))
        return True
        
    return False # En caso de error inesperado
    
# --- Funciones de Orquestación ---

def build_and_run():
    """Configura el directorio, construye y levanta los contenedores y verifica el estado."""
    check_docker_daemon()
    
    # Paso Cero: Asegurar que estamos en el directorio correcto
    if not setup_pwndoc_directory():
        print(LANG["SETUP_FAIL"])
        sys.exit(1)
        
    print(LANG["BUILD_AND_RUN_START"])
    command = ["docker-compose", "up", "-d", "--build"]
    
    if run_command(command, check=False):
        # La verificación es crítica, no solo la ejecución del comando
        if check_pwndoc_status(PWNDOC_PORT):
             print(LANG["ORCHESTRATION_SUCCESS"])
             print(LANG["HTTPS_NOTICE"].format(PWNDOC_PORT))
             print(LANG["SECURITY_REMINDER"])
        else:
             print(LANG["VALIDATION_FAILED"])
             # No forzamos la salida aquí, ya que el usuario podría querer debuggear con los contenedores arriba
    else:
        print(LANG["UP_COMMAND_FAILED"])
        sys.exit(1)


def show_logs():
    """Muestra los logs del servicio de backend de pwndoc."""
    print(LANG["SHOWING_LOGS"].format(BACKEND_SERVICE))
    run_command(["docker-compose", "logs", "-f", BACKEND_SERVICE], check=False)


def stop_containers():
    """Detiene los contenedores."""
    print(LANG["STOPPING_CONTAINERS"])
    run_command(["docker-compose", "stop"])

def start_containers():
    """Inicia los contenedores previamente detenidos y verifica el estado."""
    check_docker_daemon()
    print(LANG["STARTING_CONTAINERS"])
    if run_command(["docker-compose", "start"]):
          check_pwndoc_status(PWNDOC_PORT)

def remove_containers():
    """Baja y elimina los contenedores, redes y volúmenes por defecto."""
    print(LANG["REMOVING_CONTAINERS"])
    run_command(["docker-compose", "down"])

def update_application():
    """Detiene, actualiza el código via git pull, y reconstruye/levanta la aplicación."""
    check_docker_daemon()
    
    # Si no estamos en el directorio de pwndoc, no podemos hacer git pull
    if not os.path.exists("docker-compose.yml"):
        print(LANG["UPDATE_CRITICAL_ERROR"])
        print(LANG["UPDATE_TIP"])
        sys.exit(1)
        
    print(LANG["UPDATE_START"])
    
    # 1. Detener
    # Usamos check=False para no salir si ya estaban detenidos
    if run_command(["docker-compose", "down"], check=False).returncode != 0:
        print(LANG["UPDATE_DOWN_WARN"])
        
    # 2. Pull
    print(LANG["UPDATE_GIT_PULL"])
    result = run_command(["git", "pull"], check=False)
    if result is None or result.returncode != 0:
        print(LANG["UPDATE_GIT_PULL_FAIL"])
        return
        
    # 3. Reconstruir y levantar
    print(LANG["UPDATE_BUILD_START"])
    build_and_run()
    print(LANG["UPDATE_COMPLETE"])
    
def main():
    # Usamos .format(PWNDOC_PORT) para la descripción.
    parser = argparse.ArgumentParser(
        description=LANG["PARSER_DESCRIPTION"].format(PWNDOC_PORT),
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("action", choices=[
        "up", 
        "logs", 
        "stop", 
        "start", 
        "down", 
        "update"
    ], help=LANG["PARSER_HELP_ACTIONS"])
    
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    # Mapeo de acciones a funciones
    actions = {
        "up": build_and_run,
        "logs": show_logs,
        "stop": stop_containers,
        "start": start_containers,
        "down": remove_containers,
        "update": update_application,
    }
    
    # Para las acciones que dependen de docker-compose, verificamos si existe la carpeta pwndoc y cambiamos si es necesario.
    if args.action != 'up' and not os.path.exists("docker-compose.yml"):
        
        if os.path.isdir(PWNDOC_DIR_NAME):
            os.chdir(PWNDOC_DIR_NAME)
        else:
            print(LANG["ACTION_PRECHECK_FAIL"])
            print(LANG["ACTION_PRECHECK_TIP"])
            sys.exit(1)
            
    # Ejecutar la acción
    actions[args.action]()

if __name__ == "__main__":
    main()