import os
import subprocess


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(f"El archivo {ruta_script} no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {ruta_script}: {e}")
        return None


def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código {ruta_script}: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el archivo dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Se modifican las rutas de SEMANA_2 y SEMANA_3 a rutas absolutas
    semanas = {
        '2': os.path.join(ruta_base, '..', 'SEMANA_2'),  # Subir un directorio con '..'
        '3': os.path.join(ruta_base, '..', 'SEMANA_3')  # Subir un directorio con '..'
    }

    while True:
        print("\nMenú Principal - Dashboard")
        # Imprime solo los nombres de las semanas
        for key in semanas:
            print(f"{key} - SEMANA_{key}")
        print("0 - Salir")

        eleccion_semana = input("Elige una semana o '0' para salir: ")
        if eleccion_semana == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_semana in semanas:
            ruta_semana = semanas[eleccion_semana]
            if os.path.exists(ruta_semana):  # Verificamos si la carpeta existe
                mostrar_sub_menu(ruta_semana)
            else:
                print(f"La carpeta SEMANA_{eleccion_semana} no existe.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_semana):
    # Verifica si la carpeta existe antes de proceder
    sub_carpetas = [f.name for f in os.scandir(ruta_semana) if f.is_dir()]

    if not sub_carpetas:
        print(f"No se encontraron subcarpetas en {ruta_semana}.")
        return

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        # Imprime las subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_semana, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_scripts(ruta_sub_carpeta):
    # Verifica si la carpeta tiene scripts Python
    if not os.path.exists(ruta_sub_carpeta):
        print(f"La carpeta {ruta_sub_carpeta} no existe.")
        return

    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    if not scripts:
        print(f"No se encontraron scripts Python en {ruta_sub_carpeta}.")
        return

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")
        # Imprime los scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return  # Regresar al menú principal
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida. Regresando al menú de scripts.")
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()