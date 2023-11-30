class Cuenta:
    def __init__(self, numero_cuenta, saldo, titular):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__titular_cedula = titular

    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_titular_cedula(self):
        return self.__titular_cedula

    def set_titular_cedula(self, titular_cedula):
        self.__titular_cedula = titular_cedula
