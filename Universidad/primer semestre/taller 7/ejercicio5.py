def calcular_terceralista(lista1,lista2):
    lista = []
    for i in range(0,8,1):
        lista.append(lista1[i]*lista2[i])
    return lista
def acumulado3(lista3):
    acumulado = 0
    for i in lista3:
        acumulado += i
    return acumulado
def promedio3(acumuladolista3):
    promedio = acumuladolista3/8
    return promedio

lista1 = []
lista2 = []
lista3 = []
acumuladolista3 = 0
promediolista3 = 0

for i in range(0,8,1):
    num = int(input('por favor ingrese un numero para agregar a la lista 1: '))
    lista1.append(num)
    num = int(input('por favor ingrese un numero para agregar a la lista 2: '))
    lista2.append(num)

lista3 = calcular_terceralista(lista1,lista2)
acumuladolista3 = acumulado3(lista3)
promediolista3 = promedio3(acumuladolista3)
print ('los valores de la lista 1 son ',lista1,', los valores de la lista 2 son',lista2,', el resultado de la lista 3 es',lista3,', el valor acumulado de la lista 3 es',acumuladolista3,' y el promedio de la lista 3 es',promediolista3)