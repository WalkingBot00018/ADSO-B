def acceso_diccionario(value,key):
    try:
        return value[key]
    except KeyError:
        print(f"la clave ", {key},  "no se encuentra en el diccionario")
   
l={'gato' : 1, 
   'perro' : 2,
   'raton' : 3}
print(acceso_diccionario(l,'gato'))

    
        