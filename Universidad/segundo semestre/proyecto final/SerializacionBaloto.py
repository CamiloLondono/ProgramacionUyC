__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Corsoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from Baloto import Baloto

class SerializacionBaloto():
    """Clase que representa la serializacion de Baloto"""
    serializacionBaloto=None #variable nula
    
    def __init__(self):
        """Metodo constructor que permite crear la serializacion de baloto
        
        Args:
          None
        return:
            None"""
        self.__serializacionBaloto=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionBaloto.txt', "a")#Busco el archivo y la "a" es para decir que lea el archivo

    def getBaloto(self):
        """metodo consultor que trae la serializacion Baloto.
    
        Args:
            None
        Returns:
            retorno: self.__serializacionBaloto(str)"""
        return self.__serializacionBaloto

    def setBaloto(self, serializacionBaloto):
        """metodo modificador que actualiza la serializacion Baloto.
    
        Args:
            parametro1: serializacionBaloto(str)=serializacionBaloto
        Returns:
            None"""
        self.__seBaloto=serializacionBaloto

    def escribirBaloto(self, dato):
        """Metodo que permite escribir los balotos para la serializacion
        Args:
          parametro1: dato(str)=dato
        Returns:
          None"""
        self.__serializacionBaloto=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionBaloto.txt', "a")
        self.__serializacionBaloto.write(dato)
        self.__serializacionBaloto.close()
    def leerBaloto(self):
        """Metodo que permite leer los balotos para la serializacion
        Args:
          None
        Returns:
          listaBaloto(str)"""
        self.__serializacionBaloto=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionBaloto.txt', "r")
        x = 0
        listaBaloto=[]
        id = 0
        fecha =""
        nume1 = ''
        nume2 = ''
        nume3 = ''
        nume4 = ''
        nume5 = ''
        nume6 = ''
        for i in self.__serializacionBaloto:
          if x == 0:
            id=int(i.strip())
            x += 1
          elif x == 1:
            fecha=i.strip()
            x += 1
          elif x == 2:
            nume1=(i.strip())
            x += 1
          elif x == 3:
            nume2=(i.strip())
            x += 1
          elif x == 4:
            nume3=(i.strip())
            x += 1
          elif x == 5:
            nume4=(i.strip())
            x += 1
          elif x == 6:
            nume5=(i.strip())
            x += 1
          else:
            nume6=(i.strip())
            x = 0
            miBaloto = Baloto(id, fecha, [nume1, nume2, nume3, nume4, nume5, nume6])
            listaBaloto.append(miBaloto)
        return listaBaloto