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
from MenuAdmin import MenuAdmin
from MenuUsuario import MenuUsuario
from SerializacionUsuarios import SerializacionUsuarios
from Administrador import Administrador
from Vendedor import Vendedor
class Loggin():
    """clase que representa la interfaz de realizar loggin"""
    ventana = tk.Tk() #variables de ambito globlal
    ventana.title('La suerte')
    ventana.geometry('250x100')
    varNombre = StringVar() #variables de ambito globlal
    varPassword = StringVar() #variables de ambito globlal

    def abrirVentana(self):
        self.ventana.mainloop()
    
    def validarUsuario(self,listaUsuarios):
        if len(listaUsuarios) > 0:
            sesion = False
    #administrador verificacion
            for i in listaUsuarios:
                if (self.varNombre.get() == i.getNombre() and self.varPassword.get() == i.getPassword()): 
                    sesion = True
                    if ("Administrador" == i.getRol()):
                        admin = Administrador(i.getCedula(),i.getNombre(),i.getApellido(),i.getEdad(),i.getTelefono(),i.getEmail(),i.getDireccion(),i.getRol(),i.getPassword())
                        miMenu = MenuAdmin(self.ventana,admin,listaUsuarios) #objeto de la clase menu
                        miMenu.abrirVentana()
                    else:
                        vendedor = Vendedor(i.getCedula(),i.getNombre(),i.getApellido(),i.getEdad(),i.getTelefono(),i.getEmail(),i.getDireccion(),i.getRol(),i.getPassword())
                        miMenu2 = MenuUsuario(self.ventana,vendedor)
                        miMenu2.abrirVentana()
                else:
                    pass
            if sesion == False:
                print('Usuario y/o password no coinciden, por favor intente de nuevo')

    def __init__(self):
        listaUsuarios = []
        miSerializacionUsuarios = SerializacionUsuarios()
        listaUsuarios = miSerializacionUsuarios.leerArchivoUsuarios()
    # texto mostrado en la ventada
        tk.Label(self.ventana, text='Iniciar Sesión').grid(row=0, columns=2)
        tk.Label(self.ventana, text='Nombre Usuario*').grid(row=1, column=0)
        tk.Label(self.ventana, text='Password*').grid(row=2, column=0)
    # campos de textos generados en la ventana
        entrada1 = tk.Entry(self.ventana, textvariable=self.varNombre).grid(row=1, column=1)
        entrada2 = tk.Entry(self.ventana, textvariable=self.varPassword, show= '*').grid(row=2, column=1)
    # botones
        botonIngresar = tk.Button(self.ventana, text='Entrar', command=lambda:self.validarUsuario(listaUsuarios)).grid(row=3, column=0)
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy).grid(row=3, column=1)