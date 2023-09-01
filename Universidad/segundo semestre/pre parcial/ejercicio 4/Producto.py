class Producto():
    def __init__(self,nombre,categoria,precioNeto,precioTotal,iva):
        self.nombre = nombre
        self.categoria = categoria
        self.precioNeto = precioNeto
        self.precioTotal = precioTotal
        self.iva = iva
    def getNombre(self):
        return self.nombre
    def getCategoria(self):
        return self.categoria
    def getPrecioNeto(self):
        return self.precioNeto
    def getPrecioTotal(self):
        return self.precioTotal
    def getIva(self):
        return self.iva
    def setNombre(self,nombre):
        self.nombre = nombre
    def setCategoria(self,categoria):
        self.categoria = categoria
    def setPrecioNeto(self,precioNeto):
        self.precioNeto = precioNeto
    def setPrecioTotal(self,precioTotal):
        self.precioTotal = precioTotal
    def setIva(self,iva):
        self.iva = iva
    #funciones
    def calcularAcumuladoGranos(self,Productos):
        acumulado = 0
        categoria = 'granos'
        for i in Productos:
            if i.categoria == categoria:
                acumulado = acumulado + i.precioTotal
        print('el valor total de los productos de categoria granos es de: ',acumulado)
    def calcularAcumuladoLacteos(self,Productos):
        acumulado = 0
        categoria = 'lacteos'
        for i in Productos:
            if i.getCategoria() == categoria:
                acumulado += i.getPrecioTotal()
        print('el valor total de los productos de categoria lacteos es de: ',acumulado)
    def calcularAcumuladoVerduras(self,Productos):
        acumulado = 0
        categoria = 'verduras'
        for i in Productos:
            if i.getCategoria() == categoria:
                acumulado += i.getPrecioTotal()
        print('el valor total de los productos de categoria verduras es de: ',acumulado)
    def calcularAcumuladoAseo(self,Productos):
        acumulado = 0
        categoria = 'aseo'
        for i in Productos:
            if i.getCategoria() == categoria:
                acumulado += i.getPrecioTotal()
        print('el valor total de los productos de categoria aseo es de: ',acumulado)