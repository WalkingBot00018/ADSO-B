#aqui se define la calse aprendiz
class Aprendiz:
    #aqui se usas una funcion y se inicia el constructor de la clase aprendiz con un parametro nombre
    def __init__(self,nombre):
        # aqui se crea una variable de instancia privada llamada nnombre 
        self.__nombre=nombre
        #aqui se crea una lista vacia llamada cursos  y esta es una variable privada
        self.__cursos=[]
    #se define un metodo llamado agregarcurso que tiene un parametro titulo 
    def agregarCurso(self,titulo):
        #aqui se agrega en titulo la lista  de cursos de la instancia actual
        self.__cursos.append(titulo)
    #se define el metodo getcursos
    def getCursos(self):
        #aqui devuelve la lista de los cursos de la lista actual
        return self.__cursos
# aqui se define una clase llamada curso
class Curso:
    #aqui se inicia un constructo con init que tiene un parametro titulo
    def __init__(self,titulo):
        #aqui se crea una variable de instacia llamada titulo
        self.__titulo=titulo
    #aqui se define el metodo get curso
    def getTitulo(self):
        # aqui devueleve el titulo del curso
        return self.__titulo
#se crea variable de instancia de la clse aprendiz llamada a que tiene un nombre martha    
a=Aprendiz('Martha')
#aqui se crea trez variables de instancia para la clase aprendiz llamadas c1,c2,c3 y estos tiene como parametros un mensaje de cadena
c1=Curso('Python Intermedio')
c2=Curso('Python Basico')
c3=Curso('Introduccion a Java')
#aqui se agregan los tres objetos de curso a la lista de cursos de la instancia a utilizando el metodo agregarCurso
a.agregarCurso(c1)
a.agregarCurso(c2)
a.agregarCurso(c3)
#Se imprime la lista de cursos de la instancia a utilizando el metodo getCursos
print(a.getCursos())

#Se itera sobre la lista de cursos de la instancia a utilizando un ciclo for, 
# y se imprime el título de cada curso utilizando el método getTitulo de la clase Curso
for curso in a.getCursos():
    print(curso.getTitulo())