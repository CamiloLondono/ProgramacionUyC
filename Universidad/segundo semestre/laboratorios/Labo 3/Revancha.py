from random import randrange
class Revancha():
    def __init__(self,fecha,revancha):
        self.__revancha = revancha
        self.__fecha = fecha
    def getFecha(self):
        return self.__fecha
    def getRevancha(self):
        return self.__revancha
    def setRevancha(self,revancha):
        self.__revancha = revancha
    def setFecha(self,fecha):
        self.__fecha = fecha
    
    def generarRevancha(self,revancha):
        while len(revancha) <6:
            numero = (randrange(2,44,2))
            if numero in revancha:
                pass
            else:
                revancha.append(numero)
        print('La revancha se genero exitosamente')
        return revancha

    def imprimirRevancha(self,fecha,revancha):
        print('El día de hoy',fecha,'el numero jugado fue',revancha)