def ingresar_lista1():
    lista = []
    for i in range(4):
        num = int(input('por favor ingrese un numero para ingresarlo en la lista 1: '))
        lista.append(num)
    return lista
def ingresar_lista2():
    lista = []
    for i in range(4):
        num = int(input('por favor ingrese un numero para ingresarlo en la lista 2: '))
        lista.append(num)
    return lista
def suma_lista3(lista1,lista2):
    lista = []
    for i in range(4):
        lista.append(lista1[i]+lista2[i])
    return lista
lista1 = []
lista2 = []
lista3 = []
lista1 = ingresar_lista1()
lista2 = ingresar_lista2()
lista3 = suma_lista3(lista1,lista2)
print('el valor de la suma de los 2 vectores es de: {}'.format(lista3))