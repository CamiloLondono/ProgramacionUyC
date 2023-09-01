#from Baloto import Baloto
class serializacionBaloto():
    archivo = None
    def __init__(self):
        self.__archivo = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\laboratorios\\Labo 3\\archivobaloto.txt','a')
        def getArchivo(self):
            return self.__archivo
        def setArchivo(self,archivo):
            self.__archivo = archivo
        #funcion
        def escribirArchivoBaloto(self,dato):
            self.archivo = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\laboratorios\\Labo 3\\archivobaloto.txt','a')
            self.__archivo.write(dato)
            self.__archivo.close()
        def leerArchivoBaloto(self):
            self.__archivo = open('C:\\Users\\crist\\OneDrive\\Documentos\\Programacion\\Universidad\\segundo semestre\\laboratorios\\Labo 3\\archivobaloto.txt','r')
            x = 0
            fecha = ''
            baloto = []
            for i in self.__archivo:
                if x == 0:
                    fecha = i.strip()
                    x += 1
                elif x == 1:
                    baloto = i.strip()
                else:
                    x = 0
                    miBaloto = Baloto(fecha, baloto)
                    baloto.append(miBaloto)
            return baloto