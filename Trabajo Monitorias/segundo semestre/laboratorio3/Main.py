from Corresponsal import Corresponsal

class Main:
    @staticmethod
    def main():
        corresponsal1 = Corresponsal("Carlos", "Pérez", "111111111", "123-4567890", "carlos@example.com", "Sucursal A", "Dirección 123")
        corresponsal2 = Corresponsal("María", "Gómez", "222222222", "321-6549870", "maria@example.com", "Sucursal B", "Dirección 456")

        opcion = 999
        while opcion != 0:
            opcion = int(input('\nMENÚ CORRESPONSAL\n'
                                    '1. Iniciar Sesión\n'
                                    '0. Salir\n'
                                    'Selecciona una opción: '))

            if opcion == 1:
                corresponsal = None
                nombre_corresponsal = input("Ingrese su nombre de corresponsal: ")
                for c in [corresponsal1, corresponsal2]:
                    if c.get_nombre() == nombre_corresponsal:
                        corresponsal = c
                        break

                if corresponsal is not None:
                    opcion_operacion = 999
                    while opcion_operacion != 0:
                        opcion_operacion = int(input('\nMENÚ OPERACIONES\n'
                                                    '1. Realizar Depósito\n'
                                                    '2. Realizar Retiro\n'
                                                    '3. Generar Informe Financiero\n'
                                                    '4. Realizar Análisis\n'
                                                    '5. Crear Cliente\n'
                                                    '6. Eliminar Cliente\n'
                                                    '7. Crear Cuenta para Cliente\n'
                                                    '8. Eliminar Cuenta para Cliente\n'
                                                    '0. Cerrar Sesión\n'
                                                    'Selecciona una opción: '))
                    #realizar deposito
                        if opcion_operacion == 1:
                            monto = float(input("Ingrese el monto a depositar: "))
                            numero_cuenta = input("Ingrese el número de cuenta: ")
                            corresponsal.realizar_deposito(numero_cuenta, monto)
                    #realizar retiro
                        elif opcion_operacion == 2:
                            monto = float(input("Ingrese el monto a retirar: "))
                            numero_cuenta = input("Ingrese el número de cuenta: ")
                            corresponsal.realizar_retiro(numero_cuenta, monto)
                    #realizar informe
                        elif opcion_operacion == 3:
                            corresponsal.generar_informe_cuentas()
                    #generar analisis de saldo promedio
                        elif opcion_operacion == 4:
                            corresponsal.generar_reporte_cuentas()
                    #crear cliente
                        elif opcion_operacion == 5:
                            nombre = input('ingrese el nombre del cliente: ')
                            apellido = input('ingrese el apellido del cliente: ')
                            cedula = input('ingrese la cedula del cliente: ')
                            telefono = input('ingrese el telefono del cliente: ')
                            correo = input('ingrese el correo del cliente: ')
                            corresponsal.crear_cliente(nombre,apellido,cedula,telefono,correo)
                    #elimnar cliente        
                        elif opcion_operacion == 6:
                            cedula_cliente_eliminar = input("Ingrese la cédula del cliente a eliminar: ")
                            # Lógica para eliminar cliente (puedes adaptarla según tu implementación)
                            corresponsal.eliminar_cliente(cedula_cliente_eliminar)
                    #crear cuenta cliente
                        elif opcion_operacion == 7:
                            numero_cuenta_cliente = input("Ingrese el número de cuenta: ")
                            cedula_cliente = input("Ingrese la cédula del cliente: ")
                            corresponsal.crear_cuenta_cliente(numero_cuenta_cliente, cedula_cliente)
                    #elimnar cuenta cliente
                        elif opcion_operacion == 8:
                            numero_cuenta_eliminar = input("Ingrese el número de cuenta a eliminar: ")
                            # Aquí llamamos a eliminar_cuenta_cliente con la cédula y el número de cuenta
                            corresponsal.eliminar_cuenta_cliente(numero_cuenta_eliminar)
                    #cerrar sesion
                        elif opcion_operacion == 0:
                            print("Cerrando sesión del corresponsal.")
                    #opcion no valida
                        else:
                            print("Opción no válida. Inténtalo de nuevo.")
        #salir del programa    
            elif opcion == 0:
                print("Saliendo del programa.")
        #opcion no valida
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    Main.main()