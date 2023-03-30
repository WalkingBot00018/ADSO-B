#esto es una tupla dentro de una variable llamada values
values = (1, 0)
#x,y=19,30
#print(divmod(10,3))
#el try es basicamente un codigo que se aparata para realizarle una comprabacion de errorres
try:
#son dos varibles creadas con una coma que teiene un metodo div mod que la division que tiene un anterisco dentro de la tupla y este anterisco lo que hace es desagregarlo que hay en la tupla
    q, r = divmod(*values) 
    #print('q=',q)
#este print inprime un argumento
# dentro de los print esta uan f eso es templex iterales que basicamente es para que la variable aparesca y quede ordenadamente  
    print(f'q={q}')
    print(f'r={r}')
#el except es una ecepcion o error que se tiene que corregir
#aqui en el print nos muestran dos tipos de errores las cuales el zero es un error que no permite dividirse entre cero, el type es cuando usamos un tipo de dato incorrecto
#el as aqui es para abreviar basicamento esos nombres de errores tan largos por una letra o otro nombre en especifico
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)