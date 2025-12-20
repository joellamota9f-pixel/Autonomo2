from generator_final import generar_contraseña
from evaluator_final import evaluar_fortaleza
from storage_final import guardar_contraseña
from utils_final import limpiar_pantalla

# Diccionario como estructura de datos
contraseñas = {}

def generar():
    limpiar_pantalla()
    print("-------- CONFIGURACIÓN DE GENERACIÓN --------")

    try:
        longitud = int(input("Longitud de la contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser mayor a 0.")
            return ""
    except ValueError:
        print("Debes ingresar un número válido.")
        return ""

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
    opciones_validas = ["1", "2", "3"]

    while True:
        print("\n-------- MENÚ PRINCIPAL --------")
        print("1. Generar nueva contraseña")
        print("2. Guardar contraseña actual")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion not in opciones_validas:
            print("Opción no válida.")
            continue

        if opcion == "1":
            contraseña_actual = generar()

        elif opcion == "2":
            if contraseña_actual == "":
                print("Primero debes generar una contraseña.")
            else:
                nombre = input("Nombre o etiqueta: ")
                contraseñas[nombre] = contraseña_actual  # Diccionario
                guardar_contraseña(nombre, contraseña_actual)
                print("Contraseña guardada correctamente.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break


menu()

