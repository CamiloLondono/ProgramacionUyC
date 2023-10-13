def mergeSort(notas, estudiantes):
  if len(notas) > 1:
    medio = len(notas) // 2
    izq_notas = notas[:medio]
    der_notas = notas[medio:]
    izq_estudiantes = estudiantes[:medio]
    der_estudiantes = estudiantes[medio:]

    mergeSort(izq_notas, izq_estudiantes)
    mergeSort(der_notas, der_estudiantes)

    i = j = k = 0

    while i < len(izq_notas) and j < len(der_notas):
      if izq_notas[i] < der_notas[j]:
        notas[k] = izq_notas[i]
        estudiantes[k] = izq_estudiantes[i]
        i += 1
      else:
        notas[k] = der_notas[j]
        estudiantes[k] = der_estudiantes[j]
        j += 1
      k += 1

    while i < len(izq_notas):
      notas[k] = izq_notas[i]
      estudiantes[k] = izq_estudiantes[i]
      i += 1
      k += 1

    while j < len(der_notas):
      notas[k] = der_notas[j]
      estudiantes[k] = der_estudiantes[j]
      j += 1
      k += 1
  print("Los estudiantes con las notas ordenadas son:")
  for i in range(len(notas)):
    print(estudiantes[i], ":", notas[i])


estudiantes = []
notas = []

for i in range(6):
  estudiante = input("Ingrese el nombre del estudiante: ")
  estudiantes.append(estudiante)
  nota = float(input("Ingrese la nota del estudiante: "))
  notas.append(nota)

mergeSort(notas, estudiantes)
