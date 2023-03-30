def edad(): #Se crea una funcion llamada edad sin parametros
    try: #Se usa la palabra  try para mirar  el codigo y verificar si tiene errores.
        tuedad=int(input("introduce tu edad")) #Se crea una variable local tuedad la cual es un imput que pide un valor numerico entero al usuario, basicamente pide la edad del usuario.
        print(f'tu edad es  {tuedad}')#Aqui si no hay ningun error se imprime un mensaje mas la edad que el usuario digito en el input de arriba usando el metodo de print f{}.
    except ValueError as e: #Se usa la palabra reservada except mas el error ValueError y se le pone un alias para que se pueda identificar como e.
        print(e)#Si el codigo fue evaluado y se hallo el error en esta parte se imprimira el error o el alias e.
        print("La edad debe ser un valor numerico...")#Esto sera un mensaje para cuando se ejecute nuevamente el codigo, sera un instruccion que pedira directamente que se tiene que digitar un valor numerico.
        edad()#Si el error fue identificado como verdadero se llamara nuevamente la funcion ya creada para que se realice el mismo proceso hasta que el usuario cumpla con las restricciones que el codigo maneja en si mismo.
    else:#Se usa la condicion else para evaluar que si el codigo no tuvo ningun error pues haga lo que esta en el bloque de codigo de la condicion else.
        print('Viene por el else')#Si no hay ningun error muy seguramente se imprimira la linea 4 y la linea 10 osea esta linea ya que se cumple la condicion de no tener los errores.
edad()#Aqui simplemente se llama la funcion para realizar y empezar con la evaluacion del codigo que esta en la misma.