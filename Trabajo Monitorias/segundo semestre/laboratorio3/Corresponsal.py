from Cliente import Cliente
from Usuario import Usuario
from Cuenta import Cuenta
from Analizador import Analizador
from Reporte import Reporte
from Deposito import Deposito
from Retiro import Retiro

class Corresponsal(Usuario):
    def __init__(self, nombre, apellido, cedula, telefono, correo, nombre_corresponsal, direccion):
        super().__init__(nombre, apellido, cedula, telefono, correo)
        self.nombre_corresponsal = nombre_corresponsal
        self.direccion = direccion
        self.clientes = [] # Añadimos una lista para almacenar los clientes asociados al corresponsal
        self.cuentas = [] # Añadismos una lista para almacenar las cuentas de los clientes

    def get_cuentas(self):
        return self.cuentas

    def crear_cliente(self, nombre, apellido, cedula, telefono, correo):
        nuevo_cliente = Cliente(nombre, apellido, cedula, telefono, correo)
        self.clientes.append(nuevo_cliente)  # Asumiendo que tienes un atributo clientes en Corresponsal
        print(f"Se ha creado un nuevo cliente: {nuevo_cliente.get_nombre()}.")

    def eliminar_cliente(self, cedula):
        cliente_encontrado = None
        for cliente in self.clientes:
            if cedula == cliente.get_cedula():
                cliente_encontrado = cliente
                break
        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)
            print(f"Se ha eliminado al cliente: {cliente_encontrado.get_nombre()}.")
        else:
            print(f"No se encontró un cliente con la cédula {cedula}.")

    def crear_cuenta_cliente(self, numero_cuenta, cedula_cliente):
        cliente = None
        for c in self.clientes:
            if c.get_cedula() == cedula_cliente :
                cliente = c
                break

        if cliente:
            # Crear la cuenta y asociarla al cliente y al corresponsal
            cuenta = Cuenta(numero_cuenta, 0, cliente)
            self.cuentas.append(cuenta)  # Agregar la cuenta a la lista general de cuentas
            print(f"Se ha creado una cuenta para el cliente con cedula {cedula_cliente}.")
        else:
            print(f"No se pudo encontrar o crear el cliente con cédula {cedula_cliente}.")

    def eliminar_cuenta_cliente(self, numero_cuenta):
        cuenta_a_eliminar = None
        for c in self.cuentas:
            if c.get_numero_cuenta() == numero_cuenta:
                cuenta_a_eliminar = c
                break
        if cuenta_a_eliminar:
            self.cuentas.remove(cuenta_a_eliminar)
            print (f"Se ha eliminado la cuenta con número {numero_cuenta}") 
        else:
            print ("La cuenta no existe.")

    def realizar_deposito(self, numero_cuenta, monto):
        cuenta = None
        for c in self.cuentas:
            if c.get_numero_cuenta() == numero_cuenta:
                cuenta = c
                break
        if cuenta:
            miDeposito = Deposito(cuenta,monto)
            miDeposito.realizar_deposito(cuenta,monto)
        else:
            print ("La cuenta no existe.")

    def realizar_retiro(self, numero_cuenta, monto):
        cuenta = None
        for c in self.cuentas:
            if c.get_numero_cuenta() == numero_cuenta:
                cuenta = c
                break
        if cuenta:
            miRetiro = Retiro(cuenta,monto)
            miRetiro.realizar_retiro(cuenta,monto)
        else:
            print ("La cuenta no existe.")
            
    def generar_reporte_cuentas(self):
        analizador = Analizador()
        analizador.calcular_saldo_promedio(self.get_cuentas())

    def generar_informe_cuentas(self):
        reporte = Reporte()
        reporte.generar_reporte(self.get_cuentas())

