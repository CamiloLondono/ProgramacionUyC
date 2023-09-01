from Usuario import Usuario
from Estudiante import Estudiante
from Serializacion import Serializacion
class Docente(Usuario):
    def __init__(self, cedula, nombre, edad):
        Usuario.__init__(self, cedula, nombre, edad)
    #metodos
    def registrarEstudiante(self,listaEstudiantes):
        miSerializacion = Serializacion() #estoy creando un objeto de tipo serializacion para hacer uso de sus funciones 
        cedula = input('por favor ingrese la cedula del estudiante: ')
        nombre = input('por favor ingrese el nombre del estudiante: ')
        edad = input('por favor ingrese la edad del estudiante: ')
        notas = []
        miSerializacion.escribirArchivo(cedula+'\n') #llamo a la funcion para enviar los datos en el orden adecuado como lo declaramos en la funcion 
        miSerializacion.escribirArchivo(nombre+'\n') #al momento de escribir se le escribe un salto de linea para que en el archivo de tipo texto aparezca cada elemento linea por linea 
        miSerializacion.escribirArchivo(str(edad)+'\n')
        for i in range(5):
            nota = float(input('por favor ingrese las notas del estudiante: '))
            miSerializacion.escribirArchivo(str(nota)+'\n')
            notas.append(nota)
        miEstudiante = Estudiante(cedula, nombre, edad, notas)
        listaEstudiantes.append(miEstudiante)
        print('se agrego al estudiante correctamente')
    def calcularNota(self, *args):
        if (len(args) == 0):
            return 0
        elif (len(args) == 1):
            nota = args[0]/5
            return nota
        elif (len(args) == 2):
            nota = (args[0]+args[1])/5
            return nota
        elif (len(args) == 3):
            nota = (args[0]+args[1]+args[2])/5
            return nota
        elif (len(args) == 4):
            nota = (args[0]+args[1]+args[2]+args[3])/5
            return nota
        elif (len(args) == 5):
            nota = (args[0]+args[1]+args[2]+args[3]+args[4])/5
            return nota
        else:
            raise TypeError #este TypeError significa error de consola 