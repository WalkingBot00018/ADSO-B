"""
Escriba una clase Empleado que tenga como propiedades
nombre, cargo, salario
escriba metodos contructores, setters y getters
escriba un método que permita calcular cuanto gana el empleado en una hora
un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide
cada vez que yo cree una varible aumente
"""

class empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def setnombre(self,nombre):
        self.nombre=nombre
    
    def setcargo(self,cargo):
        self.cargo=cargo

    def setsalario(self,salario):
        self.salrio=salario

    def getnombre(self):
        return self.nombre
    
    def getcargo(self):
        return self.cargo
    
    def getsalario(self):
        return self.salario
    
    def salarioporhora(self):
        return (self.salario / 30 )
    
    def  aumento_ipc(self):
        if self.salario == 1160000:
            return (self.salario * 0.16)
        elif self.salario > 1160000:
            return (self.salario *0.13)
        elif self.salario <1160000:
            return "no se puede"
    def salsriohorasextras(self):
        if horasextras>2:
            horasextras=2
        return self.salario +(self.salarioporhora* horasextras * 1.25)
    


ob=empleado('pedro', 'i', 1160000)
print(ob.getsalario())

ob.setsalario(1180000)
print(ob.getsalario())

print(ob.salarioporhora())

print()                
        