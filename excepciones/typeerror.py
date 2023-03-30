def multipli():
    try:
        a=int(input('ingrese numero: '))
        b=int(input('ingrese un numero: '))
        operacion= a//b
        return operacion
    except TypeError:
        print('esta mal ejecutado')
print(multipli())
print(multipli())