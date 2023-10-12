from random import sample
#importamos un metodo de la biblioteca random para generar listas aleatorias

lista = list(range(100)) #numero del 1 al 100

#creamos una lista aleatoria con sample
#(8 elementos aleatorios de la lista base)
vectorbs = sample(lista,8)

def bubblesort(vectorbs):
    print('El vector a ordenar es:',vectorbs)
    #establecer un contador
    n = 0
    
    for _ in vectorbs:
        n += 1 #contamos la cantidad de caracteres dentro del vector
    
    for i in range(n-1):
        #le damos un rango n para que complete el proceso
        for j in range(0,n-i-1):
            #revisa la matriz de 0 hasta n-i-1
            if vectorbs[j] > vectorbs[j+1]:
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
    print ('El vector ordenado es:',vectorbs)
bubblesort(vectorbs)