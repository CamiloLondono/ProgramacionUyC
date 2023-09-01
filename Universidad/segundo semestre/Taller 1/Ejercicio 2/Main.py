from Estudiante import Estudiante
class Main():
    def main():
        estudiantes = []
        estudiante = None
        for i in range(2):
            nombre = input('por favor ingrese el nombre del estudiante: ')
            edad = int(input('por favor ingrese la edad del estudiante: '))
            nota = float(input('por favor ingrese la nota del estudiante: '))
            estudiante = Estudiante(nombre, edad, nota)
            estudiantes.append(estudiante)
        estudiante.calcular_promedio(estudiantes)
        estudiante.notaAlta(estudiantes)
        estudiante.notaBaja(estudiantes)
        estudiante.aprobraronProgramacion(estudiantes)
    main()
