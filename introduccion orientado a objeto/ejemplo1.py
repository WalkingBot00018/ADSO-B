#aqui en la primera linea de class persona se define una clase llamada persona 
class Persona:
    #esto es una funcion y aqui estamos definiendo un metodo llamado init y este metodo es el iniciante o contructor de una clase
    #este tiene dos parametros self y nombre , self es una referencia al objeto y el nombre es como un argumento
    def __init__(self,nombre):
        #aqui en la linea7 se le asigna el valor del argumento nombre 
        #aqui el nombre tiene dos guiones abajo esto significa que este atributo es privado y no se puede acceder o modificar
        self.__nombre=nombre
        # aqui pues basicamente imprime en la consola el mensaje 
        print('Activando constructor')

#en esta linea definimos un metodo getnombre que tiene un parametro self
    def getNombre(self):
        #aqui en esta linea lo que hace es devolver el metodo privado nombre del objeto actual
        return self.__nombre
    
#aqui se define una funcion llamada setnombre que tien dos parametros self y nombre
    def setNombre(self, nombre):
        #aqui en la linea7 se le asigna el valor del argumento nombre 
        #aqui el nombre tiene dos guiones abajo esto significa que este atributo es privado y no se puede acceder o modificar
        self.__nombre=nombre

#aqui se define una funcion llamada metyodo y tiene un parametro llamado self y este hace referncia al al objete que se esta utilizando actualmente
    def metodo(self):
        #aqui no mas inprime en la consola el mensaje 
        print('Soy un método')

#se crea una instancia clase Persona y se asigna a la variable ob, y el parametro que tiene el mensaje ana este pasa por el constructor
# de la clase 
ob=Persona('Ana')
#aqui se llama al metodo getnombre  de la instancia ob de la clase persona y este metodod devuelve el valor actual del atributo
print(ob.getNombre())
#En esta línea, se llama al metodo setnombre de la instancia ob de la clase Persona. Este método actualiza el valor del atributo nombre 
ob.setNombre('Maria')
#En esta línea, se llama nuevamente al método getNombre() de la instancia ob de la clase Persona.
#como ya se habia actualizado el atributo  nombre, entonces este metodo devuelve el valor actualizado mas reciente que en este caso es maria
print(ob.getNombre())
#ob.metodo()
#print(type(ob))