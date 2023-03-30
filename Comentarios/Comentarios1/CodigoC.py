def try_syntax(numerator, denominator): #Se crea una funcion try_syntax con dos argumentos numerator, denominator.
    try: #Se hace uso del try la cual mirara el siguiente  codigo.
        print(f'In the try block: {numerator}/{denominator}') #Se imprime con el metodo f un mensaje y ambos argumentos ya puestos por el usuario en manera de division.
        result = numerator / denominator #Aqui se declara una variable  llamada result que tiene ambos argumentos de la funcion ya realizando su respectiva division.
    except ZeroDivisionError as zde: #Aqui a continuacion del bloque de codigo try se declara except con su error ZeroDivisionError el error que mas posibilidades tiene de salir y con un alias con el cual indentificaremos el error(zde).
        print(zde) #Si el codigo falla y ejecuta la instruccion except entonces en esta parte se imprimira dicho error(ZeroDivisionError).
    else: #Aqui se pone una condicion else esto quiere decir que si el programa no tuvo el error predispuesto en el except entonces ejecutara esta parte del codigo.
        print('The result is:', result) #Aqui se imprimira un mensaje y el resultado de la division si no hubo errores.
        return result #Este return ocurrira al final de todo el bloque except y si no hay errores en el codigo pues retornara el resultado de la division(result).
    finally: #Finally basicamente nos servira en esta parte del codigo para imprimir un mensaje ya sea que hallan habido errores o no.
        print('Exiting') #Este mensaje se imprimira en la terminal asi sea que existe un error o no existe en el codigo.
print(try_syntax(11, 0)) #Por ultimo se imprime la funcion con sus respectivos parametros en este caso 11 y 0, y se evaluara si con esos parametros el codigo sera tomado como un error o hara su proceso normalmente.