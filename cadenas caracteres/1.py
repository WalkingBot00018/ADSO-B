# Cuantas letras del abecedario estan en la cadena, 
# si estan repetidas cuentela solo una vez

def contar_letras(cadena):
    # Convertir la cadena a minúsculas
    cadena = cadena.lower()
    # Inicializar un conjunto vacío para almacenar las letras únicas
    letras_unicas = set()
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        # Si el carácter es una letra del alfabeto, agregarla al conjunto de letras únicas
        if caracter.isalpha():
            letras_unicas.add(caracter)
    # Devolver el tamaño del conjunto de letras únicas
    return len(letras_unicas)
cadena = "BBuenos diass"
resultado = contar_letras(cadena)
print("Hay", resultado, "letras del alfabeto en la cadena.")
