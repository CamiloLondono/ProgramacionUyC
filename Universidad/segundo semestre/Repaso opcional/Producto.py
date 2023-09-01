class Producto ():
    def __init__(self,Id,nombre,categoria,precio):
        self.__Id = Id
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
    def getId(self):
        return self.__Id
    def getNombre(self):
        return self.__nombre
    def getCategoria(self):
        return self.__categoria
    def getPrecio(self):
        return self.__precio
    def setId(self,Id):
        self.__Id = Id
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setCategoria(self,categoria):
        self.__categoria = categoria
    def setPrecio(self,precio):
        self.__precio = precio
    