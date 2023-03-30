def acceso_dicciionario(dicc,key):
    try:
        return dicc[key]
    except KeyError:
        print(f"error la clave {key} no se encuentra en el dicc")

diccionario={'balon' : 1,  'carro' : 2,  'gato' : 3} 
print(acceso_dicciionario(diccionario, 'arbol'))