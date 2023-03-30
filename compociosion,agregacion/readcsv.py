# aqui se Importa todo de la clase Aprendiz
from Aprendiz import *

# aqui inporta la libreria csv
import csv

#  aqui Crea una lista vacia para almacenar los aprendices
listaAprendices = []

#aqui se Abre el archivo csv que contiene los datos de los aprendices
# Aquí se utiliza el with para asegurarse de que el archivo se cierre automáticamente después de que se termine de leer tabien puede ser un bloque
# El archivo se encuentra en la ruta 'C:\Users\usuario\Documentos\01-SENA\NetAcademy2023\2693629.csv'
with open('C:\\Users\\usuario\\Documentos\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:

    #aqui Crea un objeto csvReader que permitirá leer el archivo csv
    csvReader = csv.reader(csvDataFile)

    #aqui Recorre cada fila del archivo csv
    for fila in csvReader:

        # aqui Crea un objeto Aprendiz con los datos de la fila actual
        apr = Aprendiz(fila[0], fila[1], fila[2], fila[3])

        # aqui Agrega el objeto Aprendiz a la lista de aprendices
        listaAprendices.append(apr)

# aqui Imprime la lista de aprendices
print(listaAprendices)

# aqui Recorre la lista de aprendices y para cada uno imprimir su nombre completo
for abr in listaAprendices:
    print(abr.nombreCompleto())