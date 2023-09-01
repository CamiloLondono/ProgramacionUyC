__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from Usuario import Usuario

class SerializacionUsuarios():
    """Clase que representa la serializacion de los Usuarios"""
    archivoUsuarios = None
    def __init__(self):
        """Metodo constructor que permite crear la serializacion de los Usuarios
        
        Args:
          None
        return:
            None"""
        self.archivo = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\archivoUsuarios.txt','a') 
    def getAchivoUsuarios(self):
        """metodo consultor que trae la serializacion de los Usuarios.
    
    Args:
      None
    Returns:
      retorno: self.__archivoUsuarios(str)"""
        return self.__archivoUsuarios
    def setArchivoUsuarios(self,archivoUsuarios):
        """metodo modificador que actualiza la serializacion de los Usuarios.
    
        Args:
            parametro1: archivoUsuarios(str)=archivoUsuarios
            None"""
        self.__archivoUsuarios = archivoUsuarios
    def escribirArchivoUsuarios(self,dato):
        """Metodo que permite escribir los Usuarios para la serializacion
        Args:
          parametro1: dato(str)=dato
        Returns:
          None"""
        self.__archivoUsuarios = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\archivoUsuarios.txt','a')
        self.__archivoUsuarios.write(dato)
        self.__archivoUsuarios.close()
    def sobreescribirArchivoUsuarios(self,texto):
        """Metodo que permite sobreescribir los Usuarios para la serializacion
        Args:
          parametro1: texto(str)=texto
        Returns:
          None"""
        self.__archivoUsuarios = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\archivoUsuarios.txt','w')
        self.__archivoUsuarios.write(texto)
        self.__archivoUsuarios.close()
    def leerArchivoUsuarios(self):
        """Metodo que permite leer los Usuarios para la serializacion
        Args:
          None
        Returns:
          listaUsuarios(str)"""
        self.__archivoUsuarios = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\proyecto final\\archivoUsuarios.txt','r')
        x = 0
        listaUsuarios = []
        cedula = 0
        nombre = ''
        apellido = ''
        edad = 0
        telefono = 0
        email = ''
        direccion = ''
        rol = ''
        password = ''
        for i in self.__archivoUsuarios:
            if x == 0:
                cedula = i.strip()
                x += 1
            elif x == 1:
                nombre = i.strip()
                x += 1
            elif x == 2:
                apellido = i.strip()
                x += 1
            elif x == 3:
                edad = i.strip()
                x += 1
            elif x == 4:
                telefono = i.strip()
                x += 1
            elif x == 5:
                email = i.strip()
                x += 1
            elif x == 6:
                direccion = i.strip()
                x += 1
            elif x == 7:
                rol = i.strip()
                x += 1
            else:
                password = i.strip()
                x = 0
                miUsuario = Usuario(cedula, nombre, apellido, edad, telefono, email, direccion, rol, password)
                listaUsuarios.append(miUsuario)
        return listaUsuarios