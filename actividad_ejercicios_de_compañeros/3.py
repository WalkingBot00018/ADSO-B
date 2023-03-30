#Solicite al usuario un usuario y una contraseña la cual debe coincidir con los datos almacenados previamente, 
# debe reconocer minúsculas de mayúsculas.

# Solicitar al usuario un usuario y una contraseña
usuario = input('Ingrese su usuario: ')
contraseña = input('Ingrese su contraseña: ')
 
# Comparar los datos almacenados con la información ingresada
usuario_almacenado = 'mi_usuario'
contraseña_almacenada = 'mi_contraseña'

if usuario.lower() != usuario_almacenado or contraseña != contraseña_almacenada:
    print('Usuario o contraseña incorrectos!')
else:
    print('Bienvenido!')