
class Usuario():
    """clase que representa a los usuarios de la aplicacion"""
    def __init__(self,nombre,password):
        """Metodo constructor que permite crear objetos de tipo usuario.
        
        Args:
            parametro 1: nombre(str) = nombre
            parametro 2: password(str) = password
        Returns:
            None"""
        self.__nombre = nombre
        self.__password = password
    def getNombre(self):
        """Metodo cosultor que trae el nombre de usuario.
        
        Args:
            None
        Returns:
            retorno: nombre(str)"""
        return self.__nombre
    def getPassword(self):
        """Metodo cosultor que trae el password de usuario.
        
        Args:
            None
        Returns:
            retorno: password(str)"""
        return self.__password
    def setNombre(self,nombre):
        """Metodo modificador que actualiza el nombre de usuario.
        
        Args:
            parametro 1: nombre(str) = nombre
        Returns:
            None"""    
        self.__nombre = nombre
    def setPassword(self,password):
        """Metodo modificador que actualiza el password de usuario.
        
        Args:
            parametro 1: password(str) = password
        Returns:
            None"""
        self.__password = password