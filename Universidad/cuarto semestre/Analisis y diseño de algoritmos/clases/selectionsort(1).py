def selection_sort(notas, estudiantes):
    print("Las notas a ordenar son:", notas)
    n = len(notas)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if notas[j] < notas[minimo]:
                minimo = j
        # Los intercambios deben estar fuera del bucle interno
        notas[i], notas[minimo] = notas[minimo], notas[i]
        estudiantes[i], estudiantes[minimo] = estudiantes[minimo], estudiantes[i]

    print("Los estudiantes ordenados son:")
    for i in range(n):
        print("La nota de", estudiantes[i], "fue:", notas[i])

estudiantes = []
notas = []

for i in range(6):
    estudiante = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(estudiante)
    nota = float(input("Ingrese la nota del estudiante: "))
    notas.append(nota)

selection_sort(notas, estudiantes)
