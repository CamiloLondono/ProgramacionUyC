__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
import tkinter as tk
from CrearV import CrearV
from EliminarV import EliminarV
from CrearBaloto import CrearBaloto
from CrearRevancha import CrearRevancha
from GanadorBalotoRevancha import GanadorBalotoRevancha
from SerializacionBaloto import SerializacionBaloto
from SerializacionRevancha import SerializacionRevancha
from TodosGanadoresBaloto import TodosGanadoresBaloto
from TodosGanadoresRevancha import TodosGanadoresRevancha

class MenuAdmin():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()
    
    def crearVendedor(self,admin):
        miVendedor = CrearV(self.ventana, admin)
        miVendedor.abrirVentana()
    
    def crearTodosBaloto(self,admin,listaBaloto):
        miTodosBaloto = TodosGanadoresBaloto(self.ventana,admin,listaBaloto)
        miTodosBaloto.abrirVentana()
    
    def crearTodosRevancha(self,admin,listaRevancha):
        miTodosRevancha = TodosGanadoresRevancha(self.ventana,admin,listaRevancha)
        miTodosRevancha.abrirVentana()

    def ganadorBalotoyRevancha(self,admin,listaBaloto,listaRevancha):
        miGanador = GanadorBalotoRevancha(self.ventana, admin,listaBaloto,listaRevancha)
        miGanador.abrirVentana()

    def eliminarVendedor(self,admin,lista):
        miEliminado = EliminarV(self.ventana, admin, lista)
        miEliminado.abrirVentana()

    def crearBaloto(self,admin):
        miBaloto = CrearBaloto(self.ventana, admin)
        miBaloto.abrirVentana()

    def crearRevancha(self,admin):
        miRevancha = CrearRevancha(self.ventana, admin)
        miRevancha.abrirVentana()

    def __init__(self,loggin,administrador,listaUsuarios):
        miSerializacionBaloto = SerializacionBaloto()
        self.__listaBaloto = miSerializacionBaloto.leerBaloto()
        miSerializacionRevancha = SerializacionRevancha()
        self.__listaRevancha = miSerializacionRevancha.leerRevancha()
        self.admin = administrador
        self.lista = listaUsuarios
        self.ventana = tk.Toplevel()
        self.ventana.geometry('500x300')
        menu = tk.Menu(self.ventana)
        self.ventana.config(menu=menu)
        tk.Label(self.ventana, text='~~~Bienvenido Administrador~~~').grid(row=0, columns=2)
        datosMenu = tk.Menu(menu)
        menu.add_cascade(label='Gestionar Vendedores', menu= datosMenu)
        datosMenu.add_command(label='Crear Vendedor', command=lambda:self.crearVendedor(self.admin))
        datosMenu.add_separator()
    #separador
        datosMenu.add_command(label='Eliminar Vendedor', command=lambda:self.eliminarVendedor(self.admin,self.lista))
    #siguiente opcion el la barra
        gestionarMenu = tk.Menu(menu)
        menu.add_cascade(label='Gestionar Sorteos', menu= gestionarMenu)
        gestionarMenu.add_command(label='Realizar Sorteo Baloto', command=lambda:self.crearBaloto(self.admin))
        gestionarMenu.add_separator()
    #separador
        gestionarMenu.add_command(label='Realizar Sorteo Revancha', command=lambda:self.crearRevancha(self.admin))
    #siguiente opcion en la barra
        consultarMenu = tk.Menu(menu)
        menu.add_cascade(label='Consultar Informacion', menu= consultarMenu)
        consultarMenu.add_command(label='Consultar Ganador del Día', command=lambda:self.ganadorBalotoyRevancha(self.admin,self.__listaBaloto,self.__listaRevancha))
        consultarMenu.add_separator()
    #separador
        consultarMenu.add_command(label='Consultar Todos los Resultados Baloto', command=lambda:self.crearTodosBaloto(self.admin, self.__listaBaloto))
        consultarMenu.add_separator()
    #separador
        consultarMenu.add_command(label='Consultar Todos los Resultados Revancha',command=lambda:self.crearTodosRevancha(self.admin, self.__listaRevancha))
    #siguiente opcion en la barra
        salirMenu = tk.Menu(menu)
        menu.add_cascade(label='Salir', menu=salirMenu)
        salirMenu.add_command(label='Salir',command=self.ventana.destroy)