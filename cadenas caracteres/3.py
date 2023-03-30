#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas 
#y minusculas

def imprimir_combinaciones(cadena, combinacion=""):
    # Si ya se han generado todas las combinaciones, imprimir la última
    if len(cadena) == 0:
        print(combinacion)
    else:
        # Generar todas las combinaciones recursivamente
        imprimir_combinaciones(cadena[1:], combinacion + cadena[0].upper())
        imprimir_combinaciones(cadena[1:], combinacion + cadena[0].lower())
cadena = input("Ingresa una cadena: ")
print("Todas las combinaciones posibles son:")
imprimir_combinaciones(cadena)
