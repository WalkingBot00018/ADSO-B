#esto una funcion definimos y le ponemos un nombre ala funcion que tendra dos parametro
def try_syntax(numerator, denominator):
##el try es basicamente un codigo que se aparata para realizarle una comprabacion de errorres
    try:
        print(f'In the try block: {numerator}/{denominator}')
#en eat linea nos muestra que se crea una variable dentro del print la cual es la que se va a revisar, dentor de esa variable 
#se hace una operacion y es dividir el parametro numerator con denominator 
        result = numerator / denominator
#el except es una ecepcion o error que se tiene que corregir
#el tipo de error zero es un error que no permite dividirse entre cero
#el as aqui es para abreviar basicamento esos nombres de errores tan largos por una letra o otro nombre en especifico
    except ZeroDivisionError as zde:
#este print inprime un argumento y lo muestra por panatalla
        print(zde)
#este esle es un condicional que va  arriba del if pero ene este caso el profe nos dijo
# que el else tambien puede estar en excepciones y significa y sino se cumple  pues imprima esto
    else:
#en esta linea nprime un argumento y lo muestra por panatalla que saldra como salida el resultado es: la divicion que se hiso 
        print('The result is:', result)
#esta lina lo que hace es devolkver el la variable osea devolver la divicion de resultado
        return result

    finally:
#n esta linea nprime un argumento y lo muestra por panatalla
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
#aqui se llama la funcion para ejecutarla haber si hay o no errores
print(try_syntax(11, 0))