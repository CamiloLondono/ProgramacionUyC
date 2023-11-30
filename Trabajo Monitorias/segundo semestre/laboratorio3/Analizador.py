from datetime import datetime
from Cuenta import Cuenta
from datetime import datetime

class Analizador:
    def __init__(self):
        self.fecha_analisis = datetime.now()

    def get_fecha_analisis(self):
        return self.fecha_analisis

    def calcular_saldo_promedio(self, cuentas):
        if not cuentas:
            print("No hay cuentas para calcular el saldo promedio.")
            return 0

        total_saldo = sum(cuenta.get_saldo() for cuenta in cuentas)
        promedio = total_saldo / len(cuentas)
        print('El saldo promedio de las cuentas es de', promedio, 'Reporte realizado el día', self.fecha_analisis)
