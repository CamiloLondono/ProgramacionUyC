from Cola import Cola #aca importamos las clases con las que vamos a trabajar
from Pila import Pila #aca importamos las clases con las que vamos a trabajar
class Main():
    def main():
        pila = []
        cola = []
        admin = Cola('bernal',cola) #creamos objetos de las clases para poder llamarlas
        admin2 = Pila('camilo',pila) #creamos objetos de las clases para poder llamarlas
        opcion = 999
        while opcion != 0: #aca creamos un menu donde podemos ejecutar el progrmaa 
            opcion = int(input('\nMenú Principal\nSeleccione la opcion a hacer.\nOprima 1 para administrar cola.\nOprima 2 para administrar pila.\nOprima 0 para salir.\nIngrese la opcion: '))
            if opcion == 1:
                admin.administrarCola(cola) #aca llamamos a las funciones de cada clase respectivamente
            elif opcion ==2:
                admin2.administrarPila(pila) #aca llamamos a las funciones de cada clase respectivamente
            elif opcion == 0:
                print('la pila quedo de la siguiente manera:',admin2.getPila())#aca llamamos un get para imprimir las listas al salir
                print('la cola quedo de la siguiente manera:',admin.getCola())
                print('gracias por usar la aplicacion')
            else:
                print('el valor ingresado no es valido')
    main() 