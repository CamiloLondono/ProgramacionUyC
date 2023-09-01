from Usuario import Usuario
class Estudiante(Usuario): #en el parentesis va la clase de la que esta heredando
    def __init__(self,cedula,nombre,edad,notas):
        Usuario.__init__(self, cedula, nombre, edad)#en este se especifica que parametros heredar
        self.__notas = notas
    #get y set 
    def getNotas(self):
        return self.__notas
    def setNotas(self,notas):
        self.__notas = notas