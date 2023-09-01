def ingresar_lista():
    lista = []
    for i in range(0,6,1):
        num = int(input('por favor ingrese un numero '))
        lista.append(num)
    return lista
def calcular_acumulado(numeros):
    acumulado = 0
    for i in numeros:
        acumulado += i
    print ('el valor acumulado de los numeros de la lista es de {}'.format(acumulado))
def acumulado_my36(numeros):
    mayores36 = 0
    for i in numeros:
        if i > 16:
            mayores36 += i
    print('el valor acumulado de numeros mayores a 16 es de {}'.format(mayores36))
def cantidad_my40(numeros):
    mayores40 = 0
    for i in numeros:
        if i > 40:
            mayores40 += 1
    print('la cantidad de numeros mayores a 40 es de {}'.format(mayores40))

numeros = []
valoracumulado = 0
acumuladomy36 = 0
cantidadmy40 = 0
numeros = ingresar_lista()
valoracumulado = calcular_acumulado(numeros)
acumuladomy36 = acumulado_my36(numeros)
cantidadmy40 = cantidad_my40(numeros)
print ('la lista de numeros ingresados es {}'.format(numeros))
