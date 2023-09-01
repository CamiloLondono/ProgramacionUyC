__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
import tkinter as tk
from VenderBaloto import VenderBaloto
from VenderRevancha import VenderRevancha
from GanadorBalotoRevancha import GanadorBalotoRevancha
from SerializacionBaloto import SerializacionBaloto
from SerializacionRevancha import SerializacionRevancha


class MenuUsuario():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()

    def venderBaloto(self,vendedor):
        miBaloto = VenderBaloto(self.ventana,vendedor)
        miBaloto.abrirVentana()
    
    def VenderRevancha(self,vendedor):
        miRevancha = VenderRevancha(self.ventana,vendedor)
        miRevancha.abrirVentana()

    def ganadorBalotoyRevancha(self,vendedor,listaBaloto,listaRevancha):
        miGanador = GanadorBalotoRevancha(self.ventana, vendedor, listaBaloto, listaRevancha)
        miGanador.abrirVentana()

    def __init__(self,loggin,vendedor):
        self.ventana = tk.Toplevel()
        self.ventana.geometry('500x300')
        miSerializacionBaloto = SerializacionBaloto()
        self.__listaBaloto = miSerializacionBaloto.leerBaloto()
        miSerializacionRevancha = SerializacionRevancha()
        self.__listaRevancha = miSerializacionRevancha.leerRevancha()
        self.vendedor = vendedor
        menu = tk.Menu(self.ventana)
        self.ventana.config(menu=menu)
        tk.Label(self.ventana, text='~~~Bienvenido Vendedor~~~').grid(row=0, columns=2)
        ventaMenu = tk.Menu(menu)
        menu.add_cascade(label='Gestionar Boletos', menu= ventaMenu)
        ventaMenu.add_command(label='Vender Boleto Baloto', command=lambda:self.venderBaloto(self.vendedor))
        ventaMenu.add_separator()
    #separador
        ventaMenu.add_command(label='Vender Boleto Revancha', command=lambda:self.VenderRevancha(self.vendedor))
    #siguiente opcion el la barra
        gestionarMenu = tk.Menu(menu)
        menu.add_cascade(label='Consultar Informacion', menu= gestionarMenu)
        gestionarMenu.add_command(label='Consultar Ganador del Día', command=lambda:self.ganadorBalotoyRevancha(self.vendedor, self.__listaBaloto, self.__listaRevancha))
    #botones 
        salirMenu = tk.Menu(menu)
        menu.add_cascade(label='Salir', menu=salirMenu)
        salirMenu.add_command(label='Salir',command=self.ventana.destroy)