import tkinter as tk
from tkinter import *

ventana = tk.Tk()
ventana.title('Calculadora')

titulo = tk.Label(ventana, text='Mi Calculadora')
titulo.grid(row=0, column=0, columnspan=4)

#variables
operacion = StringVar()
resultadooperaciones = StringVar()
i = 0
#funciones de botones y limpieza
def limpiar():
    operacion.set('')
    resultadooperaciones.set('')

def agregarnumero1():
    operacion.set(operacion.get()+'1')

def agregarnumero2():
    operacion.set(operacion.get()+'2')

def agregarnumero3():
    operacion.set(operacion.get()+'3')

def agregarnumero4():
    operacion.set(operacion.get()+'4')

def agregarnumero5():
    operacion.set(operacion.get()+'5')

def agregarnumero6():
    operacion.set(operacion.get()+'6')

def agregarnumero7():
    operacion.set(operacion.get()+'7')

def agregarnumero8():
    operacion.set(operacion.get()+'8')

def agregarnumero9():
    operacion.set(operacion.get()+'9')

def agregarnumero0():
    operacion.set(operacion.get()+'0')

def agregarsuma():
    operacion.set(operacion.get()+'+')

def agregarresta():
    operacion.set(operacion.get()+'-')

def agregardivision():
    operacion.set(operacion.get()+'/')

def agregarnmultiplicacion():
    operacion.set(operacion.get()+'x')

def agregarpunto():
    operacion.set(operacion.get()+'.')

#operacionesmatematicas

def operacionmatematica():
    listaprincipal = operacion.get()
    for i in listaprincipal:
        if i == '+':
            operador = listaprincipal.index('+')
            listaizquierda = float(listaprincipal[:operador])
            listaderecha = float(listaprincipal[operador+1:])
            suma = listaizquierda + listaderecha
            resultadooperaciones.set(suma)
        if i == '-':
            operador = listaprincipal.index('-')
            listaizquierda = float(listaprincipal[:operador])
            listaderecha = float(listaprincipal[operador+1:])
            resta = listaizquierda - listaderecha
            resultadooperaciones.set(resta)
        if i == 'x':
            operador = listaprincipal.index('x')
            listaizquierda = float(listaprincipal[:operador])
            listaderecha = float(listaprincipal[operador+1:])
            multiplicacion = listaizquierda * listaderecha
            resultadooperaciones.set(multiplicacion)
        if i == '/':
            operador = listaprincipal.index('/')
            listaizquierda = float(listaprincipal[:operador])
            listaderecha = float(listaprincipal[operador+1:])
            if listaderecha == 0:
                resultadooperaciones.get(resultadooperaciones.set('error'))
            else:
                division = listaizquierda / listaderecha
                resultadooperaciones.set(division)
        if '+' not in listaprincipal and '-' not in listaprincipal and 'x' not in listaprincipal and '/' not in listaprincipal:
            resultadooperaciones.set(listaprincipal)

#botones generales:
#entrada
calculo = tk.Entry(ventana, textvariable=operacion)
calculo.config(state='disabled')
resultado = tk.Entry(ventana, textvariable=resultadooperaciones)
resultado.config(state='disabled')

#operaciones
botonigual = tk.Button(ventana, text='=', command=operacionmatematica)
botondividir = tk.Button(ventana, text='/', command=agregardivision)
botonmultiplicar = tk.Button(ventana, text='x', command=agregarnmultiplicacion)
botonresta = tk.Button(ventana, text='-', command=agregarresta)
botonsuma = tk.Button(ventana, text='+', command=agregarsuma)

#numeros
boton1 = tk.Button(ventana, text='1', command=agregarnumero1)
boton2 = tk.Button(ventana, text='2', command=agregarnumero2)
boton3 = tk.Button(ventana, text='3', command=agregarnumero3)
boton4 = tk.Button(ventana, text='4', command=agregarnumero4)
boton5 = tk.Button(ventana, text='5', command=agregarnumero5)
boton6 = tk.Button(ventana, text='6', command=agregarnumero6)
boton7 = tk.Button(ventana, text='7', command=agregarnumero7)
boton8 = tk.Button(ventana, text='8', command=agregarnumero8)
boton9 = tk.Button(ventana, text='9', command=agregarnumero9)
boton0 = tk.Button(ventana, text='0', command=agregarnumero0)

#otros
botonpunto = tk.Button(ventana, text='.', command=agregarpunto)
botonlimpiar = tk.Button(ventana, text='Limpiar', width=15, command=limpiar)
botonsalir = tk.Button(ventana, text='Salir', command=ventana.destroy)

#grids
calculo.grid(row=1, column=0, columnspan=4)
resultado.grid(row=2, column=0, columnspan=4)
botonmultiplicar.grid(row=4, column=3, padx= 5, pady=5)
botonresta.grid(row=5, column=3, padx= 5, pady=5)
botondividir.grid(row=3, column=3, padx= 5, pady=5)
boton7.grid(row=3, column=0, padx= 5, pady=5)
boton8.grid(row=3, column=1, padx= 5, pady=5)
boton9.grid(row=3, column=2, padx= 5, pady=5)
boton4.grid(row=4, column=0, padx= 5, pady=5)
boton5.grid(row=4, column=1, padx= 5, pady=5)
boton6.grid(row=4, column=2, padx= 5, pady=5)
boton1.grid(row=5, column=0, padx= 5, pady=5)
boton2.grid(row=5, column=1, padx= 5, pady=5)
botonpunto.grid(row=6, column=1, padx= 5, pady=5)
boton3.grid(row=5, column=2, padx= 5, pady=5)
boton0.grid(row=6, column=0, padx= 5, pady=5)
botonigual.grid(row=6, column=2, padx= 5, pady=5)
botonsuma.grid(row=6, column=3, padx= 5, pady=5)
botonlimpiar.grid(row=7, column=0, columnspan=2)
botonsalir.grid(row=7, column=2, columnspan=2)

ventana.mainloop()