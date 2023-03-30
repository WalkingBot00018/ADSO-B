# Invente un cifrado de texto tipo murcielago o César. 
# Puede utilizar alguna formula matemática para este fin.

diccionario = {
    "a": "m",
    "b": "u",
    "c": "r",
    "d": "c",
    "e": "i",
    "f": "e",
    "g": "l",
    "h": "a",
    "i": "g",
    "j": "o",
    "k": " ",
    "l": "b",
    "m": "f",
    "n": "z",
    "ñ": "n",
    "o": "j",
    "p": "s",
    "q": "d",
    "r": "p",
    "s": "y",
    "t": "h",
    "u": "t",
    "v": "q",
    "w": " ",
    "x": "k",
    "y": "v",
    "z": "w"
}
def cifrar_murcielago(texto):
    texto_cifrado = ""
    for letra in texto.lower():
        if letra in diccionario:
            texto_cifrado += diccionario[letra]
        else:
            texto_cifrado += letra
    return texto_cifrado
texto_original = "mama"
texto_cifrado = cifrar_murcielago(texto_original)
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)

