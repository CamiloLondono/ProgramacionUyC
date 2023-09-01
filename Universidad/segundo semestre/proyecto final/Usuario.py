__author__="Juan Pablo Bernal"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from MenuAdmin import MenuAdmin
from MenuUsuario import MenuUsuario
class Usuario():
    """Clase que representa a los usuarios de la aplicacion """

    def __init__(self, cedula, nombre, apellido, edad, telefono, email, direccion, rol, password):
        """Metodo constructor que permite crear objetos de tipo usuario
        
        Args:
            parametro1: cedula(int) = cedula
            parametro2: nombre(str) = nombre
            parametro3: apellido(str) = apellido
            parametro4: edad(int) = edad
            parametro5: telefono(int) = telefono
            parametro6: email(str) = email
            parametro7: direccion(str) = direccion
            parametro8: rol(str) = rol
            parametro9: pasawor(str) = password    
        return:
            None"""
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.telefono=telefono
        self.email=email
        self.direccion=direccion
        self.rol=rol
        self.password = password

    def getCedula(self):
        """metodo consultor que trae la cedula de usuario.
    
        Args:
            None
        Returns:
            retorno: cedula(int)"""
        return self.cedula
    def getNombre(self):
        """metodo consultor que trae el nombre de usuario.
        
        Args:
            None
        Returns:
            retorno: nombre(str)"""
        return self.nombre
    def getApellido(self):
        """metodo consultor que trae el apellido de usuario.
        
        Args:
            None
        Returns:
            retorno: nombre(str)"""
        return self.apellido
    def getEdad(self):
        """metodo consultor que trae la edad de usuario.
    
        Args:
            None
        Returns:
            retorno: edad(int)"""
        return self.edad
    def getTelefono(self):
        """metodo consultor que trae el telefono de usuario.
        
        Args:
            None
        Returns:
            retorno: telefono(int)"""
        return self.telefono
    def getEmail(self):
        """metodo consultor que trae el email de usuario.
    
        Args:
            None
        Returns:
            retorno: email(str)"""
        return self.email
    def getDireccion(self):
        """metodo consultor que trae la direccion de usuario.
    
        Args:
            None
        Returns:
            retorno: direccion(str)"""
        return self.direccion
    def getRol(self):
        """metodo consultor que trae el rol de usuario.
    
        Args:
            None
        Returns:
            retorno: rol(str)"""
        return self.rol
    def getPassword(self):
        """metodo consultor que trae el password de usuario.
    
        Args:
            None
        Returns:
            retorno: password(str)"""
        return self.password

    def setCedula(self, cedula):
        """metodo modificador que actualiza la cedula de usuario
    
        Args:
            parametro1: cedula(int)=cedula
        Returns:
            None"""
        self.cedula=cedula
    def setNombre(self, nombre):
        """metodo modificador que actualiza el nombre de usuario
    
        Args:
            parametro1: nombre(str)=nombre
        Returns:
            None"""
        self.nombre=nombre
    def setApellido(self, apellido):
        """metodo modificador que actualiza el appelido de usuario
    
        Args:
            parametro1: apellido(str)=apellido
        Returns:
            None"""
        self.apellido=apellido
    def setEdad(self, edad):
        """metodo modificador que actualiza la edad de usuario
    
        Args:
            parametro1: edad(int)=edad
        Returns:
            None"""
        self.edad=edad
    def setTelefono(self, telefono):
        """metodo modificador que actualiza el telefono de usuario
    
        Args:
            parametro1: telefono(int)=telefono
        Returns:
            None"""
        self.telefono=telefono
    def setEmail(self, email):
        """metodo modificador que actualiza el email de usuario
    
        Args:
            parametro1: email(str)=email
        Returns:
            None"""
        self.email=email
    def setDireccion(self, direccion):
        """metodo modificador que actualiza la direccion de usuario
    
        Args:
            parametro1: direccion(str)=direccion
        Returns:
            None"""
        self.direccion=direccion
    def setRol(self, rol):
        """metodo modificador que actualiza el rol de usuario
    
        Args:
            parametro1: rol(str)=rol
        Returns:
            None"""
        self.rol=rol
    def setPassword(self, password):
        """metodo modificador que actualiza el password de usuario
    
        Args:
            parametro1: password(str)=password
        Returns:
            None"""
        self.password = password
    
    #funciones
    def consultarGanadorDia(self,listaBaloto,listaRevancha,varBaloto,varRevancha):
        """Metodo para consultar al ganador del dia
        Args:
            parametro1: listaBaloto(str)=listaBaloto
            parametro2: listaRevancha(str)=listaRevancha
            parametro3: varBaloto(str)=varBaloto
            parametro4: varRevancha(str)=varRevancha
        Return:
            None"""
        ultimoBaloto = listaBaloto[-1] #va a coger el ultimo indice de la lista
        ultimaRevancha = listaRevancha[-1]
        varBaloto.set((ultimoBaloto.getListaNumeros()[0],'-',ultimoBaloto.getListaNumeros()[1],'-',ultimoBaloto.getListaNumeros()[2],'-',ultimoBaloto.getListaNumeros()[3],'-',ultimoBaloto.getListaNumeros()[4],'-',ultimoBaloto.getListaNumeros()[5])) #Agregar numeros al campo texto
        varRevancha.set((ultimaRevancha.getListaNumeros()[0],'-',ultimaRevancha.getListaNumeros()[1],'-',ultimaRevancha.getListaNumeros()[2],'-',ultimaRevancha.getListaNumeros()[3],'-',ultimaRevancha.getListaNumeros()[4],'-',ultimaRevancha.getListaNumeros()[5]))