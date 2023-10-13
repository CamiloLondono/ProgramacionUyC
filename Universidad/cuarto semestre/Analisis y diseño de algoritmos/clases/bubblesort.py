def bubblesort(notas, estudiantes):
    print("El vector a ordenar es:", notas)
    n = len(notas)
    for i in range(n - 1):
        # Le damos un rango n-1 para que complete el proceso
        for j in range(0, n - i - 1):
            # Revisa la matriz de 0 hasta n-i-1
            if notas[j] > notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
    print("Los estudiantes con las notas ordenadas son:")
    for i in range(n):
        print(estudiantes[i], ":", notas[i])

estudiantes = []
notas = []
for i in range(5):
    estudiante = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(estudiante)
    nota = float(input("Ingrese la nota: "))
    notas.append(nota)

bubblesort(notas, estudiantes)
