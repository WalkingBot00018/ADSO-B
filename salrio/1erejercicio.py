#Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario
#escriba metodos contructores, setters y getters.
#escriba un método que permita calcular cuanto gana el empleado en una hora
#Un método para saber cuanto recibe de incremento si el salario sube con el IPC.
#Si gana el mínimo se le aumenta el ipc + 3% 
#Un método que reciba una cantidad de horas extras y calcule el salario 
#incementando las extras. No puede hacer mas de dos horas diarias y trabaja de 
#lunes a viernes. Valide 

class empleado:
    s=0
    def __init__(self, nombre, cargo, salario,extras):
            self.__nombre=nombre
            self.__cargo=cargo
            self.__salario=salario
            self.__extras=extras
            self.__class__.c+=1
        
    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getsalario(self):
        return self.__salario
    
    def getExtras(self):
        return self.__extras
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def setCargo(self,cargo):
        self.__cargo=cargo
        
    def setSalario(self,salario):
        self.__salario=salario
        
    def setExtras(self,extras):
        self.__extras=extras
        
    def lahora(self):
        total=self.__salario//160
        return total

    def minimoaumento(self):
        if self.__salario==1160000:
            incremento2=self.__salario//100*16.3
            return incremento2
        elif self.__salario>1160000:
            incremento=self.__salario//100*13.3           
            return incremento
        elif self.__salario<1160000:
            return ' Gana menos del minimo'
    
    def extra(self):
        if self.__extras<11 and self.__extras>=0:
            total=self.__extras*self.__salario//160
            return total            
        elif self.__extras>10 or self.__extras<0:
            mensaje=' Las horas extra no pudieron ser diligenciadas'
            return mensaje

ob=empleado('juan','trabajador',1160000,5)
print(ob.s)
print(ob.getNombre(),ob.getCargo(),ob.getsalario(),ob.lahora(),ob.minimoaumento(),ob.extra())
ob1=empleado('maria','admin',15000000,0)
print(ob.s)
print(ob1.getNombre(),ob1.getCargo(),ob1.getsalario(),ob1.lahora(),ob1.minimoaumento(),ob1.extra())
