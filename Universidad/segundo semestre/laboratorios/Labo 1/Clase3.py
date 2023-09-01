
class Clase3():
    def __init__(self,ed):
        self.ed = ed
    def getId(self):
        return self.ed
    def setId(self,ed):
        self.ed = ed
    #funciones
    def funcion_Tres(self,acumuladora):
        if acumuladora % 2 == 0:#aca uso el modulo para comprobar que el valor ingresado sea divisible entre 2 y hacer la respectiva operacion
            acumuladora = pow(acumuladora,2)#con el metodo pow hago la potencia, mandando de primer valor la variable a potenciar y el segundo valor el numero al cual se va a potenciar 
            print('el valor al cuadrado es de: ',acumuladora,'\n ')
        else:
            acumuladora = pow(acumuladora,3)
            print('el valor al cubo es de: ',acumuladora,'\n ')