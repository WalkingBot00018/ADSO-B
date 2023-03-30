#solicite al usuario capital en pesos,
#intereses y años de inversión y devuelva cual es el interés generado en cada año.


# Solicitar al usuario capital, intereses y años de inversión
capital = float(input('Ingrese el capital: '))
interes = float(input('Ingrese el interés: '))
años = int(input('Ingrese los años de inversión: '))

# Calcular el interés generado por cada año
for i in range(1, años + 1):
    interes_generado = capital * interes
    capital = capital + interes_generado
    print(f'El interés generado en el año {i} es de {interes_generado:0.2f} pesos.')