from Cuenta import *
from Transaccion import *                                    

class main():
    def main():
        listaCuentas = []
        opcion = 990
        miCuenta = Cuenta(111,1115195045,0)
        miTransaccion = Transaccion(111,1115195045,0)
        while (opcion != 0) :
            opcion = int(input("menu principal\n1. Crear Cuenta bancaria \n2. \n3. \n4. \n5. \n0. salir\n -->"  ))
            if (opcion == 1) :
                miCuenta.CrearCuenta(listaCuentas)
            elif (opcion == 2) :
                miTransaccion.realizarDeposito(listaCuentas)
            elif (opcion == 3) :
                pass
            elif (opcion == 4) :
                pass
            elif (opcion == 5) :
                pass
            elif (opcion == 0) :
                print("hasta la proxima")
            else :
                print(" opcion no valida intente nuevamente ")
    
    main()
        


