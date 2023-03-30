#Detetrminar que tipo de palabra es: 
#aguda, grave, esdrujula sobre esdrujula

def tipo_palabra(palabra):
    # Convertir la palabra a minúsculas
    palabra = palabra.lower()
    # Contar las sílabas de la palabra
    if palabra.endswith("ión") or palabra.endswith("tico") or palabra.endswith("grafía"):
        # Si la palabra termina en "ión", "tico" o "grafía", es esdrújula
        return "esdrújula"
    elif palabra.endswith("n") or palabra.endswith("s") or palabra.endswith("vocal"):
        # Si la palabra termina en "n", "s" o vocal, es grave
        return "grave"
    else:
        # En otro caso, es aguda
        return "aguda"
# Pedir una palabra al usuario
palabra = input("Ingresa una palabra: ")

# Llamar a la función tipo_palabra() para determinar el tipo de palabra
tipo = tipo_palabra(palabra)

# Imprimir el resultado
print(f"La palabra es {tipo}.")

