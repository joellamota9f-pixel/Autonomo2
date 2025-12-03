import secrets
import string

def generar_contraseña(longitud, mayus, minus, numeros, simbolos):

    caracteres = ""

    if mayus:
        caracteres += string.ascii_uppercase
    if minus:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    # Política por defecto si no elige nada
    if caracteres == "":
        caracteres = string.ascii_letters + string.digits

    # Generar contraseña segura
    contraseña = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña
