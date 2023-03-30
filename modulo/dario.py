import ruben


radio = 9
area = ruben.area_circulo(radio)
print("El área del círculo es:", area)

#from ruben import *
#radio = 6
#area = area_circulo(radio)
#print("El área del círculo es:", area)


victorias = 2
empates = 1
derrotas = 2

indice_desempeño = ruben.indice_desempeño(victorias, empates, derrotas)

print("El índice de desempeño es:", indice_desempeño)




genero = "electronica"

es_electronica = ruben.es_electronica(genero)

if es_electronica:
    print("La canción es de género electronica")
else:
    print("La canción no es de género electronica")



energia = 5000
resistencia = 100
indice_energia = ruben.indice_energia(energia, resistencia)

print("El índice de energía es:", indice_energia)







