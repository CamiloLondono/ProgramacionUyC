from Transaccion import Transaccion

class Deposito(Transaccion):

    def realizar_deposito(self,cuenta,monto):
        cuenta.set_saldo(cuenta.get_saldo()+monto)
        print("deposito exitoso")
            