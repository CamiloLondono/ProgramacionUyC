def valorAcumulado(numeros):
    acumulado = 0
    for i in numeros:
        acumulado += i
    return acumulado
def mayores50(numeros):
    acumulado = 0
    for i in numeros:
        if i < 20:
            acumulado += i
    return acumulado
def cantidadValores(numeros):
    cantidad = 0
    for i in numeros:
        if i > 50:
            cantidad += 1
    return cantidad

numeros = []
valor_Acumulado = 0
acumuladoMayores50 = 0
cantidadMayores50 = 0
for i in range (8):
    numero = int(input('por favor ingrese un numero: '))
    numeros.append(numero)
valor_Acumulado = valorAcumulado(numeros)
acumuladoMayores50 = mayores50(numeros)
cantidadMayores50 = cantidadValores(numeros)
print('el valor acumulado de los numeros es de: ',valor_Acumulado,'\nEl valor acumulado de los numeros menores a 20 es de: ',acumuladoMayores50,'\nLa cantidad de numeros mayores a 50 es de: ',cantidadMayores50)