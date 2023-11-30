"""3.	Desarrollar un programa que pida la carga de DOS LISTAS  numéricas enteras de 10 elementos cada una. Generar una TERCERA LISTA que compare los elementos de cada posición y almacene en esta última un mensaje así, según corresponda:

•	Son iguales
•	El mayor está en la primera lista
•	El mayor está en la segunda lista

lista1 = []
lista2 = []

for i in range(10):
    numero = int(input('Por ingrese los numeros de la lista 1: '))
    lista1.append(numero)

for i in range(10):
    numero = int(input('Por ingrese los numeros de la lista 2: '))
    lista2.append(numero)

comparaciones = []

for i in range(10):
    if lista1[i] == lista2[i]:
        comparaciones.append('son iguales')
    elif lista1[i] > lista2[i]:
        comparaciones.append('el numero mayor esta en la lista 1')
    else:
        comparaciones.append('el numero mayor esta en la lista 2')

for i in comparaciones:
    print(i) 

#ejercicio 4

listaNombres = []
listaCodigos = []
listaNotas = []
contador = 0
while contador != 5:
    nombre = input('Ingrese el nombre del estudiante: ')
    codigo = input('Ingrese el codigo del estudiante: ')
    nota = float(input('Ingrese la nota del estudiante: '))
    listaNombres.append(nombre)
    listaCodigos.append(codigo)
    listaNotas.append(nota)
    contador += 1

indice_notaAlta = listaNotas.index(max(listaNotas))
indice_notaBaja = listaNotas.index(min(listaNotas))

for i,valor in enumerate(listaNombres):
    if i == indice_notaAlta:
        nombre = valor

for i,valor in enumerate(listaCodigos):
    if i == indice_notaAlta:
        codigo = valor

print('El estudiante con la nota mas alta es',nombre,'con codigo',codigo)

for i,valor in enumerate(listaNombres):
    if i == indice_notaBaja:
        nombre = valor

for i,valor in enumerate(listaCodigos):
    if i == indice_notaBaja:
        codigo = valor

print('El estudiante con la nota mas baja es',nombre,'con codigo',codigo)



ejercicio 5:

cantidad = int(input('ingrese la cantidad de usuarios que tiene su empresa: '))
nombres = []
salarios = []
for i in range(cantidad):
    nombre = input('ingrese el nombre del empleado: ')
    salario = float(input('ingrese el salario del empleado: '))
    nombres.append(nombre)
    salarios.append(salario)

listaOrdenada = sorted(zip(salarios,nombres)) #la funcion sorted me acomoda una lista de menor a mayor pero sin monidifcar la lista original, solo creando una nueva lista
# y la funcion zip me combinar 2 listas 
print(salarios)
print(nombres)
print(listaOrdenada)"""

tecla="S"
lista_codigo=[]
lista_nombre=[]
lista_nota=[]

while tecla=="s" or tecla=="S":
    cod=input("Ingrese un codigo:")
    nom=input("Ingrese su nombre:")
    nof=input("Ingrese la nota definitiva de la materia:")


    lista_codigo.append(cod)
    lista_nombre.append(nom)
    lista_nota.append(nof)
    tecla=input("Desea continuar S/N:")

notaAlta= lista_nota.index(max(lista_nota)) 
notaBaja= lista_nota.index(min(lista_nota))

for i,valor in enumerate(lista_nombre):
    if i==notaBaja:
        nombre1=valor

for i,valor in enumerate(lista_codigo):
    if i==notaBaja:
        codigo1=valor

print("El estudiante con la nota más baja es",nombre1,"con codigo",codigo1)

for i, valor in enumerate(lista_nombre):
    if i == notaAlta:
        nombre2=valor

for i, valor in enumerate(lista_codigo):
    if i == notaAlta:
        codigo2=valor

print("El estudiante con la nota más alta es", nombre2, "con codigo",codigo2)