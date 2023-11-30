from datetime import datetime
from Analizador import Analizador
from Cuenta import Cuenta

class Reporte:
    def __init__(self):
        self.fecha_generacion = datetime.now()

    def ocultar_digitos_cedula(self, cliente):
        # Mostrar solo los últimos 4 dígitos de la cédula del cliente
        return '******' + cliente.get_cedula()[-4:]

    def generar_reporte(self, cuentas):
        if not cuentas:
            print("No hay cuentas para generar el reporte.")
            return

        analizador = Analizador()
        saldo_promedio = analizador.calcular_saldo_promedio(cuentas)

        print("\n=== INFORME FINANCIERO ===")
        print(f"Fecha de Generación del Informe: {self.fecha_generacion}")
        print(f"Número total de cuentas: {len(cuentas)}")

        if saldo_promedio is not None:
            print(f"Saldo Promedio de las cuentas: ${saldo_promedio:.2f}")

        print("\nDetalles de cada cuenta:")
        for cuenta in cuentas:
            print(f"\nNúmero de Cuenta: {cuenta.get_numero_cuenta()}")
            print(f"Cédula del Cliente: {self.ocultar_digitos_cedula(cuenta.get_titular_cedula())}")
            print(f"Saldo de la Cuenta: ${cuenta.get_saldo():.2f}")
