#De una cadena diga cuantas vocales tiene, cuantas consonantes, 
# cuantas vocales con tilde y cuantos caracteres especiales.

def contar_caracteres(cadena):
    # Definir listas de vocales y caracteres especiales
    vocales = ["a", "e", "i", "o", "u"]
    tildes = ["á", "é", "í", "ó", "ú"]
    especiales = [" ", ".", ",", ";", ":", "-", "_", "(", ")", "[", "]", "{", "}", "!", "?", "'", "\""]

    # Inicializar contadores
    num_vocales = 0
    num_consonantes = 0
    num_tildes = 0
    num_especiales = 0

    # Contar las vocales, consonantes, vocales con tilde y caracteres especiales
    for letra in cadena:
        if letra.lower() in vocales:
            num_vocales += 1
            if letra in tildes:
                num_tildes += 1
        elif letra.isalpha():
            num_consonantes += 1
        elif letra in especiales:
            num_especiales += 1

    # Devolver los resultados
    return num_vocales, num_consonantes, num_tildes, num_especiales
# Pedir al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Contar los caracteres de la cadena
num_vocales, num_consonantes, num_tildes, num_especiales = contar_caracteres(cadena)

# Imprimir los resultados
print(f"La cadena tiene {num_vocales} vocales, {num_consonantes} consonantes, {num_tildes} vocales con tilde y {num_especiales} caracteres especiales.")
