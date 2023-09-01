from listas import listas #importamos la clase principal de la cual vamos a heredar
#solo comento esta clase porque hace lo mismo que la clase cola 
class Pila(listas):
    def __init__(self,lista,pila): 
        listas.__init__(self,lista) #aca le especificamos que caracteristicas heredar 
        self.__pila = pila #agregamos un valor mas a las caracteristicas de la pila, que es la lista
    def getPila(self): 
        return self.__pila
    def setPila(self,pila):
        self.__pila = pila 
    #metodos
    def administrarPila(self,pila): #no se crea una lista, sino que se recibe como parametro la lista vacia ya par trabajar con ella y poder llamarla a la hora de cerrar el codigo 
        opcion = 999
        while opcion != 0:
            opcion = int(input('\nMenú Pila\nSeleccione la opcion a hacer:\nOprima 1 para insertar.\nOprima 2 para remover.\nOprima 3 para regresar.\nIngrese la opcion: '))
            if opcion == 1:
                if len(pila) >= 12: #aca le decimos que lea la lista creada y si tiene mas elementos no agrega mas
                    print('La pila no tiene espacio')
                else: #si por caso contrario la lista si tiene espacio sigue agregando valores 
                    valor = int(input('ingrese el valor entero a ingresar a la pila: '))
                    pila.append(valor)
                    print('Se ingreso correctamente el valor a la pila')
                    print(pila)
            elif opcion == 2:
                valor = int(input('Ingrese el numero de valores de 1 a 12 a remover de la pila: '))
                if len(pila) >= valor: #leemos la lista para ver si se pueden borrar valores 
                    if valor > 0:
                        for i in range(valor): #con un ciclo le decimos que interactue con el valor que le llego a elementos para borrar
                            pila.pop(-1) #eliminamos y el -1 es para decir que se elimina de atras para adelante 
                        print('Se removio correctamente el valor.') #ponemos el print fuera del ciclo para que solo aparezca una vez eliminado todo
                    else:
                        print('No hay elementos para borrar') #si el valor llegado es 0, no borra ningun elemento
                else:
                    print('La pila no tiene los elementos que desea borrar')
                    #si el valor ingresado a borrar es mayor a los elementos en la lista no deja borrar 
            elif opcion ==3:
                return #usamos un return para volver al menu principal sin necesidad de romper el ciclo <3 
            else:
                print('el numero ingresado no es valido')
        