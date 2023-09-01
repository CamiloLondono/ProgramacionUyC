from Docente import Docente
from Serializacion import Serializacion
class Main():
    def main():
        miSerializacion = Serializacion()
        miDocente = Docente('1115195149','camilo','23')
        listaEstudiantes = miSerializacion.leerArchivoEstudiantes()
        opcion = 999
        while opcion != 0:
            opcion = int(input('seleccione una opcion:\n1.Registrar estudiante.\n2.Calcular nota\n0.Salir\n.'))
            if opcion == 1:
                miDocente.registrarEstudiante(listaEstudiantes)
            elif opcion == 2:
                for i in listaEstudiantes:
                    print('el promedio de notas es de: ',miDocente.calcularNota(i.getNotas()[0], i.getNotas()[1], i.getNotas()[2], i.getNotas()[3], i.getNotas()[4]))
            elif opcion == 0:
                print('Gracias por usar la aplicacion')
            else:
                print('opcion no valida')
    main()