from listas import listas
class Cola(listas):
    def __init__(self,lista,cola):
        listas.__init__(self, lista)
        self.__cola = cola
    def getCola(self):
        return self.__cola
    def setCola(self,cola):
        self.__cola = cola
    #metodos
    def administrarCola(self,cola):
        opcion = 999
        while opcion != 0:
            opcion = int(input('\nMenú Cola\nSeleccione la opcion a hacer:\nOprima 1 para insertar.\nOprima 2 para remover.\nOprima 3 para regresar.\nIngrese la opcion: '))
            if opcion == 1:
                if len(cola) >= 12:
                    print('La cola no tiene espacio')
                else:
                    valor = int(input('ingrese el valor entero a ingresar a la cola: '))
                    cola.append(valor)
                    print('Se ingreso correctamente el valor a la cola')
                    print(cola)
            elif opcion == 2:
                valor = int(input('Ingrese el numero de valores de 1 a 12 a remover de la cola: '))
                if len(cola) >= valor:
                    if valor > 0:
                        for i in range(valor):
                            cola.pop(0) #el metodo remover 
                        print('Se removio correctamente el valor.')
                    else:
                        print('No hay elementos para borrar')
                else:
                    print('La cola no tiene los elementos que desea borrar')
            elif opcion ==3:
                return
            else:
                print('el numero ingresado no es valido')