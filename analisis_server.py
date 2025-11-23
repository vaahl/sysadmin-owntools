import os
import shutil
import datetime

# Verificamos el disco raíz porque si se llena al 100%, el servidor Linux deja de responder.

def check_disk_usage(path="/"):

    try: 
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
    except Exception as e:
        print(f'ERROR: NO SE PUDO LEER EL DISCO. REVISAR {e} ')

# 2. Función para ver quién está conectado (comando 'who' de Linux)
def check_active_users():
    print("\n--- Usuarios Conectados ---")
    # Ejecutamos un comando de sistema y leemos la salida

    try:
        users = os.popen('who').read()


        if users:
            print(users)
        else:
            print("No hay usuarios humanos conectados.")
    except Exception as e:
        print(f'ERROR: Fallo en la verificacion de personas conectadas. Revisar: {e}')

# 3. Función principal que orquesta todo y guarda un log
def run_audit():
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Iniciando auditoría del sistema: {fecha_hoy}\n")
    
    check_disk_usage()
    check_active_users()
    
    print("\nAuditoría finalizada.")

if __name__ == "__main__":
    run_audit()