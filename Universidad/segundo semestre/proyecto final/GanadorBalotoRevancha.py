__author__="Juan Pablo Bernal"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
import tkinter as tk
from tkinter import StringVar

class GanadorBalotoRevancha():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()
    
    def GanadorBalotoRevanchaDia(self,administrador,listaBaloto,listaRevancha,varBaloto, varRevancha):
        administrador.consultarGanadorDia(listaBaloto,listaRevancha,varBaloto,varRevancha)
    
    def __init__(self, MenuAdmin, administrador, listaBaloto,listaRevancha):
        self.ventana = tk.Toplevel(MenuAdmin)
    #campos de texto
        self.__varBaloto = StringVar()
        self.__varRevancha = StringVar()
    #datos mostrados
        tk.Label(self.ventana, text='Los numeros ganadores fueron').grid(row=0, columns=2)
        tk.Label(self.ventana, text='Baloto').grid(row=1, column= 0)
        tk.Label(self.ventana, text='Revancha').grid(row=2, column=0)
    # entradas
        entrada1 = tk.Entry(self.ventana, textvariable=self.__varBaloto).grid(row=1, column=1)
        entrada2 = tk.Entry(self.ventana, textvariable=self.__varRevancha).grid(row=2, column=1)
    #botones
        botonMostrar = tk.Button(self.ventana, text='Mostrar', command=lambda:self.GanadorBalotoRevanchaDia(administrador, listaBaloto,listaRevancha, self.__varBaloto, self.__varRevancha)).grid(row=3, column=0)
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=3, column=1)