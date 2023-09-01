from Clase1 import Clase1

class Main():
    def main():
        opcion = 999
        Admin = Clase1('laboratorio') #este admin esta inicializando la clase para llamar la funcion
        while opcion != 0:
            opcion = int(input('Oprima opcion 1 para ejecutar el programa.\nOprima la opcion 0 si desea salir\n.'))
            if opcion == 1:
                Admin.funcion_Uno() #aca el admin llama la funcion que esta almacenada en la clase 1
            elif opcion == 0:
                print('gracias por usar la aplicacion')
            else:
                print('la opcion ingresada no es valida')
    main()
