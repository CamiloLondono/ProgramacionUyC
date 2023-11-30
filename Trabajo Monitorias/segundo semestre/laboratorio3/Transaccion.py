class Transaccion:
    contador_transacciones = 0  # Contador para asignar números consecutivos a las transacciones

    def __init__(self, cuenta, monto):
        Transaccion.contador_transacciones += 1
        self.numero_transaccion = Transaccion.contador_transacciones
        self.cuenta = cuenta
        self.monto = monto

    def getnumero_transaccion(self):
        return self.numero_transaccion 

    def getcuenta(self):
        return self.cuenta

    def setcuenta(self, nuevaCuenta):
        self.cuenta = nuevaCuenta
    
    def getmonto(self):
        return self.monto
    
    def setmonto(self, monto):
        self.monto = monto

    def realizar_transaccion(self):
        pass  # La implementación específica se hará en las subclases