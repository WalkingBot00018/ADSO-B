#Pedir al usuario el color en el que se encuentra el semáforo e imprimir la instrucción correspondiente, 
# si el color no coincide con un semáforo debe solicitar aclaración de dicho dato.

# Pedir al usuario el color del semáforo
color = input('¿Qué color está el semáforo? (Verde, Amarillo, Rojo): ')

# Imprimir la instrucción correspondiente
if color.lower() == 'verde':
    print('Puede cruzar la calle.')
elif color.lower() == 'amarillo':
    print('Prepárese para cruzar la calle.')
elif color.lower() == 'rojo':
    print('No cruce la calle.')
else:
    print('No entendí el color, por favor inténtelo de nuevo.')