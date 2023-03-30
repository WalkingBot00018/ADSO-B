 #Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. 
 #Cual es el valor numerico de acuerdo a los códigos del alfabeto
def frase(cadena):
    # Inicializar la variable para el valor numerico
    sum = 0
    # Iterar sobre cada carácter en la cadena
    for i in cadena:
        # Obtener el valor del código ASCII del carácter y sumarlo al valor numerico
        sum += ord(i)
    # Devolver el valor numerico
    return sum
cadena = input("Ingresa una cadena: ")
i = frase(cadena)
print("la frase de la cadena es:", i)
