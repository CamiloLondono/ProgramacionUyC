
class Clase4():
    def __init__(self,ed):
        self.ed = ed
    def getId(self):
        return self.ed
    def setId(self,ed):
        self.ed = ed
    #funciones 
    def funcion_Cuatro(self,primero,ultimo):
        valor = (primero + ultimo) * 30 #aca resivo los dos valores de la funcion 2 para hacer la respectiva operacion 
        return print('la suma del primer punto y del ultimo punto multiplicada por 30 es :',valor)