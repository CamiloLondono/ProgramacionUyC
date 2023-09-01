class Empleado():
    def __init__(self,nombre,cedula,edad,salario):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.salario = salario 
    def getNombre(self):
        return self.nombre
    def getCedula(self):
        return self.cedula
    def getEdad(self):
        return self.edad
    def getSalario(self):
        return self.salario
    def setNombre(self,nombre):
        self.nombre = nombre
    def setCedula(self,cedula):
        self.cedula = cedula
    def setEdad(self,edad):
        self.edad = edad
    def setSalario(self,salario):
        self.salario = salario
    # funciones
    def calcularValorNeto(self,salario):
        if salario > 879.000:
            descuento = (7*salario)/100
            valor = salario - descuento
        print('el salario del empleado con el descuento es de: ',valor)
    def calcuarValorSalud(self,salario):
        descuento = (salario*12.5)/100
        salario1 = salario - descuento
        salario2 = salario - salario1
        print('el empleado debe pagar de salud: ',salario2)
    def calcuarValorPension(self,salario):
        descuento = (salario*16)/100
        salario1 = salario - descuento
        salario2 = salario - salario1
        print('el valor a pagar por pension es de: ',salario2)
    def calcuarValorARL(self,salario):
        descuento = (salario*3.5)/100
        salario1 = salario - descuento
        salario2 = salario - salario1
        print('el valor a pagar del ARL es de: ',salario2)
