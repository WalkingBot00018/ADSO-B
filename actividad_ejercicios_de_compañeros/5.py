#Crear una función que solicite al usuario correo y contraseña los cuales deben coincidir con los datos almacenados previamente, 
# debe reconocer minúsculas de mayúsculas, de lo contrario debe seguir solicitando dicha información.


def verificar_credenciales(usuario, contraseña):
    usuario_almacenado = input('Ingrese su usuario: ')
    contrasena_almacenada = input('Ingrese su contraseña: ')

    """Verifica las credenciales del usuario."""
    
    # Comparar los datos almacenados con la información ingresada
    usuario_almacenado = 'mi_usuario'
    contrasena_almacenada = 'mi_contrasena'
 
    if usuario.lower() != usuario_almacenado or contraseña != contrasena_almacenada:
        return False
    else:
        return True

