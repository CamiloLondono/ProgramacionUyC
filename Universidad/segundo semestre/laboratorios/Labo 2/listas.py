class listas():
    def __init__(self,lista):
        self.__lista = lista
    def getLista(self):
        return self.__lista
    def setLista(self,lista):
        self.__lista = lista
#la clase principal de la cual heredan la pila y cola solo lleva el objeto 