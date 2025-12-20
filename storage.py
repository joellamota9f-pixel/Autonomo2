def guardar_contraseña(nombre, contraseña):

    with open("contraseñas_guardadas.txt", "a") as archivo:
        archivo.write(f"{nombre}: {contraseña}\n")
