from Cuenta import *

class Transaccion(Cuenta):
    def __init__(self, numero_cuenta, saldo, cedula_cliente):
        super().__init__(numero_cuenta, saldo, cedula_cliente)   
        self.Ntransaccion = 0  # Inicializa el contador de transacciones en 0

    def getNtransaccion(self):
        return self.Ntransaccion

    def realizarDeposito(self,listaCuentas):
        encontrado = False
        numerocuenta = input("Ingrese el numero de cuenta a buscar: ")
        for Cuenta in listaCuentas:
            if(numerocuenta == Cuenta.getNumero_cuenta()):
                encontrado = True 
                monto = int(input("Ingrese el monto a depositar: $"))
                nuevo_saldo = int(Cuenta.getSaldo())
                nuevo_saldo1 = nuevo_saldo + monto
                Cuenta.setSaldo(nuevo_saldo1)
                self.Ntransaccion += 1
                contadora = self.getNtransaccion()
                print("EL saldo fue agregado con exito!!!\nid transaccion es:",contadora)
                break
        if(encontrado == False):
            print("La cuenta no se  encuentra, verifique e intente de nuevo\n")

    def realizarRetiro(self,listaCuentas):
        encontrado = False
        numeroretiro = input("Ingrese el numero de cuenta a retirar: ")
        
        pass