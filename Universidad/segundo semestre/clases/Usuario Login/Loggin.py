import tkinter as tk
from tkinter import StringVar
from Usuario import Usuario
from Menu import Menu

class Loggin():
    """Clase que representa la interfaz de usuario para realizar loggin. """
    ventana = tk.Tk() #declarando variable de tipo tk, lo muestra el '.' al ser usado
    varNombre = StringVar() #variable declarada en ambito global para ser usada en todo momento 
    varPassword = StringVar()

    def abirVentana(self):
        self.ventana.mainloop()
        
    def validarUsuario(self, usuario):
        sesion = False
        if (self.varNombre.get() == usuario.getNombre() and self.varPassword.get() == usuario.getPassword()): #comprobamos si lo que esta en los campos de texto es la misma informacion que esta guardada en el objeto
            sesion = True
        else:
            pass
        if (sesion == True):
            #abrir ventana principal
            miMenu = Menu(self.ventana)
            miMenu.abirVentana()
        else:
            print('Usuario y/o Password errados, por favor intente de nuevo')

    def __init__(self):
        miUsuario = Usuario('camilo', '123') #objeto creado de la clase usuario 
        tk.Label(self.ventana, text='Loggin').grid(row=0, columnspan=2) #usamos el self, porque la variable esta declarada en el objeto, row significa fila y el cero porque esta ubicada en la fila 0
        tk.Label(self.ventana, text='Nombre de Usuario*:').grid(row=1, column=0)
        tk.Label(self.ventana, text='Password*:').grid(row=2, column=0)
        e1 = tk.Entry(self.ventana, textvariable=self.varNombre) #entry es la caja de texto
        e2 = tk.Entry(self.ventana, textvariable=self.varPassword)
        e1.grid(row=1, column=1) #se ubican al frente de las etiquetas que las asocian
        e2.grid(row=2, column=1)
        botonIngresar = tk.Button(self.ventana, text='Entrar', command=lambda:self.validarUsuario(miUsuario))
        #la palabra reservada lambda me sirve para dejar pausada la funcion y no se ejecute automaticamente
        botonSalir = tk.Button(self.ventana, text='Salir', command=self.ventana.destroy) #se usa el destroy para destruir la ventana
        botonIngresar.grid(row=3, column=0)
        botonSalir.grid(row=3, column= 1)