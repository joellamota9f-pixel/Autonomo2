def evaluar_fortaleza(contraseña):

    puntaje = 0

    if len(contraseña) >= 8:
        puntaje += 1
    if any(c.isupper() for c in contraseña):
        puntaje += 1
    if any(c.islower() for c in contraseña):
        puntaje += 1
    if any(c.isdigit() for c in contraseña):
        puntaje += 1
    if any(c in "!@#$%&*()-_=+;:,.?" for c in contraseña):
        puntaje += 1

    if puntaje <= 2:
        return "Débil"
    elif puntaje == 3:
        return "Media"
    else:
        return "Fuerte"
