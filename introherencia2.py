
# aqui se define la clase llamada a1
class A1:
    #aqui se define un metodo inigt que va a inicializar el constructor de la clase
    def __init__(self):
        # esta instruccio significa vacio entonces pues no hace nada
        pass
    #aqui se define el metodo llamado saludo 
    def saludo(self):
        #aqui se imprime en la consola el mensaje hola desde a1
        print('Hola desde A1')

# aqui se deine una clase llamada a2
class A2:
    #aqui se crea un metodo init que va a inicializar el constructor de la clase a2
    def __init__(self):
        # esta instruccio significa vacio entonces pues no hace nada
        pass
     #aqui se define el metodo llamado saludo 
    def saludo(self):
         #aqui se imprime en la consola el mensaje hola desde a2
        print('Hola desde A2')

# aqui se crea una clase b y esta tiene unos parametros a1,a2 esto sisgnifica que la clse b hereda de las clases a1,a2
#esto quiere decir que b tiene accseso a todos los atributos y metods de a1,a2
class B(A2,A1):
    #aqui se crea un metodo init que va a inicializar el constructor de la clase b
    def __init__(self):
        # esta instruccio significa vacio entonces pues no hace nada
        pass
    #aqui se define el metodo llamado saludo 
    def saludo(self):
        #aqui se imprime en la consola el mensaje hola desde b
        print('Hola desde B')
    #aqui se define un metodo especial llamado str y esto quiere decir que va a retornar una cadena  de texto que describe el objeto
    def __str__(self):
        #aqui retorna este mensaje
        return 'Soy un objeto de la clase B'
#Estas lineas crean una instancia de la clase B, llamada obj
obj=B()
#aqui se llama al método str de la instancia obj, que retorna la cadena de texto Soy un objeto de la clase B
# Esta cadena de texto se imprime en la consola
print(obj.__str__())
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())