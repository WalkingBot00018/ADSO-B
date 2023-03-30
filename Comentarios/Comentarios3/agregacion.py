class Aprendiz: #Se hace la clase usando la palabra  class y se le asigna su respectivo nombre el cual es Aprendiz.
    def __init__(self,nombre): #Se crea el constructor de la clase Aprendiz el cual lleva en su lista de parametros, el parametro self que es su parametro obligatorio para indicar que el constructor se encuentra en la clase Aprendiz, y un segundo parametro el cual es nombre que seguramente guardara el nombre ingresado por el usuario y que sera un aprendiz.
        self.__nombre=nombre #Se crea una variable de instancia o un atributo que es self.__nombre y que guardara el parametro nombre y su tipo de dato osea el nombre que se le puso al aprendiz cuando se cree un objeto para la clase aprendiz.
        self.__cursos=[] #Se crea un nuevo atributo pero que no se encuentra en los parametros del metodo el cual es self.__cursos y que contiene como dato una lista vacia que seguramente se llenara de cursos.

    def agregarCurso(self,titulo): #Se crea un nuevo metodo para la clase Aprendiz el cual es agregarCurso y que contiene dos parametros, uno que es self el cual es un parametro obligatorio que indica que el metodo se encuentra en la clase, y un segundo parametro que es titulo que seguramente se llenara de los uevos cursos que se agregen.
        self.__cursos.append(titulo)  #Se hace un llamado del atributo self.__cursos y como este atributo es basicamente un lista entonces se usa el metodo de listas '.append' y como argumento se le pasa el parametro titulo que fue creado en la instaciacion del metodo,

    def getCursos(self): #Se crea un nuevo metodo para la clase Aprendiz que lleva como nombre getCursos que servira para retornar un contenido en este caso los cursos que se agregaron en el metodo agregarCurso(), y que contiene como parametro el parametro obligatorio self que indica que esta dentro de la clase Aprendiz.
        return self.__cursos #El return servira para retornar la direccion en memoria del atributo self.__cursos el cual contendra el nombre de los cursos agregados.

class Curso: #Se crea una nueva clase con la palabra  class y que llevara por nombre Curso:
    def __init__(self,titulo): #Se crea el constructor de la clase Curso, que lleva dos parametros, el parametro ya obligatorio self que indica que el constructor se encuentra dentro de la clase, y un segundo parametro que es titulo que contendra el nombre de los cursos.
        self.__titulo=titulo #Se instancia una variable de instancia o un atributo que es self-__titulo y que llevara como contenido el nombre del titulo del curso que se le pase cuando se cree un objeto de la clase Curso

    def getTitulo(self): #Se crea un nuevo metodo que es getTitulo() con su parametro obligatorio self que indicara que esta en la clase Curso.
        return self.__titulo #El return nos servira para retornar lo que se encuetra en el atributo self.__titulo
    
a=Aprendiz('Martha') #Se instancia un objeto para la clase Aprendiz que lleva por nombre 'a' y que en su argumento lleva el nombre 'Martha'.
c1=Curso('Python Intermedio') #Se instancia un objeto para la clase Curso que lleva por nombre 'c1' y que en su argumento lleva el nombre 'Python Intemedio'.
c2=Curso('Python Basico') #Se instancia un objeto para la clase Curso que lleva por nombre 'c2' y que en su argumento lleva el nombre 'Python Basico'.
c3=Curso('Introduccion a Java') #Se instancia un objeto para la clase Curso que lleva por nombre 'c3' y que en su argumento lleva el nombre 'Introduccion a Java'.

a.agregarCurso(c1) #El objeto 'a' llama el metodo agregarCurso y pone el objeto 'c1' que fue instanciado anteriormente para la clase Curso, osea agregar el curso 'Python Intermedio' al aprendiz.
a.agregarCurso(c2)  #El objeto 'a' llama el metodo agregarCurso y pone el objeto 'c2' que fue instanciado anteriormente para la clase Curso, osea agregar el curso 'Python Basico' al aprendiz.
a.agregarCurso(c3)  #El objeto 'a' llama el metodo agregarCurso y pone el objeto 'c3' que fue instanciado anteriormente para la clase Curso, osea agregar el curso 'Instroduccion a Java' al aprendiz.

print(a.getCursos()) #Este imprime el objeto 'a' de la clase aprendiz con el metodo getCursos que envio las cordenadas de dicho metodo y las muestra por pantalla

for curso in a.getCursos(): #El for hara la iteracion para una variable local la cual es 'curso' que iterara el atributo osea la lista que se encuentra como retorno en el metodo getCursos().
    print(curso.getTitulo()) #Y se imprimira curso en la posicion getTitulo() que pertence a la clase Curso y que mostrara en pantalla la impresion de todos los cursos que se agregaron a la aprendiz 'Martha'.      