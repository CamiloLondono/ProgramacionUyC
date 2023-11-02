class Cuenta():
    def __init__(self, numero_cuenta, saldo, cedula_cliente):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.cedula_cliente = cedula_cliente

    
    
    def getNumero_cuenta(self):
        return self.numero_cuenta
    def getSaldo(self):
        return self.saldo
    def getCedula_cliente(self):
        return self.cedula_cliente
    
    def setNumero_cuenta(self,numero_cuenta):
        self.numero_cuenta = numero_cuenta
    def setSaldo(self, saldo):
        self.saldo = saldo
    def setCedula_cliente(self, cedula_cliente):
        self.cedula_cliente = cedula_cliente


    def CrearCuenta(self, listaCuentas):
        Cuenta_ = None

        numero_cuenta = input("ingrese el numero de cuenta que desea: ")
        cedula_cliente = (input("ingrese su cedula: "))
        saldo = 0
        cuenta = Cuenta(numero_cuenta, cedula_cliente, saldo)
        listaCuentas.append(cuenta)  #agrega la nueva cuenta

        print("Su cuenta se ha creado con exito!!!!\n")

    


