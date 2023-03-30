# Invente un cifrado de texto tipo murcielago o César. 
# Puede utilizar alguna formula matemática para este fin.

def cifrado_cesar(mensaje, clave):
    """
    Cifra el mensaje utilizando el cifrado César con la clave dada.
    """
    # Convertir el mensaje a mayúsculas
    mensaje = mensaje.upper()
    # Inicializar la cadena cifrada
    cifrado = ""
    # Recorrer cada carácter del mensaje
    for caracter in mensaje:
        # Si el carácter es una letra
        if caracter.isalpha():
            # Calcular el desplazamiento según la clave
            desplazamiento = clave % 26
            # Convertir el carácter a su valor ASCII
            ascii_caracter = ord(caracter)
            # Aplicar el desplazamiento al valor ASCII
            ascii_cifrado = ascii_caracter + desplazamiento
            # Si el carácter cifrado se sale del rango de letras mayúsculas,
            # volver al principio del alfabeto
            if ascii_cifrado > ord('Z'):
                ascii_cifrado -= 26
            # Convertir el valor ASCII cifrado a su carácter correspondiente
            caracter_cifrado = chr(ascii_cifrado)
        else:
            # Si el carácter no es una letra, dejarlo sin cifrar
            caracter_cifrado = caracter
        # Agregar el carácter cifrado a la cadena cifrada
        cifrado += caracter_cifrado
    # Devolver la cadena cifrada
    return cifrado
mensaje = "papa"
clave = 3
mensaje_cifrado = cifrado_cesar(mensaje, clave)
print(mensaje_cifrado)  # MROD
