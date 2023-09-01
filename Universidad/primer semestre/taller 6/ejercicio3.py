#ejercicio 3:

def calcular_promedioa(cursoA):
    promediosuma = 0
    promedio = 0
    for i in cursoA:
        promediosuma += i
    promedio = promediosuma/5
    return promedio
def calcular_promediob(cursoB):
    promediosuma = 0
    promedio = 0
    for i in cursoB:
        promediosuma += i
    promedio = promediosuma/5
    return promedio
def validacion_promedio(promedioa,promediob):
    promeg = 0
    if promedioa > promediob:
        promeg = promedioa
    else:
        promeg = promediob
    return promeg
cursoA = [4,5,3,2,5]
cursoB = [3,4,5,3,1]
promedioa = 0
promediob = 0
promedio_general = 0
promedioa = calcular_promedioa(cursoA)
promediob = calcular_promediob(cursoB)
promedio_general = validacion_promedio(promedioa,promediob)
print ('el promedio del curso a es de{}, el del curso b es de{} y el curso con mayor promedio fue {}'.format(promedioa,promediob,promedio_general))
