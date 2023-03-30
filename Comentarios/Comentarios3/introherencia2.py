class A1: #Se hace uso de la palabra class para crear una clase, el nombre de esya clase sera A1 y finalemente se cierra con dos puntos.
    def __init__(self): #Se crea el constructor de la clase con su sintaxis def despues __init__ que basicamente es una palabra reservada o una isntruccion para el constructor, y en su lista de parametros se pone el parametro obligatorio self que indica que se encuentra en dicha clase.
        pass #Se usa la palabra reservada pass que hace referencia a que el constructor no tendra variables de instacias o propiedades en si, si no que sera un constructor vacio.
    def saludo(self): #Se crea un metodo llamado saludo, que se usara para explicar la herencia o polimorfismo, y este tiene su respectivo parametro obligatorio self para indicar que el metodo se encuentra en la clase correspondiente.
        print('Hola desde A1') #Se le asigna una impresion al metodo saludo el cual si se llama imprimira 'Hola desde A1'.

class A2: #Se crea una segunda clase usando la palabra class y se le asigna su nombre correspondiente el cual en este caso sera A2.
    def __init__(self): #Se crea el constructor de la clase A2 con su respectivo parametro obligatorio self el cual indicara que el constructor esta dentro de la clase A2
        pass #Se hace uso de la palabra reservada pass para indicar que el constructor de la clase no contendra propiedades o atributos, lo cual quiere decir que esta palabra se usa para indicar que una clase o un metodo estaran vacios.
    def saludo(self): #Se crea un metodo para la clase A2 el cual tendra como nombre nuevamente saludo al igual que en la clase A1, y en este caso el metodo en su lista de parametros solo contiene el paramentro obligatorio self para indicar que se encuentra en la clase A2.
        print('Hola desde A2') #Si se isntancia un objeto de esta clase o de alguna clase hija y se hace un llamado de este metodo, lo que se mostrara por consola sera lo siguiente 'Hola desde A2'.


class B(A2,A1): #Se crea una nueva clase llamada B la cual en su lista de parametros tiene dos clases que son A2 y A1 lo que quiere decir que la clase B es una clase hija o subclase, y sus clase padre son la clase A1 y la clase A2, esto tambien quiere decir que la clases B heredara todos los metodos o propiedades de dichas clases haciendolos 'propios'.
    def __init__(self):#En esta parte se crea o instancia el constructor de la clase B el cual en su lista de parametros solo contiene el parametro obligatorio self que se usa para indicar que el constructor estara dentro de la clase B.
        pass #Aqui se usa la palabra  pass que indicara que el constructor no tendra propiedades o atributos, esto quiere decir que sera un metodo o un constructor vacio.
    def saludo(self): #Creamos el metodo saludo nuevamente como en las clases A1 y A2, con su respectivo parametro obligatorio self el cual nos indicara que el metodo se encuentra dentro de la clase B.
        print('Hola desde B') #Un print el cual imprimira 'Hola desde B', claramente si se hace llamado de dicho parametro.
    def __str__(self): #Un metodo llamado __str__ el cual por su nombre indica que se retornara o imprimira un mensaje ya que si no se hace esto, pues simplemente cuando se llame este metodo pues el indicara unas cordenadas del objeto en memoria, obviamente en su lista de parametros se encuentra el parametro obligatorio self, que sirve para indicar que se encuentra en la clase B.
        return 'Soy un objeto de la clase B' #Si se hace el llamado del metodo __str__ este retornara un mensaje que dira 'Soy un objeto de la clase B'.
obj=B() #En este apartado se instancia un objeto de la clase B llamado ob.
print(obj.__str__()) #Se hace un print del objeto anteriormente instanciado y se llama el metodo __str__ del mismo, esto indicara o mostrara por consola el mensaje 'Soy un objeto de la clase B'.
#obj.saludo() #En esta parte se trata de explicar el polimorfismo, se llama el metodo saludo del objeto anteriormente instanciado, es un objeto de la clase B pero la clase B tiene con super clases a la clase A1 y a la clase A2, lo que quiere decir que la sobreescritura de metodos podria darse en el codgio, pero aqui simplemente se imprimira 'Hola desde B' ya que el metodo llamado se encuentra en b, si esto no fuera asi entonces el llamado se buscaria en la clases padre y muy posiblemente imprimiria 'Hola desde A1' o 'Hola desde A2'.

