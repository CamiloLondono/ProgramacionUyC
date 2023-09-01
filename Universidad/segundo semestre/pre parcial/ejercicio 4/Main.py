from Producto import Producto
class Main():
    def main():
        Productos = []
        producto= None
        for i in range(2):
            nombre = input('por favor ingrese el nombre del producto: ')
            categoria = input('por favor ingrese la categoria del producto: ')
            precioNeto = float(input('por favor ingrese el precio neto del producto: '))
            precioTotal = int(input('por favor ingrese el precio total del producto: '))
            iva = int(input('por favor ingrese el IVA del producto: '))
            producto = Producto(nombre,categoria,precioNeto,precioTotal,iva)
            Productos.append(producto)
        producto.calcularAcumuladoGranos(Productos)
        producto.calcularAcumuladoLacteos(Productos)
        producto.calcularAcumuladoVerduras(Productos)
        producto.calcularAcumuladoAseo(Productos)
    main()