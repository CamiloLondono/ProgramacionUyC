

class Producto():
	def __init__(self, nombre, categoria, precioNeto, precioTotal, iva):
		self.__nombre = nombre
		self.__categoria = categoria
		self.__precioNeto = precioNeto
		self.__precioTotal = precioTotal
		self.__iva = iva

	def getNombre(self):
		return self.__nombre

	def getCategoria(self):
		return self.__categoria

	def getPrecioNeto(self):
		return self.__precioNeto

	def getPrecioTotal(self):
		return self.__precioTotal

	def getIva(self):
		return self.__iva

	def setNombre(self, nombre):
		self.__nombre = nombre

	def setCategoria(self, categoria):
		self.__categoria = categoria

	def setPrecioNeto(self, precioNeto):
		self.__precioNeto = precioNeto

	def setPrecioTotal(self, precioTotal):
		self.__precioTotal = precioTotal

	def setIva(self, iva):
		self.__iva = iva

	def calcularPromedio(self, listaProductos):
		acumulado = 0
		promedio = 0
		for i in listaProductos:
			acumulado = acumulado + i.getPrecioTotal()
		promedio = acumulado/len(listaProductos)
		print("El promedio del precio total de los Productos es: ",promedio)

class Principal():
	def main():
		"""Logica principal"""
		producto = None #Objeto nulo
		productos = []
		for i in range(2):
			nombre = input("Ingrese el nombre del Producto: ")
			categoria = input("Ingrese la categoria del Producto: ")
			precioNeto = float(input("Ingrese el precio neto del Producto: "))
			precioTotal = float(input("Ingrese el precioTotal del Producto: "))
			iva = float(input("Ingrese el iva del Producto: "))
			producto = Producto(nombre, categoria, precioNeto, precioTotal, iva)
			productos.append(producto)
		producto.calcularPromedio(productos)


	main()