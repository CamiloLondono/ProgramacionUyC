import tkinter as tk
from AgregarUsuario import AgregarUsuario

class Menu():
    ventana = None
    listaUsuarios = []

    def abirVentana(self):
        self.ventana.mainloop()
    def agregarUsuario(self):
        miUsuario = AgregarUsuario(self.ventana, self.listaUsuarios)
        miUsuario.abrirVentana()

    def __init__(self,Loggin):#llega como parametro loggin que es la ventana raiz de la cual sera ejecutada
        self.ventana = tk.Toplevel() #el objeto de la ventana sera un Toplevel para podere crearse
        menu = tk.Menu(self.ventana) #recibe como primer parametro la ventana poder ser ejecutada
        self.ventana.config(menu=menu) 
        fileMenu = tk.Menu(menu)
        menu.add_cascade(label='Gestionar Usuarios', menu = fileMenu)
        #aca uso el metodo cascada para poder ejecutarse de manera correcta
        fileMenu.add_command(label='Agregar Usuario',command=lambda:self.agregarUsuario())
        fileMenu.add_separator() #el separator es para agregar una linea que separe los comandos uno del otro
        fileMenu.add_command(label='Modificar Usuario')
        fileMenu.add_separator()
        fileMenu.add_command(label='Eliminar Usuario')
        #para cada opcion creamos una nueva opcion que vaya a la barra de menu que esta acontinuacion
        searchMenu = tk.Menu(menu)
        menu.add_cascade(label='Consultar Usuarios',menu = searchMenu)
        searchMenu.add_command(label='Buscar Usuarios')
        #esta es la otra opcion
        exitMenu = tk.Menu(menu)
        menu.add_cascade(label='Salir',menu= exitMenu)
        exitMenu.add_command(label='Salir',command=self.ventana.destroy)