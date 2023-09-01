
__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"

class Boletos():
  """Clase que representa a los boletos de la aplicacion """
  def __init__(self, id, fecha, cedulaCliente, listaNumeros):
    """Metodo constructor que permite crear objetos de tipo boleto.
    
    Args:
    parametro1: id(int) = id
    parametro2: fecha(str) = fecha
    parametro3: cedulaCliente(int) = cedulaCliente
    parametro4: listaNumeros(int) = listaNumeros
    return:
      None"""
    self.__id=id
    self.__fecha=fecha
    self.__cedulaCliente=cedulaCliente
    self.__listaNumeros=listaNumeros

  def getId(self):
    """metodo consultor que trae el id del boleto.
    
    Args:
      None
    Returns:
    retorno: id(int)"""
    return self.__id
  def getFecha(self):
    """metodo consultor que trae la fecha del boleto.
    
    Args:
      None
    Returns:
    retorno: fecha(str)"""
    return self.__fecha
  def getCedulaCliente(self):
    """metodo consultor que trae la cedulaCliente del boleto.
    
    Args:
      None
    Returns:
    retorno: cedulaClientes(int)"""
    return self.__cedulaCliente
  def getListaNumeros(self):
    """metodo consultor que trae la listaNumeros del boleto.
    
    Args:
      None
    Returns:
    retorno: listaNumeros(int)"""
    return self.__listaNumeros

  def setId(self, id):
    """metodo modificador que actualiza la id del boleto
    
    Args:
      parametro1: id(int)=id
    Returns:
    None"""
    self.__id=id
  def setFecha(self, fecha):
    """metodo modificador que actualiza la fecha del boleto
    
    Args:
      parametro1: fecha(str)=fecha
    Returns:
    None"""
    self.__fecha=fecha
  def setCedulaCliente(self, cedulaCliente):
    """metodo modificador que actualiza la cedulaCliente del boleto
    
    Args:
      parametro1: cedulaCliente(int)=cedulaCliente
    Returns:
    None"""
    self.__cedulaCliente=cedulaCliente
  def setListaNumeros(self, listaNumeros):
    """metodo modificador que actualiza la listaNumeros del boleto
    
    Args:
      parametro1: listaNumeros(int)=listaNumeros
    Returns:
    None"""
    self.__listaNumeros=listaNumeros