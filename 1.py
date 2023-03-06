class registro:
    def __init__(self, nombre, edad,genero, telefono,usuario,contraseña):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.telefono=telefono
        self.usuario=usuario
        self.contraseña=contraseña
    def getnombre(self):
        return f"nombre:{self.nombre}"
    
    def getedad(self):
        return f"edad: {self.edad}"
    
    def getgenero(self):
        return f"genero: {self.genero}"
    
    def gettelefono(self):
        return f"Telefono: {self.telefono}"
    

class estudiante:
    def __init__(self,cursos):
        self.cursos=cursos
    
    def getcurs(self):
        return f"curso: {self.curso}"
    
    
    
