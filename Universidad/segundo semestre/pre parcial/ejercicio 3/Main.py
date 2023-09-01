from Empleado import Empleado
class Main:
    def main():
        empleados = []
        empleado = None
        for i in range(1):
            nombre = input('por favor ingrese su nombre: ')
            cedula = input('por favor ingrese su cedula: ')
            edad = input('por favor ingrese la edad: ')
            salario = float(input('por favor ingrese el salario del empleado: '))
            empleado = Empleado(nombre,cedula,edad,salario)
            empleados.append(empleado)
        empleado.calcularValorNeto(salario)
        empleado.calcuarValorSalud(salario)
        empleado.calcuarValorPension(salario)
        empleado.calcuarValorARL(salario)
    main()
        