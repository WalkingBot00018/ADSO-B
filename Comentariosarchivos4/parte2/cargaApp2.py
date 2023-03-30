from Conductor import * #Se usa la palabra reservada from para indicar que archivo se va a importar en este caso es el archivo Conductor, despues se usa la palabra reservada import que se utiliza para saber que se va a importar de dicho archivo esto se refiere que se va a importar todo del archivo Conductor.
from Carga import * #Se usa la palabra reservada from para indicar que archivo se va a importar en este caso es el archivo Carga, despues se usa la palabra reservada import que se utiliza para saber que se va a importar de dicho archivo esto se refiere que se va a importar todo del archivo Carga.
lista=[] #Se crea una variable local que se llama 'lista', y su contenido es una lista vacia.

with open('C:\\Users\\lozano\\OneDrive\\Documents\\ruben lozano\\SENA\\3er Trimestre\\Samuel Padilla\\Repositorio\\ADSO-B\\Comentarios\\Comentariosarchivos4\\Parte2\\basico.txt','r') as flujo: #Aqui se hace uso de la palabra reservada with que sera la que ayude a manipular el archivo con su bloque de codigo, despues de with viene la palabra tambien reservada open() que se usa para abrir un archivo en su lista de parametros tiene la ruta del archivo que ya fue indica de forma absoluta y de segundo parametro contiene lo que se desea hacer con el archivo ya sea agregar, crear el archivo, escribir en el archivo o leer el archivo, como en este caso esta la r entonces se leera el contenido del archivo, despues de esto viene as que es para poner un alias al archivo y su alias en este caso sera flujo.
    for ob in flujo: #Se usa la estructura de iteracion for que es un ciclo, despues una variable local(ob) que recorrera flujo osea el contenido del archivo y lo recorrera linea por linea.
        lista.append(ob) #Aqui se hace llamado de la lista vacia (lista) que se creo anteriormente con su metodo append que sirve para agregar cosas dentro de la lista pero esta lista pide un parametro, en este caso se le pasa la variable ob para que la agrege a la lista vacia.
i=0 #Se crea una variable local la cual es i que contiene un numero entero con el valor 0. 
for ob in lista: #Se usa otra estructura de control que iterara o recorrera el archivo y esto quedara guardado en la varaible ob que sera la que recorrera todo el contenido.
    lista[i]=ob.rstrip() #Despues de la iteracion a la lista se pone una posicion la cual sera i osea la variable anteriormente instanciada, que sera igual al recorrido de ob pero con el metodo para cadenas rstrip() que borra todos los caracteres especiales que no sean numeros o letras.
    i+=1 #En este caso se llama la variable i que fue creada anteriormente y que empezaba en cero pero ahora esta variable se ira sumando 1 cada vez que se repita el ciclo.
print(lista) #Con este print simplemente se imprime la lista ya completamente llena de datos y sin caracteres especiales.
lautos=[] #Se instancia otra variable nueva que es lautos que como contenido tiene una lista vacia para ser rellenada o agrega o sustraer datos.
for ob in lista: #Se usa una estructura de control o un ciclo for con una variable local que sera ob, pero este for servira para recorrer la lista; lista.
    lautos.append(ob.split(',')) #Aqui en lautos que aun no contiene ningun dato, se llama con su metodo append que sirve para agregar cosas a la lista, en este caso se agregara la variable ob que fue la que recorrio lista pero con ell metodo split(',') que sirve para partir la lista en diferentes palabras pasandole un caracter especial por el cual se empezara am partir dicha lista.
cargas=[] #Se crea una nueva variable que sera cargas y contendra nuevamente una lista vacia.
print(lautos) #Aqui con el uso de print, se imprimira y se mostrara por consola el contenido del lista lautos.
for i in range(len(lautos)): #Se crea un nuevo for con una variable local i pero ya no serivra para recorrer una lista, en este caso recorrera la desde 0 hasta la longitud de la lista lautos en este caso 3 pero se cuenta hasta 2 osea desde 0 hasta 2.
    p=lautos[i][0] #Se crea una variable local llamada p que contendra lautos en la posicion i en la posicion 0 osea cada vez que se repita el ciclo recorrera una la lista pero solo mostrara el primer dato de la lista lautos.
    n=lautos[i][1] #Se crea una variable local llamada n que contendra lautos en la posicion i en la posicion 1 osea cada vez que se repita el ciclo recorrera una la lista pero solo mostrara el segundo dato de la lista lautos.
    d=lautos[i][2] #Se crea una variable local llamada d que contendra lautos en la posicion i en la posicion 2 osea cada vez que se repita el ciclo recorrera una la lista pero solo mostrara el tercer dato de la lista lautos.
    c=lautos[i][3] #Se crea una variable local llamada c que contendra lautos en la posicion i en la posicion 3 osea cada vez que se repita el ciclo recorrera una la lista pero solo mostrara el cuarto dato de la lista lautos.
    e=lautos[i][4]  #Se crea una variable local llamada e que contendra lautos en la posicion i en la posicion 4 osea cada vez que se repita el ciclo recorrera una la lista pero solo mostrara el quinto dato de la lista lautos.
    con=Conductor(n,d) #Se instancia un nuevo objeto para la clase conductor que llevara por nombre 'con' y por parametro tendra n y d osea se creara 3 nuevos objetos ya que esta accion se hara cada vez que se repita el ciclo.
    obj=Carga(p,con,c,e) #Se instancia un nuevo objeto para la calse Carga que llevara por nombre 'Carga' y piden cuatro parametros, que seran p que basicamente sera placa, despues como segundo parametro se le pasara el objeto con, despues como terecer parametro se le pasara c que es basicamente la capacidad en toneladas que puede cargar el vehiculo, y como ultimo parametro se le pasara e que seran los ejes de la maquinaria.
    cargas.append(obj) #Y aqui se llama la lista cargas pero con su metodo append y como parametro para que agrege a la lista cargas se le pasa el objeto obj osea el objeto de Carga.
print(cargas) #En este print se imprimira la direccion de los objetos creados en memoria.