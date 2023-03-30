#Determinar en que tiempo esta conjugado un verbo
def v(verbo):
    # Convertir el verbo a minúsculas
    verbo = verbo.lower()
    # Determinar en qué tiempo está conjugado el verbo
    if verbo.endswith("ar"):
        return "presente"
    elif verbo.endswith("er"):
        return "pasado"
    elif verbo.endswith("ir"):
        return "futuro"
    else:
        return "no se reconoce el tiempo verbal"
# Pedir una palabra o verbo al usuario
palabra = input("Ingresa una palabra: ")

# Determinar el tipo de palabra y el tiempo verbal
if palabra.isalpha():
    tipo = v(palabra)
    tiempo = v(palabra)
    print(f"La palabra es {tipo} y el verbo está conjugado en {tiempo}.")
else:
    print("Error: la entrada debe ser una palabra o verbo.")
