def convertir_a_decimal(num, base):
     """
     Esta función convierte un número de una base dada a forma decimal.
     """
     decimal = 0
     valor_posicional = 1
     for digito in num[::-1]:
         decimal += int(digito) * valor_posicional
         valor_posicional *= base
     return decimal

def convertir_decimal_dado(num, base):
     """
     Esta función convierte un número decimal en un número en una base dada.
     """
     if num == 0:
         return "0"
    
     resultado = ""
     while  num > 0:
         digito = num % base
         resultado = str(digito) + resultado
         num = num // base
     return resultado

def agregar_numeros_en_base(num1, num2, base):
     """
     Esta función suma dos números en una base dada y devuelve el resultado en esa base.
     """
     decimal1 = convertir_a_decimal(num1, base)
     decimal2 = convertir_a_decimal(num2, base)
     suma_decimal = decimal1 + decimal2
     return convertir_decimal_dado(suma_decimal, base)

if __name__=="__main__":
    print("prefiero ser un modulo: ")
else:
    print("desearia ser un modulo: ")