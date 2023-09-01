__author__="Camilo Londoño"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Corsoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from Loggin import Loggin
class Main():
    """Clase que representa la clase principal de la aplicacion """
    def main():
        """Metodo principal que permite ejecutar la aplicacion
    
    Args:
    None
    return:
    None"""
        aplicacion = Loggin() #creo un objeto de la clase loggin para ejecutarse la ventana
        aplicacion.abrirVentana()
    main()