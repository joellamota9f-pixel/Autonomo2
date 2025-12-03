from generator import generar_contraseña
from evaluator import evaluar_fortaleza
from storage import guardar_contraseña

def generar():
    print("\n=== CONFIGURACIÓN DE GENERACIÓN ===")

    longitud = int(input("Longitud: "))
    mayus = input("Incluir mayúsculas? (s/n): ").lower() == "s"
    minus = input("Incluir minúsculas? (s/n): ").lower() == "s"
    numeros = input("Incluir números? (s/n): ").lower() == "s"
    simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

    contraseña = generar_contraseña(longitud, mayus, minus, numeros, simbolos)
    fortaleza = evaluar_fortaleza(contraseña)

    print("\nContraseña generada:", contraseña)
    print("Fortaleza:", fortaleza)

    return contraseña


def menu():

    contraseña_actual = ""

    while True:
        print("\n===== GENERADOR SEGURO DE CONTRASEÑAS =====")
        print("1. Generar nueva contraseña")
        print("2. Guardar contraseña actual")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            contraseña_actual = generar()

        elif opcion == "2":
            if contraseña_actual == "":
                print("Primero debes generar una contraseña.")
            else:
                nombre = input("Nombre o etiqueta para guardar: ")
                guardar_contraseña(nombre, contraseña_actual)
                print("Contraseña guardada correctamente.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


menu()
