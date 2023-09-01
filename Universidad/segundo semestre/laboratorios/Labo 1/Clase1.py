import random
from Clase2 import Clase2
from Clase3 import Clase3

class Clase1():
    def __init__(self,ed):
        self.ed = ed
    def getId(self):
        return self.ed
    def setId(self,ed):
        self.ed = ed
    #funciones
    def funcion_Uno(self):
        Admin2 = Clase2('laboratorio')#este es otro objeto que almacena los datos
        Admin3 = Clase3('laboratorio')
        mayor = 0
        menor = 15
        acumuladora = 0
        numero = random.sample(range(5,16),5) #esto genera una lista aleatoria de 5 a 15
        print ('la lista generada es: ',numero)
        for i in numero: #por medio de este ciclo obtengo el mayor y el menor numero de la lista
            if i < menor:
                menor = i
            if i > mayor:
                mayor = i
        for i in numero: 
            acumuladora += i
    #es este valor acumulo los 5 numeros de la lista para luego restar el mayor y el menor
        acumuladora = acumuladora - menor - mayor
        print('el numero menor es: ',menor)
        print('el numero mayor es: ',mayor)
        sumatoria = mayor + menor #este suma el mayor y el menor numeor s de la lista 
        print('la suma del numero mayor y menor es de: ',sumatoria)
        print('el acumulado de numeros diferentes al mayor y menor es de: ',acumuladora)
        Admin2.funcion_Dos(sumatoria)# aca a la funcion dos le estoy enviando el valor que ella necesita
        Admin3.funcion_Tres(acumuladora)# aca a la funcion tres le estoy enviando el valor que ella necesita 
