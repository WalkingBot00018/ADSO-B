
# en esta es una linea que define una clase llamada curso
class Curso:
    #aqui se usas una funcion y se inicia el constructor de la clase curso
    def __init__(self,titulo):
        #aqui se crea una varibale de instancia llamada titulo esta es privada y este se le asigna el valor 
        #del parametro titulo y este pas por el constructor
        self.__titulo=titulo
    #aqui se define ele metodo getTitulo de la clase curso con el parametro self
    def getTitulo(self):
        #aqui se devuelve el valor de la varible privada titulo
        return self.__titulo
#aqui se define clase aprendiz
class Aprendiz:
    #aqui se crea la funcion y se inicia el constructor de la clse aprendiz
    def __init__(self,nombre):
        #aqui se crea una variable privada llamada nombre y este tiene un parametro llamado nombre
        self.__nombre=nombre
        #aqui se crea una lista vacia llamada cursos  y esta es una variable privada
        self.__cursos=[]
    #aqui se define el metodo agregar curso de la clase aprendiz
    def agregarCurso(self,nombreCursito):
        #aqui se crea una variable de instancia de la clse curso con un parametro nombrecursito y esta en una variable nombre
        cursito=Curso(nombreCursito)
        #aqui se agrega la instancia de la clase curso en la lista de cusrsos en la instancia de aprendiz que es la actual
        self.__cursos.append(cursito)
    # aqui se define el metodo getcursos de la clase aprendiz
    def getCursos(self):
        #aqui se devuelve la lista de cursos de la clase actual aprendiz
        return self.__cursos
#aqui es una instancia de la clase aprendiz que tiene  un parametro sofia y esta en la variable ap   
ap=Aprendiz('Sofia')
# en este se agrega un curso llamado python basico en la lista de cursos de app de la clase aprendiz utlizando el metodo agregarcursos
ap.agregarCurso('Python Basico')
#aqui se agrega un cursoi llamado python intermedio  ene la lista de cursos de la instancia ap de la clase aprendiz utilizando el metodo agregarcurso
ap.agregarCurso('Python Intermedio')
# aqui se itera sobre la lista de cursos  de la intsancia ap de la clase aprendiz
for c in ap.getCursos():
    #aqui se imprime en la consola el titulo de cada curso utilizando el metodo getTitulo de la clase curso
    print(c.getTitulo())