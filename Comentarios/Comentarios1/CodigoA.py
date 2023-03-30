try:#Se usa el  try para tratar el siguiente bloque de codigo y mirar su posibles errores.
    raise SyntaxError #aqui hay una excepcion excepcion SyntaxError con el metodo raise.
except SyntaxError: #aqui hay excepcion SyntasError por medio dexcept la cual mirara el fragmento de codigo del try y si ocurre el error vendra aqui.
    print('Cierra el parentesis') #aqui se imprime el mensaje si el error fue de la sintaxis
    