#esto una funcion definimos y le ponemos un nombre ala funcion que tendra parametros vacios
def edad():
#el try es basicamente un codigo que se aparata para realizarle una comprabacion de errorres
    try:
#en esta linea lo que se ve es una variable que va a aser probada y dentor de esta variable  podemos ver que hay un
#int y un inpu el int es para escribir numeros enteros y el input letra pero aqui basicamente es para que el usuario introdusca por teclado
#un numero entero
        tuedad=int(input("introduce tu edad"))
## dentro de los print esta uan f eso es templex iterales que basicamente es para que la variable aparesca y quede ordenadamente 
        print(f'tu edad es  {tuedad}')
        #print('Tu edad es ',tuedad)
#el except es una ecepcion o error que se tiene que corregir
#el value error es un tipo de error que significa que uno ingresa un valor incorrecto ejemplo aqui en este codigo si ingresamos
#un string nos va a adar ese error por que en este esta pidiendo un numeor entero
#el as aqui es para abreviar basicamento esos nombres de errores tan largos por una letra o otro nombre en especifico
    except ValueError as e:   
    #estas lineas del prin se inprimen de acuerdo con la ecepcion si no se cumple sale el mensaje y si se cumple pas y no se ejecuta 
        print(e)
        print("La edad debe ser un valor numerico...")
    #esto es para llamar la funcion y bueno pues aqui se puso para ver si no se cumple sal el error pero vuelve a pedir el numero 
        edad()
    #este esle es un condicional que va  arriba del if pero ene este caso el profe nos dijo
    # que el else tambien puede estar en excepciones y significa y sino se cumple  pues imprima esto
    else:
        # aqui imprime de acuerdo al else si no se cumple pues imprime este mensaje
        print('Viene por el else')
#aqui es para llamar la funcion y que se pueda ejecuta
edad()