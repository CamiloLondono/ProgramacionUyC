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

class VenderRevancha():
    ventana = None

    def abrirVentana(self):
        self.ventana.mainloop()

    def venderBoletoRevancha(self,vendedor,varId,varFecha,varCedula,varNum1,varNum2,varNum3,varNum4,varNum5,varNum6):
        vendedor.venderBoletoRevancha(varId,varFecha,varCedula,varNum1,varNum2,varNum3,varNum4,varNum5,varNum6)

    def Limpiar(self,varCedula,varNum1,varNum2,varNum3,varNum4,varNum5,varNum6):
        varCedula.set('')
        varNum1.set('')
        varNum2.set('')
        varNum3.set('')
        varNum4.set('')
        varNum4.set('')
        varNum5.set('')
        varNum6.set('')

    def __init__(self,MenuUsuario,vendedor):
        self.ventana = tk.Toplevel(MenuUsuario)
    #campos de texto
        self.__varId = StringVar()
        self.__varFecha = StringVar()
        self.__varCedula = StringVar()
        self.__varNum1 = StringVar()
        self.__varNum2 = StringVar()
        self.__varNum3 = StringVar()
        self.__varNum4 = StringVar()
        self.__varNum5 = StringVar()
        self.__varNum6 = StringVar()
    #datos
        tk.Label(self.ventana, text='Vender Boleto Revancha').grid(row=0, columns=6)
        tk.Label(self.ventana, text='ID*:').grid(row=1, column=0)
        tk.Label(self.ventana, text='Fecha*:').grid(row=2, column=0)
        tk.Label(self.ventana, text='Cedula:').grid(row=3, column=0)
        tk.Label(self.ventana, text='Números*:').grid(row=4, column=0)
    #entradas
        entradaId = tk.Entry(self.ventana, textvariable=self.__varId, state='disabled').grid(row=1, column=1)
        entradaFecha = tk.Entry(self.ventana, textvariable=self.__varFecha, state='disabled').grid(row=2, column=1)
        entradaCedula = tk.Entry(self.ventana, textvariable=self.__varCedula).grid(row=3, column=1)
        entrada1 = tk.Entry(self.ventana,width=4, textvariable=self.__varNum1).grid(row=4, column=1)
        entrada2 = tk.Entry(self.ventana,width=4, textvariable=self.__varNum2).grid(row=4, column=2)
        entrada3 = tk.Entry(self.ventana,width=4, textvariable=self.__varNum3).grid(row=4, column=3)
        entrada4 = tk.Entry(self.ventana,width=4, textvariable=self.__varNum4).grid(row=4, column=4)
        entrada5 = tk.Entry(self.ventana,width=4, textvariable=self.__varNum5).grid(row=4, column=5)
        entrada6 = tk.Entry(self.ventana,width=4, textvariable=self.__varNum6).grid(row=4, column=6)
    #botones
        botonVender = tk.Button(self.ventana, text='Vender', command=lambda:self.venderBoletoRevancha(vendedor, self.__varId, self.__varFecha, self.__varCedula, self.__varNum1, self.__varNum2, self.__varNum3, self.__varNum4, self.__varNum5, self.__varNum6)).grid(row=5, column=0)
        botonLimpiar = tk.Button(self.ventana, text='Limpiar', command=lambda:self.Limpiar(self.__varCedula, self.__varNum1, self.__varNum2, self.__varNum3, self.__varNum4, self.__varNum5, self.__varNum6)).grid(row=5, column=1)
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=5, column=2)