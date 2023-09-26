import tkinter as tk

##### VENTANA DEL PROGRAMA #####

ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.minsize(width=200, height=300)

##### LABEL TITULO #####

titulo = tk.Label(ventana,
	text="CONTADOR",
	font="arial 24",
	bg="lightgreen", fg="darkgreen",
	relief=tk.GROOVE, #pone un marco a raz con la letra
	padx=20, pady=20) #el espacio del texto en comparacion con el texto
titulo.pack()

##### LABEL NUMERO #####

numero = tk.Label(ventana, 
    text= 0,
    font ='arial 48',
    bg="darkgreen", fg="lightgreen",
    padx=20, pady=20)
numero.pack()

##### BOTON CONTAR #####

anadir = tk.Button(ventana, 
    text="CONTAR",
    font ="arial 18",
    bg="lightgreen", fg="black",
    padx=50, pady=10, 
    relief="groove", bd=8)
anadir.pack()

##### BUCLE PRINCIPAL PROGRAMA #####

ventana.mainloop()