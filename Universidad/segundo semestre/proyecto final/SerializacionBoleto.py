__author__="Juan Pablo Bernal"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from Boletos import Boletos
class SerializacionBoleto():
  """Clase que representa la serializacion de Boleto"""
  serializacionBoleto = None  #para que la variable sea global
  def __init__(self):
    """Metodo constructor que permite crear la serializacion de boleto
        
        Args:
          None
        return:
            None"""
    self.__serializacionBoleto =open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionBoleto.txt', "a")

  def getBoleto(self):
    """metodo consultor que trae la serializacion Boleto.
    
        Args:
            None
        Returns:
            retorno: self.__serializacionBoleto(str)"""
    return self.__serializacionBoleto
  def setBoleto(self, serializacionBoleto):
    """metodo modificador que actualiza la serializacion Boleto.
    
        Args:
            parametro1: serializacionBoleto(str)=serializacionBoleto
        Returns:
            None"""
    self.__serializacionBoleto = serializacionBoleto

  def escribirBoleto(self, dato):
    """Metodo que permite escribir los boletos para la serializacion
        Args:
          parametro1: dato(str)=dato
        Returns:
          None"""
    self.__serializacionBoleto=open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionBoleto.txt', "a")
    self.__serializacionBoleto.write(dato)
    self.__serializacionBoleto.close()
  def leerBoleto(self):
    """Metodo que permite leer los boletos para la serializacion
        Args:
          None
        Returns:
          listaBoleto(str)"""
    self.__serializacionBoleto = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\serializacionBoleto.txt', "r")
    x = 0
    listaBoleto = []
    id = 0
    fecha = ""
    cedulaCliente = ''
    num1 = ''
    num2 = ''
    num3 = ''
    num4 = ''
    num5 = ''
    num6 = ''
    for i in self.__serializacionBoleto:
      if x == 0:
        id = int(i.strip())
        x += 1
      elif x == 1:
        fecha = i.strip()
        x += 1
      elif x == 2:
        cedulaCliente = i.strip()
        x += 1
      elif x == 3:
        num1 = i.strip()
        x += 1
      elif x == 4:
        num2 = i.strip()
        x += 1
      elif x == 5:
        num3 = i.strip()
        x += 1
      elif x == 6:
        num4 = i.strip()
        x += 1
      elif x == 7:
        num5 = i.strip()
        x += 1
      else:
        num6 = i.strip()
        x = 0
        miBoleto = Boletos(id, fecha, cedulaCliente, [num1, num2, num3, num4, num5, num6])
        listaBoleto.append(miBoleto)
    return listaBoleto