import math

def suma_fracciones(a, b):
     """
     Esta función suma dos fracciones y devuelve el resultado como una fracción simplificada.
     """
     num = a[0] * b[1] + a[1] * b[0]
     den = a[1] * b[1]
     return simplificar_fracción((num, den))

def simplificar_fracción(a):
     """
     Esta función simplifica una fracción y devuelve la forma simplificada como una tupla.
     """
     num = a[0]
     den = a[1]
     gcd = math.gcd(num, den)
     return (num // gcd, den // gcd)

def multiplicar_fracciones(a, b):
     """
     Esta función multiplica dos fracciones y devuelve el resultado como una fracción simplificada.
     """
     num = a[0] * b[0]
     den = a[1] * b[1]
     return simplificar_fracción((num, den))

def dividir_fracciones(a, b):
     """
     Esta función divide dos fracciones y devuelve el resultado como una fracción simplificada.
     """
     num = a[0] * b[1]
     den = a[1] * b[0]
     return simplificar_fracción((num, den))

def restar_fracciones(a, b):
     """
     Esta función resta dos fracciones y devuelve el resultado como una fracción simplificada.
     """
     num = a[0] * b[1] - a[1] * b[0]
     den = a[1] * b[1]
     return simplificar_fracción((num, den))


if __name__=="__main__":
    print("prefiero ser un modulo: ")
else:
    print("desearia ser un modulo: ")