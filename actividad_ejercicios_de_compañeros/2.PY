#Solicite al usuario un usuario y una contraseña la cual debe coincidir con los datos almacenados previamente, 
#debe reconocer minúsculas de mayúsculas, de lo contrario debe seguir solicitando dicha información.

# Solicitar al usuario un usuario y una contraseña
usuario = input('Ingrese su usuario: ')
contrasena = input('Ingrese su contraseña: ')
 
# Comparar los datos almacenados con la información ingresada
usuario_almacenado = 'mi_usuario'
contrasena_almacenada = 'mi_contrasena'
 
while usuario.lower() != usuario_almacenado or contrasena != contrasena_almacenada:
    print('Usuario o contraseña incorrectos!')
    usuario = input('Ingrese su usuario: ')
    contrasena = input('Ingrese su contraseña: ')
 
print('Bienvenido!')