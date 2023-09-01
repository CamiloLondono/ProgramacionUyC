from Baloto import Baloto
from Revancha import Revancha
#from serializacionBaloto import serializacionBaloto
import datetime
class Main():
    def main():
        #miSerializacion = serializacionBaloto()
        fechaActual = datetime.datetime.now() #guarda la fecha actual del equipo
        fechaActual2 = datetime.datetime.strftime(fechaActual,'%d/%m/%Y') #solo acomoda la fecha 
        opcion = 999
        baloto = []
        revancha = []
        Admin = Baloto(fechaActual2,baloto)
        Admin2= Revancha(fechaActual2,revancha)
        while opcion != 0:
            opcion = int(input(' MENÚ PRINCIPAL\n Administrar sorteos.\n1.Realizar sorteo baloto.\n2.Realizar sorteo revancha.\n3.Imprimir los resultados de los sorteos del día.\n4.Imprimir todos los resultados del Baloto.\n5.Imprimir todos los resultados de revancha.\n0.Salir.\n'))
            if opcion == 1:
                Admin.generarBaloto(baloto)
            elif opcion == 2:
                Admin2.generarRevancha(revancha)
            elif opcion == 3:
                print('los resultados del día del baloto fueron',baloto,'y de revancha fueron',revancha)
            elif opcion == 4:
                Admin.imprimirBaloto(fechaActual2,baloto)
            elif opcion == 5:
                Admin2.imprimirRevancha(fechaActual2,revancha)
            elif opcion == 0:
                print('Felicitaciones a los ganadores')
            else:
                print('opción no válida')
    main()