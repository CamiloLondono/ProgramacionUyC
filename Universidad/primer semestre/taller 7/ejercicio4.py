def comparar_elementos(lista1,lista2):
    iguales = []
    for i in range(10):
        iguales.append(lista1[i]==lista2[i])
    return iguales

lista1 = []
lista2 = []
igualdad = []
for i in range(0,10,1):
    num = int(input('por favor ingrese un numero para agregar a la lista: '))
    lista1.append(num)
    num = int(input('por favor ingrese un numero para agregar a la segunda lista: '))
    lista2.append(num)

igualdad = comparar_elementos(lista1,lista2)
print('la lista numero 1 tiene estos valores',lista1,'la lista 2 tiene estos valores',lista2,' y la igualdad de los valores de las listas es de ',igualdad)
