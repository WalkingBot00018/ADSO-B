import random

print("Me gusta ser un módulo.")

print(__name__)

#if __name__ == "__main__":
#    print("Yo prefiero ser un módulo")
#else:
#    print("Me gusta ser un módulo")


def area_circulo(radio):
    return 3.14 * (radio ** 2)

"""radio = 9
area = area_circulo(radio)
#print("El área del círculo es:", area)"""


def indice_desempeño(victorias, empates, derrotas):
    total_partidos = victorias + empates + derrotas
    if total_partidos == 0:
        return 0
    indice_desempeño = (victorias * 3 + empates) / total_partidos
    return indice_desempeño

"""victorias = 2
empates = 1
derrotas = 2

indice_desempeño = ruben.indice_desempeño(victorias, empates, derrotas)

print("El índice de desempeño es:", indice_desempeño)"""





def es_electronica(genero):
    if genero == "electronica":
        return True
    else:
        return False

"""genero = "electronica"

es_electronica = es_electronica(genero)

if es_electronica:
    print("La canción es de género electronica")
else:
    print("La canción no es de género electronica")"""


def indice_energia(energia, resistencia):
    return energia / resistencia


"""energia = 5000
resistencia = 100
indice_energia = ruben.indice_energia(energia, resistencia)

print("El índice de energía es:", indice_energia)
"""
