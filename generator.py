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

    # Política por defecto
    if caracteres == "":
        caracteres = string.ascii_letters + string.digits

    contraseña = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña
