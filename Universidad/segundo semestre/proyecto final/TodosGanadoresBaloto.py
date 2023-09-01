__author__="Steven Cordoba Rodriguez"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Corsoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
import tkinter as tk
from tkinter import StringVar

class TodosGanadoresBaloto():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()
    
    def imprimirTodosBaloto(self,administrador,listaBaloto,todosBaloto):
        administrador.consultarTodosResultadosBaloto(listaBaloto,todosBaloto)
    
    def __init__(self,MenuAdmin,administrador,listaBaloto):
        self.ventana = tk.Toplevel(MenuAdmin)
    #campos de texto
        self.__todosBaloto = StringVar()
    #label
        tk.Label(self.ventana, text='El resultado de todos los balotos es').grid(row=0, column=0,columns=3)
        tk.Label(self.ventana, textvariable=self.__todosBaloto, command=s).grid(row=1, column=0, columns=3)
    #botones
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=2, column=1)
    