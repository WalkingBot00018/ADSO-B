from Industria import *
import csv

empresas=[]
with open('C:\\Users\\palma\\OneDrive\\Documents\\Ivan Palmar\\SENA\\3er Trimestre\\Samuel Padilla\\Repositorio\\ADSO-B-INSTRUCTOR-SAMUEL\\14ava Miscelania (archivos csv)\\empresas.csv') as flujo:
    leer=csv.reader(flujo)
    for i in leer:
        industrias=industria(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        empresas.append(industrias)

for i in empresas:
    print(i.getAll())
    


print('\nAnalisis de datos en Python (Empresas)')
print('')
print('1-Buscar una empresa por su pais, recordando que son empresas de paises de Asia y Oceania')
print('2-Buscar una empresa por el nombre (Asia y Oceania)')
print('3-Buscar empresa por indice, esto mostrara toda la informacion de la empresas (Asia y Oceania)')
print('0-Salir')
menu=int(input('\n¿Que accion deseas realizar?\n-'))
while True:
    match menu:
        case 1:
            print('\nEmpresas Alrededor del Mundo (Asia y Oceania)')
            pais=input('¿De que pais es la empresa que deseas buscar?\n-')
            pais1=pais.capitalize()
            for i in empresas:
                if pais1 in i.getCountry():
                    print('Los datos de la empresa son:',i.getAll())
                    break
        case 2:
            print('\nEmpresas en Asia y Oceania')
            nombre=input('¿Cual es el nombre de la empresa que deseas buscar?\n-')
            nombre1=nombre.capitalize()
            for i in empresas:
                if nombre1 in i.getName():
                    print('Los datos de la empresa son:',i.getIndex(),i.getOrgaId(),i.getName(),i.getCountry(),i.getNEmplo())
                    break
        case 3:
            print('\nEmpresas en Asia y Oceania')
            indice=input('¿Que indice deseas buscar (Un numero)?\n-')
            for i in empresas:
                if indice in i.getIndex():
                    print('Los datos de la empresa son:',i.getAll())
                    break
                
        case 0:
            print('Has decidido salir, espero haya sido de mucha ayuda todo el analisis de los datos.')
            print('Si no ha salido nada en ninguna de las opciones, significa que no hay registros de dicha opcion que elegiste')
            break