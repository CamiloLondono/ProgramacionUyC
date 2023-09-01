from Clase4 import Clase4

class Clase2():
    def __init__(self,ed):
        self.ed = ed
    def getId(self):
        return self.ed
    def setId(self,ed):
        self.ed = ed
    # funciones
    def funcion_Dos(self,sumatoria):
        Admin4 = Clase4('laboratorio')
        primero = 76
        ultimo = 0
        lista2 = []
        suma = sumatoria + 10
        for i in range(suma,77,10):
 #crea una lista con el valor de la sumatoria de la funcion 1 aumentando de 10 en 10 hasta almacenar 5 elementos 
            lista2.append(i)
        for i in lista2:#con este ciclo obtengo el primer numero de la lista y el ultimo de la generada
            if i < primero:
                primero = i
            if i > ultimo:
                ultimo = i
        print('la lista de numeros generados a partir de la suma es: ',lista2)
        print('el primer numero de la lista es ',primero,'y el ultimo numero de la lista es',ultimo)
        Admin4.funcion_Cuatro(primero,ultimo)#aca le estoy enviando a la funcion 4 los valores que ella necesita
