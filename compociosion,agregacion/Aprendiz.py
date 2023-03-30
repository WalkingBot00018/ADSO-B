# aqui se Define la clase Aprendiz
class Aprendiz:
    
    # aqui se Define el metodo constructor para la clase
    def __init__(self, fname, lname, email, id):
        
        # aqui se establece los atributos de la clase a partir de los argumentos de entrada
        self.__fnombre = fname
        self.__nombre = lname
        self.__correoElectronico = email
        self.__identificacion = id
    
    # aqui Define un metodo para obtener el nombre completo del aprendiz
    def nombreCompleto(self):
        
        # aqui Combina el primer nombre y el apellido del aprendiz y devolver el resultado
        return self.__fnombre + ' ' + self.__nombre