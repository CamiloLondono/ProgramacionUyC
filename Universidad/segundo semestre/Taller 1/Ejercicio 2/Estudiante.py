class Estudiante():
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getNota(self):
        return self.nota
    def setNombre(self, nombre):
        self.nombre = nombre
    def setEdad(self, edad):
        self.edad = edad
    def setNota(self, nota):
        self.nota = nota

    def calcular_promedio(self, estudiantes):
        #calculo promedio de edad
        promedio = 0
        for i in estudiantes:
            promedio += i.getEdad()
        promedio = promedio/len(estudiantes)
        print('edad promedio es: ',promedio)
    def notaAlta(self, estudiantes):
        #la nota mas alta de los estudiantes de programacion
        nota = -1
        for i in estudiantes:
            if i.getNota() > nota:
                nota = i.getNota()
        print('la nota mas alta del curso de programacion es de ',nota)
    def notaBaja(self, estudiantes):
        #la nota mas baja de estudiantes de programacion
        nota = 100
        for i in estudiantes:
            if i.getNota() < nota:
                nota = i.getNota()
        print('la nota mas baja del curso de programacion es de ',nota)
    def aprobraronProgramacion(self, estudiantes):
        # estudiantes que aprobaron programacion
        contador = 0
        for i in estudiantes:
            if i.getEdad() < 18 and i.getNota() >= 3:
                contador+=1
        print('la cantidad de estudiantes menores de edad que aprobaron fue de ',contador)