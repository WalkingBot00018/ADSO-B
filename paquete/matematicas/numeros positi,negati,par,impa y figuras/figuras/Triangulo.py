def Triangulos():
    print("Clasificacion de triangulos")
    print("!Tipos de triangulos segun sus lados(!Caracteristicas¡)")
    print("1-Equilatero")
    print("2-Escaleno")
    print("3-Isosceles")
    print("!Tipos de triangulos segun sus angulos(!Caracteristicas¡)")
    print("4-Triangulo Rectangulo")
    print("5-Triangulo Acutangulo")
    print("Elije una opcion")
    opcion=int(input("Digite el numero del triangulo para ver sus caracteristicas: ")) 
    if opcion==1:
        print("Elejiste Equilatero:Los lados de este tipo de triangulo tienen la misma longitud")
    elif opcion==2:
        print("Elejiste Escaleno:Este triangulo posee longitudes distintas en sus lados,tambien sus lados difieren en amplitud")
    elif opcion==3:
        print("Elejiste Isosles:Este triangulo tiene dos lados que poseen la misma medida,y uno que es diferente")
    elif opcion==4:
        print("Elejiste Rectangulo:Posee un angulo recto(90° grados),sus otros dos angulos son agudos o menores a 90°")
    elif opcion==5:
        print("Elejiste Acutangulo: Sus tres angulos son agudos")
    else:
        print("El numero digitado no esta en la lista")    
        
        
        

    
