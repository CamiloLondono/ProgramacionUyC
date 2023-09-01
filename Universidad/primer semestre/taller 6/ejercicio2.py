#ejercico 2:

def calcular_nino(edad1,edad2,edad3,edad4,edad5):
    '''esta funcion sirve para saber cuantos son niños'''
    edades = [edad1,edad2,edad3,edad4,edad5]
    menor = 0
    adolescentes = 0
    for i in edades:
        if i <= 10:
            menor += 1
    return menor
def calcular_adolescente(edad1,edad2,edad3,edad4,edad5):
    '''esta funcion sirve para calcular cuantos son adolescentes'''
    edades = [edad1,edad2,edad3,edad4,edad5]
    adoles = 0
    for i in edades:
        if i > 10 and i <= 25:
            adoles += 1
    return adoles
def calcular_adulto(edad1,edad2,edad3,edad4,edad5):
    '''esta funcion sirve para calcular los adultos'''
    edades = [edad1,edad2,edad3,edad4,edad5]
    mayor = 25
    adul = 0
    for i in edades:
        if i > mayor:
            adul += 1
    return adul
edad1 = int(input('por favor ingrese la edad '))
edad2 = int(input('por favor ingrese la edad '))
edad3 = int(input('por favor ingrese la edad '))
edad4 = int(input('por favor ingrese la edad '))
edad5 = int(input('por favor ingrese la edad '))
nino = 0 
adulto = 0
adolescentes = 0 
nino = calcular_nino(edad1,edad2,edad3,edad4,edad5)
adolescentes = calcular_adolescente(edad1,edad2,edad3,edad4,edad5)
adulto = calcular_adulto(edad1,edad2,edad3,edad4,edad5)
print ('la cantidad de niños es de {}, la cantidad de adolescentes es de {} y la cantidad de adultos es de {}'.format(nino,adolescentes,adulto))
