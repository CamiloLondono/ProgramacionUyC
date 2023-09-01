__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from Revancha import Revancha

class SerializacionRevancha():
  """Clase que representa la serializacion de Revancha"""
  serializacionRevancha=None
  def __init__(self):
    """Metodo constructor que permite crear la serializacion de revancha
        
        Args:
          None
        return:
            None"""
    self.__serializacionRevancha=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionRevancha.txt', "a")#Busco el archivo y la "a" es para decir que lea el archivo

  def getRevancha(self):
    """metodo consultor que trae la serializacion de Revancha.
    
    Args:
      None
    Returns:
      retorno: self.__serializacionRevancha(str)"""
    return self.__serializacionRevancha

  def setRevancha(self, serializacionRevancha):
    """metodo modificador que actualiza la serializacion de Revancha.
    
        Args:
            parametro1: serializacionRevancha(str)=serializacionRevancha
        Returns:
            None"""
    self.__serializacionRevancha = serializacionRevancha

  def escribirRevancha(self, dato):
    """Metodo que permite escribir la Revancha para la serializacion
        Args:
          parametro1: dato(str)=dato
        Returns:
          None"""
    self.__serializacionRevancha=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionRevancha.txt', "a")
    self.__serializacionRevancha.write(dato)
    self.__serializacionRevancha.close()

  def leerRevancha(self):
    """Metodo que permite leer la Revancha para la serializacion
        Args:
          None
        Returns:
          listaRevancha(str)"""
    self.__serializacionRevancha=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionRevancha.txt', "r")
    x = 0
    listaRevancha = []
    id = 0
    fecha = ""
    nume1 = ''
    nume2 = ''
    nume3 = ''
    nume4 = ''
    nume5 = ''
    nume6 = ''
    for i in self.__serializacionRevancha:
      if x == 0:
        id = int(i.strip())
        x += 1
      elif x == 1:
        fecha = i.strip()
        x += 1
      elif x == 2:
        nume1= (i.strip())
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
        miRevancha = Revancha(id, fecha, [nume1, nume2, nume3, nume4, nume5, nume6])
        listaRevancha.append(miRevancha)
    return listaRevancha