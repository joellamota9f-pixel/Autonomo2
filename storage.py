def guardar_contraseña(nombre, contraseña):
    with open("contraseñas_guardadas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre}: {contraseña}\n")
