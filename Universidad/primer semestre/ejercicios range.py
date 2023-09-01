
#ejercicio 1:

i = 0
for i in range(5,16,1):
    print ("los valores son {}".format(i))

#ejercicio2:

valorAcumulado = 0
valorAcumuladomy36 = 0
cantidadmy50 = 0
i = 0
for i in range(0,8,1):
    numero = int(input("por favor ingrese un numero entero "))
    valorAcumulado += numero
    if numero > 36:
        valorAcumuladomy36 += numero
    if numero > 50:
        cantidadmy50 += 1
print ("el valor acomulado de todos los numeros es de {}, el valor acumulado de los numeros mayores a 36 es de {} y la cantidad de numeros mayores a 50 es de {}".format(valorAcumulado,valorAcumuladomy36,cantidadmy50))

#ejercicio 3:

nino = 0
adolescentes = 0
adultos = 0
i = 0
for i in range(0,5,1):
    edad = int(input("por favor ingrese la edad de la persona "))
    if edad <= 10:
        nino += 1
    elif edad <= 25:
        adolescentes += 1
    else:
        adultos += 1
print("la cantidad de niños es de {}, la cantidad de adolescentes es de {} y la cantidad de adultos es de {}".format(nino,adolescentes,adultos))