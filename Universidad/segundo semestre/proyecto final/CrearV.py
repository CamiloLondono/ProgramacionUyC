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

class CrearV():
    ventana = None

    def Limpiar(self,varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,varPassword):
        varCedula.set('')
        varNombre.set('')
        varApellido.set('')
        varEdad.set('')
        varTelefono.set('')
        varEmail.set('')
        varDireccion.set('')
        varPassword.set('')

    def crearVendedor(self,administrador,varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,varPassword):
        administrador.crearVendedor(varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,varPassword)


    def abrirVentana(self):
        self.ventana.mainloop()

    def __init__(self,MenuAdmin,administrador):
        self.admin = administrador
        self.ventana = tk.Toplevel(MenuAdmin)
    # espacios de texto
        self.__varCedula = StringVar()
        self.__varNombre = StringVar()
        self.__varApellido = StringVar()
        self.__varEdad = StringVar()
        self.__varTelefono = StringVar()
        self.__varEmail = StringVar()
        self.__varDireccion = StringVar()
        self.__varPassword = StringVar()
    # Datos a pedir
        tk.Label(self.ventana, text='Crear Vendedor').grid(row=0, columns=2)
        tk.Label(self.ventana, text='Cédula*:').grid(row=1, column=0)
        tk.Label(self.ventana, text='Nombres*:').grid(row=2, column=0)
        tk.Label(self.ventana, text='Apellidos*:').grid(row=3, column=0)
        tk.Label(self.ventana, text='Edad*:').grid(row=4, column=0)
        tk.Label(self.ventana, text='Telefono*:').grid(row=5, column=0)
        tk.Label(self.ventana, text='Email*:').grid(row=6, column=0)
        tk.Label(self.ventana, text='Dirección*:').grid(row=7, column=0)
        tk.Label(self.ventana, text='Password*:').grid(row=8, column=0)
    # campos de texto
        entrada1 = tk.Entry(self.ventana, textvariable=self.__varCedula).grid(row=1, column=1)
        entrada2 = tk.Entry(self.ventana, textvariable=self.__varNombre).grid(row=2, column=1)
        entrada3 = tk.Entry(self.ventana, textvariable=self.__varApellido).grid(row=3, column=1)
        entrada4 = tk.Entry(self.ventana, textvariable=self.__varEdad).grid(row=4, column=1)
        entrada5 = tk.Entry(self.ventana, textvariable=self.__varTelefono).grid(row=5, column=1)
        entrada6 = tk.Entry(self.ventana, textvariable=self.__varEmail).grid(row=6, column=1)
        entrada7 = tk.Entry(self.ventana, textvariable=self.__varDireccion).grid(row=7, column=1)
        entrada8 = tk.Entry(self.ventana, textvariable=self.__varPassword).grid(row=8, column=1)
    # botones
        botonAgregar = tk.Button(self.ventana, text='Agregar', command=lambda:self.crearVendedor(self.admin,self.__varCedula,self.__varNombre,self.__varApellido,self.__varEdad,self.__varTelefono,self.__varEmail,self.__varDireccion,self.__varPassword)).grid(row=9, column=0)
        
        botonLimpiar = tk.Button(self.ventana, text='Limpiar', command=lambda:self.Limpiar(self.__varCedula,self.__varNombre,self.__varApellido,self.__varEdad,self.__varTelefono,self.__varEmail,self.__varDireccion,self.__varPassword)).grid(row=9, column=1)
        
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=9, column=2)