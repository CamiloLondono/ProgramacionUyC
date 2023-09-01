from Estudiante import Estudiante

class Serializacion():
    archivo = None
    def __init__(self): #en la serializacion solo recibe el objeto, ningun parametro
        self.__archivo = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\clases\\sobre carga de metodos\\archivo.txt','a') #el metodo open para abrir el archivo, la primera comilla es para agregar la ruta donde sera guardado el archivo, la segunda comilla sera la accion  A que hara el archivo 
    def getArchivo(self):
        return self.__archivo
    def setArchivo(self,archivo):
        self.__archivo = archivo
    #funciones
    def escribirArchivo(self,dato):
        self.__archivo = open ('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\clases\\sobre carga de metodos\\archivo.txt','a') #aca en la direccion en el ultimo slash se genera otro para crearle nombre al archivo 
        self.__archivo.write(dato) #el write es para escribir en el archivo creado
        self.__archivo.close()#el archivo siempre se debe de cerrar para que no salga un error 
    def leerArchivoEstudiantes(self):
        self.__archivo = open ('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\clases\\sobre carga de metodos\\archivo.txt','r') #aca en la segunda comilla tenemos la R para que lea el archivo
        #para leer todo el archivo se usa el self.archivo.read()
        #para leer solo una linea se una el self.archivo.readLine()
        x = 0 #se crea una variable para apoyarse en el ciclo 
        listaEstudiantes = []
        #aca son 8 varibales porque son las 8 variables que tiene un objeto de tipo estudiante 
        cedula = ''
        nombre = ''
        edad = 0
        nota1 = 0
        nota2 = 0
        nota3 = 0
        nota4 = 0
        nota5 = 0
        for i in self.__archivo: 
            if x == 0:
                #el metodo strip suprime el salto de linea 
                cedula = i.strip()
                x += 1
            elif x == 1:
                nombre = i.strip()
                x += 1
            elif x == 2:
                edad = int(i.strip())
                x += 1
            elif x == 3:
                nota1 = float(i.strip())
                x += 1
            elif x == 4:
                nota2 = float(i.strip())
                x += 1
            elif x == 5:
                nota3 = float(i.strip())
                x += 1
            elif x == 6:
                nota4 = float(i.strip())
                x += 1
            else:
                nota5 = float(i.strip())
                x = 0
                miEstudiante = Estudiante(cedula, nombre, edad, [nota1,nota2,nota3,nota4,nota5])
                #estoy creando un estudiante y para enviar 1 lista se envia entre corchetes de esa manera 
                listaEstudiantes.append(miEstudiante)
        return listaEstudiantes
