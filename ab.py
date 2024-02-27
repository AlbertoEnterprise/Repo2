import os

def ejecutar_comando():
    # Simulación de entrada del usuario (¡No hagas esto en producción!)
    archivo = input("Introduce el nombre de un archivo: ")

    # Ejecuta un comando usando el valor proporcionado por el usuario
    os.system(f"cat {archivo}")

# Llamamos a la función
ejecutar_comando()
