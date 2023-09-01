__author__="Camilo Londoño"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
import tkinter as tk
from tkinter import *

class EliminarV():
    ventana = None

    def Limpiar(self, varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion):
        self.__varCedula.set('')
        self.__varNombre.set('')
        self.__varApellido.set('')
        self.__varEdad.set('')
        self.__varTelefono.set('')
        self.__varEmail.set('')
        self.__varDireccion.set('')

    def eliminarVendedor(self,administrador,varCedula,listaUsuarios):
        administrador.eliminarVendedor(varCedula, listaUsuarios)
    
    def buscarCedula(self,administrador,varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,listaUsuarios):
        administrador.buscarCedula(varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,listaUsuarios)

    def abrirVentana(self):
        self.ventana.mainloop()

    def __init__(self,MenuAdmin,administrador,listaUsuarios):
        self.ventana = tk.Toplevel(MenuAdmin)
        self.admin = administrador
        self.lista = listaUsuarios
    # espacios de texto
        self.__varCedula = StringVar()
        self.__varNombre = StringVar()
        self.__varApellido = StringVar()
        self.__varEdad = StringVar()
        self.__varTelefono = StringVar()
        self.__varEmail = StringVar()
        self.__varDireccion = StringVar()
    # Datos a pedir
        tk.Label(self.ventana, text='Eliminar Vendedor').grid(row=0, columns=2)
        tk.Label(self.ventana, text='Cédula*:').grid(row=1, column=0)
        tk.Label(self.ventana, text='Nombres*:').grid(row=2, column=0)
        tk.Label(self.ventana, text='Apellidos*:').grid(row=3, column=0)
        tk.Label(self.ventana, text='Edad*:').grid(row=4, column=0)
        tk.Label(self.ventana, text='Telefono*:').grid(row=5, column=0)
        tk.Label(self.ventana, text='Email*:').grid(row=6, column=0)
        tk.Label(self.ventana, text='Dirección*:').grid(row=7, column=0)
    # campos de texto
        entrada1 = tk.Entry(self.ventana, textvariable=self.__varCedula).grid(row=1, column=1)
        entrada2 = tk.Entry(self.ventana, textvariable=self.__varNombre, state='disabled').grid(row=2, column=1)
        entrada3 = tk.Entry(self.ventana, textvariable=self.__varApellido, state='disabled').grid(row=3, column=1)
        entrada4 = tk.Entry(self.ventana, textvariable=self.__varEdad, state='disabled').grid(row=4, column=1)
        entrada5 = tk.Entry(self.ventana, textvariable=self.__varTelefono, state='disabled').grid(row=5, column=1)
        entrada6 = tk.Entry(self.ventana, textvariable=self.__varEmail, state='disabled').grid(row=6, column=1)
        entrada7 = tk.Entry(self.ventana, textvariable=self.__varDireccion, state='disabled').grid(row=7, column=1)
    # botones
        botonAgregar = tk.Button(self.ventana, text='Eliminar', command=lambda:self.eliminarVendedor(self.admin, self.__varCedula, self.lista)).grid(row=9, column=0)
        botonLimpiar = tk.Button(self.ventana, text='Limpiar', command=lambda:self.Limpiar(self.__varCedula,self.__varNombre,self.__varApellido,self.__varEdad,self.__varTelefono,self.__varEmail,self.__varDireccion)).grid(row=9, column=1)
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=9, column=2)
        botonBuscar = tk.Button(self.ventana, text='Buscar', command=lambda:self.buscarCedula(self.admin, self.__varCedula,self.__varNombre,self.__varApellido,self.__varEdad,self.__varTelefono,self.__varEmail,self.__varDireccion, self.lista)).grid(row=1, column=2)