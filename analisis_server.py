import os
import shutil
import datetime

# 1. Función para chequear espacio en disco
def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    
    print(f"--- Auditoría de Disco: {path} ---")
    print(f"Total: {total // (2**30)} GB")
    print(f"Usado: {used // (2**30)} GB")
    print(f"Libre: {free // (2**30)} GB")
    print(f"Porcentaje de uso: {percent_used:.2f}%")
    
    if percent_used > 80:
        print("ALERTA: ¡Espacio crítico! Revisa el servidor.")
    else:
        print("Estado: Saludable.")

# 2. Función para ver quién está conectado (comando 'who' de Linux)
def check_active_users():
    print("\n--- Usuarios Conectados ---")
    # Ejecutamos un comando de sistema y leemos la salida
    users = os.popen('who').read()
    if users:
        print(users)
    else:
        print("No hay usuarios humanos conectados.")

# 3. Función principal que orquesta todo y guarda un log
def run_audit():
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Iniciando auditoría del sistema: {fecha_hoy}\n")
    
    check_disk_usage()
    check_active_users()
    
    print("\nAuditoría finalizada.")

if __name__ == "__main__":
    run_audit()