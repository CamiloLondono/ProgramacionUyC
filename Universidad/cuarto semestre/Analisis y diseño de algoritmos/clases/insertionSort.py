from random import sample
def insertionSort(notas,estudiantes):
    print('El vector a ordenar es:',vectorIns)
    largo = 0
    for i in vectorIns:
        largo += 1
    for i in range(1,largo):
        elemento = vectorIns[i]
        #movemos los elementos de vectorIns[0....i-1] que son mayores que el elemento a una posicion adelante de su posicion actual
        j=i-1
        while j >= 0 and vectorIns[j] > elemento:
            vectorIns[j+1] = vectorIns[j]
            j -= 1
        vectorIns[j+1] = elemento
    print('el vector ordenado es:',vectorIns)
estudiantes = []
notas = []
for i in range(6):
    estudiante = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(estudiante)
    nota = float(input("Ingrese la nota del estudiante: "))
    notas.append(nota)
insertionSort(notas,estudiantes)