import tkinter as tk
from tkinter import StringVar
from Usuario import Usuario

class AgregarUsuario():
    ventana = None
    
    def agregarUsuario(self, listaUsuarios, nombre, password):
        miUsuario = Usuario(nombre, password)
        listaUsuarios.append(miUsuario)
        print(listaUsuarios)

    def abrirVentana(self):
        self.ventana.mainloop()

    def __init__(self,menu):
        self.ventana = tk.Toplevel(menu)
        varNombre = StringVar()
        varPassword = StringVar()
        tk.Label(self.ventana, text='Agregar Usuario').grid(row=0, columnspan=1)
        tk.Label(self.ventana, text='Nombre de Usuario*:').grid(row=1, column=0)
        tk.Label(self.ventana, text='Password*:').grid(row=2, column=0)
        e1 = tk.Entry(self.ventana, textvariable=self.varNombre)
        e2 = tk.Entry(self.ventana, textvariable=self.varPassword)
        e1.grid(row=1, column=1) 
        e2.grid(row=2, column=1)
        botonAgregar = tk.Button(self.ventana, text='Ingresar', command= lambda: self.agregarUsuario(listaUsuarios, varNombre.get(), varPassword.get()))
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy)
        botonAgregar.grid(row=3, column=0)
        botonSalir.grid(row=3, column= 1)