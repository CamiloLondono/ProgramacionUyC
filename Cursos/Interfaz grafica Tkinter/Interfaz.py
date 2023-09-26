import tkinter as tk
from tkinter import *

#VENTANA DEL PROGRAMA

ventana = tk.Tk() #creo objero de clase tkinter para crear interfaz
ventana.title('Mi ventana') #llamo el .title para agregar titulos a las ventanas creadas
ventana.geometry('800x500+300+100') #agregar tamaño, primer valor es el ancho(coordenada x) y el segundo es largo(coordenada y)

#CREACION WIDGETS

etiqueta = tk.Label(ventana, 
    text='titulo de la aplicacion',
    font='console 20 bold', #font es el tipo de letra, con tamaño y negrilla
    bg='lightblue', #fondo de la letra
    fg='red', #fg = foreground que es para cambiar el color de la letra
    padx=20, pady=20, #distancia del borde de la etiqueta
    relief=tk.RAISED, #me da un borde en el marco de le etiqueta, groove y sunken tambien tan bordes
    border=10) #tamaño del borde  
etiqueta.pack() #pack me da la ubucacion de la etiqueta


#BUCLE PRINCIPAL VENTANA

ventana.mainloop() #llamo la funcion mainloop para que se ejecute en bucle toda la informacion de la ventana

#APUNTES DE FUNCIONES Y COMENTARIOS

#ventana.resizable(width=False, height=False) sirve para bloquear el ahcer mas grande una ventana
#ventana.minsize(width=50, height=50) sirve para decir cual es el ancho y largo minimo de una ventana
#ventana.maxsize(width=1000, height=500) sirve para decir cual es el ancho y largo maximo de una ventana
'''ventana.configure(background='blue') Sirve para ponerle color al fondo de una ventana
se pueden abreviar funciones, configure se puede poner config y background se puede poner bg'''

