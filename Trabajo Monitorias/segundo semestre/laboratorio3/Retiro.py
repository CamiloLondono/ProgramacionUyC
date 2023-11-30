from Transaccion import Transaccion

class Retiro(Transaccion):

    def realizar_retiro(self,cuenta,monto):
        if monto > cuenta.get_saldo():
            print('la cuenta no tiene suficiente saldo')
        else:
            cuenta.set_saldo(cuenta.get_saldo()-monto)
            print("retiro exitoso")