#ejercicio 1:

def valoracumulado(num1,num2,num3,num4,num5,num6):
    """esta funcion sirve para calcular el valor acumulado"""
    numeros = [num1,num2,num3,num4,num5,num6]
    valoracumulado = 0
    for i in numeros:
        valoracumulado += i
    return valoracumulado
def mayores36(num1,num2,num3,num4,num5,num6):
    """esta funcion sirve para calcular los valores mayores a 36"""
    numeros = [num1,num2,num3,num4,num5,num6]
    mayores = 0
    for i in numeros:
        if i >= 36:
            mayores += i
    return mayores
def cantidadmayor50(num1,num2,num3,num4,num5,num6):
    """esta funcion sirve para calcular la cantidad de numeros mayores a 50"""
    numeros = [num1,num2,num3,num4,num5,num6]
    mayores50 = 0
    for i in numeros:
        if i >= 50:
            mayores50 += 1
    return mayores50
num1 = int(input('por favor ingrese un numero '))
num2 = int(input('por favor ingrese un numero '))
num3 = int(input('por favor ingrese un numero '))
num4 = int(input('por favor ingrese un numero '))
num5 = int(input('por favor ingrese un numero '))
num6 = int(input('por favor ingrese un numero '))
valor_acumulado = 0
valor_mayores36 = 0
cantidad_mayores50 = 0
valor_acumulado = valoracumulado(num1,num2,num3,num4,num5,num6)
valor_mayores36 = mayores36(num1,num2,num3,num4,num5,num6)
cantidad_mayores50 = cantidadmayor50(num1,num2,num3,num4,num5,num6)
print ('el valor acumulado de las numeros es de {}, el valor acumulado de numeros mayores a 36 es de {} y la cantidad de numeros mayores a 50 es de {}'.format(valor_acumulado,valor_mayores36,cantidad_mayores50))
