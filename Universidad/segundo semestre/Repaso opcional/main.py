from Administrador import Administrador

class Main():
    def main ():
        miAdministrador = Administrador('Camilo','99091810049')
        listaProductos = []
        opcion = 999
        while (opcion) != 0:
            opcion = int(input('Seleccione una opción:\n1. Agregar un producto.\n2. Eliminar producto.\n3. Calcular precio total de los producto.\n0. Salir\n'))
            if opcion == 1:
                miAdministrador.agregarProducto(listaProductos)
            elif opcion == 2:
                Id = int(input('Ingrese el indentificador del producto a eliminar: '))
                miAdministrador.eliminarProducto(listaProductos,Id)
            elif opcion == 3:
                total = miAdministrador.calcularPrecioTotal(listaProductos)
                print('El precio total de los productos es de:',total)
            elif opcion == 0:
                print('Gracias por usar la aplicacion.')
            else:
                print('La opcion ingresada no es valida')
    main()
'''no se una la funcion brak porque si el valor agregado es 0, ya por defecto se cierra la aplicacion'''