from random import randrange
#from serializacionBaloto import serializacionBaloto
class Baloto():
    def __init__(self,fecha,baloto):
        self.__baloto = baloto
        self.__fecha = fecha
    def getFecha(self):
        return self.__fecha
    def getBaloto(self):
        return self.__baloto
    def setBaloto(self,baloto):
        self.__baloto = baloto
    def setFecha(self,fecha):
        self.__fecha = fecha

    def generarBaloto(self,baloto): #Funcion
       # miSerializacion = serializacionBaloto()
        while len(baloto) <6:
            numero = (randrange(1,45,2)) #genera un numero aletario de 1 a 45 impares
            if numero in baloto: #lee la lista para verificar que no este el mismo numero en ella
                pass
            else:
                #miSerializacion.escribirArchivoBaloto(str(baloto)+'\n')
                baloto.append(numero) #con el append agregamos el valor a la lista
        print('El baloto se genero exitosamente')
        return baloto

    def imprimirBaloto(self,fecha,baloto):
        print('El día de hoy',fecha,'el numero jugado fue',baloto)