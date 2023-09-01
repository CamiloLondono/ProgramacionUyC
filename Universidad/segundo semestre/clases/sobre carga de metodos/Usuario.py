class Usuario():
    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
#get y set
    def getCedula(self):
        return self.cedula
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def setCedula(self,cedula):
        self.cedula = cedula
    def setNombre(self,nombre):
        self.nombre = nombre
    def setEdad(self,edad):
        self.edad = edad