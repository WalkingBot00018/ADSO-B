#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, 
#luego tres primeras y así sucesivamente hasta llegar a la última

def subcadenas(cadena):
    """
    Imprime todas las subcadenas de una cadena, comenzando con las dos primeras letras,
    luego tres primeras y así sucesivamente hasta llegar a la última.
    """
    n = len(cadena)
    # Recorrer las longitudes de las subcadenas
    for i in range(2, n+1):
        # Recorrer las posiciones de inicio de las subcadenas de longitud i
        for j in range(n-i+1):
            # Imprimir la subcadena de longitud i que comienza en la posición j
            print(cadena[j:j+i])
cadena = "dinosaurio"
subcadenas(cadena)
