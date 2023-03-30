
class Curso: #Se crea una clase con la palabra  class y se le asigna su respectivo nombre el cual sera 'Curso'.
    def __init__(self,titulo): #Se realiza la construccion del constructor de la clase, con sus respectivos parametros, el primero el conocido self que indicar que el constructor se encuentra en la clase, y un segundo parametro el cual indicara el nombre del curso correspondiente y este se le pedira al usuario.
        self.__titulo=titulo #Se crea una varaible de instancia o un atributo que se llamara self.__titulo el cual tendra como valor o contendra el parametro titulo, esto quiere decir que cuando el usuario ingrese el nombre del curso este se guardara aqui.

    def getTitulo(self): #Se crea un nuevio metodo para la clase Curso el cual tendra como nombre getTitulo, por lo general los get sirve para ver el contenido guardado en una variable del constructor o un atributo del mismo, en este caso este metodo tiene como parametro el parametro obligatotio self el cual indica que el metodo se estara dentro de la clase.
        return self.__titulo #En esta parte si hace un llamado de este metodo, retornara el atributo self.titulo esto quiere decir que retornara el nombre del curso que se le paso cuando se hizo la isntanciacion del objeto para la clase curso.

class Aprendiz: #Se crea una nueva clase con la palabra class la cual llevara como nombre Aprendiz.
    def __init__(self,nombre): #Creamos el constructor de dicha clase con dos parametros, simepre el parametro obligatorio self que indicara que el constructor hace parte de la clase Aprendiz, y un segundo parametro que sera 'nombre' y este le pedira al usuario o programador que indique el nombre de un aprendiz.
        self.__nombre=nombre #Una varaible de instancia o atributo que sera self.__nombre que sera la cual contendra el nombre que ingrese el usuario y lo guardara en un espacio de memoria dentro del computador.
        self.__cursos=[] #Se crea un atributo nuevo que no esta en la lista de parametros pero contendra una lista vacia, que seguramente servira para llenarla de cursos para el aprendiz.

    def agregarCurso(self,nombreCursito): #Se crea un metodo nuevo que lleva por nombre 'agregarCurso', en su lista de parametros se encuentra self el cual nos indica que el constructor se encuentra dentro de la clase Aprendiz, y como segundo parametro tiene a 'nombreCursito' que le pedira al usuario cuando se llame el metodo que ingrese el nombre de un curso que cursara o esta cursando.
        cursito=Curso(nombreCursito) #Se instancia un nuevo objeto que pertenecera a la clase Curso pero que lleva dentro uno de los parametros que es 'nombreCursito', con el cual se hara uso de los metodos de curso pero sin haber ninguna herencia.
        self.__cursos.append(cursito) #Ya que el atributo self.__cursos es una lista entonces se usa el metodo de lista '.append' y se le pasa como argumento el objeto cursito, esto quiere decir que la clase Curso estara dentro de un metodo y aparte que el objeto 'cursito' se agregara al atributo self.__cursos el cual es una lista.

    def getCursos(self): #Aqui se hace la creacion de un metodo get que sirve para mostrar el atributo que uno desee, en este caso este metodo lleva por nombre getCursos y como parametro obligatorio lleva self el cual indica que el metodo se encuentra dentro de la clase Aprendiz.
        return self.__cursos #El return serivira para retorna el atributo self.__cursos, pero como este atributo es una lista entonces este metodo dira el que parte de la memtoria se encuentra dicho atributo.
    
ap=Aprendiz('Sofia') #Se instancia un objeto que se llama 'ap' para la clase Aprendiz que lleva como argumento el nombre 'Sofia'.
ap.agregarCurso('Python Basico') #Se hace el llamado del metodo agregarCurso para el objeto 'ap' y se le pone como argumento el nombre de un curso el cual es 'Python Basico'.
ap.agregarCurso('Python Intermedio') #Se hace el llamado del metodo agregarCurso para el objeto 'ap' y se le pone como argumento el nombre de un curso el cual es 'Python Intermedio'.

for c in ap.getCursos(): #El for hara la iteracion para una variable local la cual es 'c' que iterara el atributo osea la lista que se encuentra como retorno en el metodo getCursos().
    print(c.getTitulo()) #Y se imprimira c en la posicion getTitulo() que pertence a la clase Curso y que mostrara en pantalla la impresion de todos los cursos que se agregaron a la aprendiz 'Sofia'.      