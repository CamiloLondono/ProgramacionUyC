# Función para mostrar el estado de la lista
def mostrarLista(lista, lon):
    listaordenada = ""
    for i in range(0, lon):
        listaordenada += str(lista[i]) + " "
    print(listaordenada)

def identificadorPrimos(lista):
    for i in lista:
        a = i #cojo una variable y se iguala al indice que tiene la lista para verficar si es primo o par
        if a %2 == 0:
            print ('El valor de la lista es par',a)
        else:
            print ('El valor de la lista es primo',a)

arreglo = [] # Crear una lista vacía

# Pedir al usuario que ingrese 11 valores a la lista y agregarlos a 'arreglo'
for i in range(10):
    a = int(input('Ingrese el valor a la lista: '))
    arreglo.append(a)

# Comenzar el proceso de ordenamiento por inserción
for i in range(1, len(arreglo)):
    clave = arreglo[i]
    j = i - 1
    # Comparar el valor seleccionado con todos los valores anteriores
    while (j >= 0 and arreglo[j] > clave):
        # Insertar el valor donde corresponda, desplazando los elementos mayores
        arreglo[j + 1] = arreglo[j]
        j = j - 1
        arreglo[j + 1] = clave  # Colocar el valor seleccionado en su posición correcta
    # Llamar a la función mostrarLista para mostrar el estado actual de la lista
    mostrarLista(arreglo, len(arreglo))

# Llamar a la función mostrarLista nuevamente para mostrar la lista ordenada final
mostrarLista(arreglo, len(arreglo))
identificadorPrimos(arreglo)