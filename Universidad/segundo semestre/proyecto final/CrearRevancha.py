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

class CrearRevancha():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()
    
    def crearRevancha(self,administrador, varNum1, varNum2, varNum3, varNum4, varNum5, varNum6):
        administrador.realizarSorteoRevancha(varNum1, varNum2, varNum3, varNum4, varNum5, varNum6)

    def __init__(self,MenuAdmin,administrador):
        self.ventana = tk.Toplevel(MenuAdmin)
    #campos de texto
        self.__varNum1 = StringVar()
        self.__varNum2 = StringVar()
        self.__varNum3 = StringVar()
        self.__varNum4 = StringVar()
        self.__varNum5 = StringVar()
        self.__varNum6 = StringVar()
    #datos
        tk.Label(self.ventana, text='Realizar Sorteo Revancha').grid(row=0, columns=6)
        tk.Label(self.ventana, text='Números*:').grid(row=1, column=0)
    #entradas
        entrada1 = tk.Entry(self.ventana,width=5, textvariable=self.__varNum1).grid(row=1, column=1)
        entrada2 = tk.Entry(self.ventana,width=5, textvariable=self.__varNum2).grid(row=1, column=2)
        entrada3 = tk.Entry(self.ventana,width=5, textvariable=self.__varNum3).grid(row=1, column=3)
        entrada4 = tk.Entry(self.ventana,width=5, textvariable=self.__varNum4).grid(row=1, column=4)
        entrada5 = tk.Entry(self.ventana,width=5, textvariable=self.__varNum5).grid(row=1, column=5)
        entrada6 = tk.Entry(self.ventana,width=5, textvariable=self.__varNum6).grid(row=1, column=6)
    #botones
        botonSortear = tk.Button(self.ventana, text='Sortear', command=lambda:self.crearRevancha(administrador, self.__varNum1, self.__varNum2, self.__varNum3, self.__varNum4, self.__varNum5, self.__varNum6)).grid(row=2, column=1, columns=3)
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=2, column=4, columns=3)