__author__="Camilo Londoño"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
class Sorteo():
    """Clase que representa los sorteos de la aplicacion"""
    def __init__(self, id, fecha, listanumeros):
        """Metodo constructor que permite crear objetos de tipo sorteo
    
        Args:
            parametro1: id(int) = id
            parametro2: fecha(str) = fecha
            parametro3: listanumeros(int) = listanumeros

        Returns:
            None"""
        self.id = id
        self.fecha = fecha
        self.listanumeros = listanumeros

    def getId(self):
        """metodo consultor que trae el id del sorteo.
    
        Args:
            None
        Returns:
            retorno: id(int)"""
        return self.id
    def getFecha(self):
        """metodo consultor que trae la fecha del sorteo.
    
        Args:
            None
        Returns:
            retorno: fecha(str)"""
        return self.fecha
    def getListaNumeros(self):
        """metodo consultor que trae la listanumeros del sorteo.
    
        Args:
            None
        Returns:
            retorno: listanumeros(int)"""
        return self.listanumeros

    def setId(self, id):
        """metodo modificador que actualiza la id del sorteo
    
        Args:
            parametro1: id(int)=id
        Returns:
            None"""
        self.id=id
    def setFecha(self, fecha):
        """metodo modificador que actualiza la fecha del sorteo
    
        Args:
            parametro1: fecha(str)=fecha
        Returns:
            None"""
        self.fecha=fecha
    def setListaNumeros(self, listanumeros):
        """metodo modificador que actualiza la listanumeros del sorteo
    
        Args:
            parametro1: listanumeros(int)=listanumeros
        Returns:
            None"""
        self.listanumeros=listanumeros