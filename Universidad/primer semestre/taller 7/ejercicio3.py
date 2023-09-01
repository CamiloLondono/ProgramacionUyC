def sublista_izquierda(lista1):
    lista = []
    for i in lista1:
        if i % 8 == 0:
            indice = i
            break
    lista = lista1[:indice]
    return lista
def sublista_derecha(lista1):
    lista = []
    for i in lista1:
        if i % 8 == 0:
            indice = i
            break
    lista = lista1[indice-1:]
    return lista
    
lista1 = []
sublistaiz = []
sublistadere = []
for i in range(0,10,1):
    num = int(input('por favor ingrese un numero para agregar a la lista: '))
    lista1.append(num)
    
sublistaiz = sublista_izquierda(lista1)
sublistadere = sublista_derecha(lista1)

print ('la sub lista izquierda de la lista principal es ',sublistaiz,' y la sub lista derecha es ',sublistadere)
