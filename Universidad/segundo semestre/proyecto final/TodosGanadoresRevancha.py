__author__="Camilo Londoño"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
import tkinter as tk
from tkinter import StringVar

class TodosGanadoresRevancha():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()
    
    def imprimirTodosRevancha(self,administrador,listaRevancha,todosRevancha):
        administrador.consultarTodosResultadoRevancha(listaRevancha,todosRevancha)
    
    def __init__(self,MenuAdmin,administrador,listaRevancha):
        self.ventana = tk.Toplevel(MenuAdmin)
    #campos de texto
        self.__todosRevancha = StringVar()
    #label
        tk.Label(self.ventana, text='El resultado de todas las revanchas es').grid(row=0, column=0,columns=3)
        tk.Label(self.ventana, textvariable=self.__todosRevancha, command=self.imprimirTodosRevancha(administrador, listaRevancha, self.__todosRevancha)).grid(row=1, column=0, columns=3)
    #botones
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=2, column=1)
    