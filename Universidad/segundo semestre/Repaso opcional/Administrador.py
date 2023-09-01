from Producto import Producto
#llegado el caso no se llame igual se llamaria 'from producto import clase'
class Administrador():
    def __init__(self,nombre,cedula):
        self.__nombre = nombre
        self.__cedula = cedula 
    def getNombre(self):
        return self.__nombre
    def getCedula(self):
        return self.__cedula
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setCedula(self,cedula):
        self.__cedula = cedula
#metodos
    def agregarProducto(self,listaProductos):
        Id = int(input('Por favor ingrese el Id del producto: '))
        nombre = input('Por favor ingrese el nombre del producto: ')
        categoria = input('Por favor ingrese la categoria del producto: ')
        precio = int(input('Por favor ingrese el precio del producto: '))
        miProducto = Producto(Id,nombre,categoria,precio)
        listaProductos.append(miProducto)
        #notificar al usuario que los procesos funcionaron
        print('El producto',nombre,'ha sido agregado con exito')
    def eliminarProducto(self,listaProductos,Id):
        productoEncontrado = False
        for i in listaProductos:
            if i.getId() == Id:
                listaProductos.remove(i)
                productoEncontrado = True
                print('El producto ha sido eliminado con exito')
        if (productoEncontrado == False):
            print('El producto no exite')
    def calcularPrecioTotal(self,listaProductos):
        total = 0
        for i in listaProductos:
            total = total + i.getPrecio()
        return total
