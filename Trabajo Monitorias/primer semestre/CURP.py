import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

def abrir_calendario():
    top = tk.Toplevel(window)
    top.title("Seleccionar Fecha")

def generar_curp():
    # Obtener datos de la interfaz
    nombre = entry_nombre.get().upper()
    apellido_paterno = entry_apellido_paterno.get().upper()
    apellido_materno = entry_apellido_materno.get().upper()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    sexo = var_sexo.get().upper()
    estado = entry_estado.get().upper()

    # Obtener las primeras letras del apellido paterno, materno y nombre
    curp = apellido_paterno[0]

    # Obtener la primera vocal interna del apellido paterno
    for letra in apellido_paterno[1:]:
        if letra in 'AEIOU':
            curp += letra
            break

    # Obtener la primera letra del apellido materno
    curp += apellido_materno[0]

    # Obtener la primera letra del nombre
    curp += nombre[0]

    # Obtener la fecha de nacimiento en formato YYMMDD
    fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    curp += fecha.strftime("%y%m%d")

    # Agregar el sexo
    curp += sexo[0]

    # Agregar el estado
    curp += estado

    # Generar los últimos caracteres alfanuméricos de forma aleatoria
    import random
    caracteres_aleatorios = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    curp += caracteres_aleatorios

    # Mostrar el CURP generado
    label_curp.config(text="CURP: " + curp)


    def seleccionar_fecha():
        fecha_seleccionada = cal.get_date()
        fecha_objeto = datetime.strptime(fecha_seleccionada, "%m/%d/%y")
        entry_fecha_nacimiento.delete(0, tk.END)
        entry_fecha_nacimiento.insert(0, fecha_objeto.strftime("%d/%m/%Y"))
        btn_limpiar.pack()  # Mostrar el botón Limpiar
        entry_fecha_nacimiento.config(state="disabled")  # Deshabilitar el campo de fecha
        top.destroy()

    def limpiar_campos():
        entry_nombre.delete(0, tk.END)
        entry_apellido_paterno.delete(0, tk.END)
        entry_apellido_materno.delete(0, tk.END)
        entry_fecha_nacimiento.delete(0, tk.END)
        entry_fecha_nacimiento.config(state="normal")  # Habilitar el campo de fecha
        var_sexo.set("")  # Limpiar la selección de sexo
        entry_estado.delete(0, tk.END)
        label_curp.config(text="CURP:")
        btn_limpiar.pack_forget()  # Ocultar el botón Limpiar

    cal = Calendar(top, font="Arial 14", selectmode="day", year=2000, month=1, day=1)
    cal.pack(padx=20, pady=20)
    btn_seleccionar_fecha = tk.Button(top, text="Seleccionar Fecha", command=seleccionar_fecha)
    btn_seleccionar_fecha.pack(pady=10)
    btn_limpiar = tk.Button(top, text="Limpiar Campos", command=limpiar_campos)

# Crear la ventana principal
window = tk.Tk()
window.title("Generador de CURP")
window.geometry("400x400")

# Crear los elementos de la interfaz
label_nombre = tk.Label(window, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(window)
entry_nombre.pack()

label_apellido_paterno = tk.Label(window, text="Apellido Paterno:")
label_apellido_paterno.pack()
entry_apellido_paterno = tk.Entry(window)
entry_apellido_paterno.pack()

label_apellido_materno = tk.Label(window, text="Apellido Materno:")
label_apellido_materno.pack()
entry_apellido_materno = tk.Entry(window)
entry_apellido_materno.pack()

label_fecha_nacimiento = tk.Label(window, text="Fecha de Nacimiento:")
label_fecha_nacimiento.pack()
entry_fecha_nacimiento = tk.Entry(window)
entry_fecha_nacimiento.pack()

button_calendario = tk.Button(window, text="Abrir Calendario", command=abrir_calendario)
button_calendario.pack()

label_sexo = tk.Label(window, text="Sexo:")
label_sexo.pack()
var_sexo = tk.StringVar()
radio_hombre = tk.Radiobutton(window, text="Hombre", variable=var_sexo, value="M")
radio_mujer = tk.Radiobutton(window, text="Mujer", variable=var_sexo, value="F")
radio_hombre.pack()
radio_mujer.pack()

label_estado = tk.Label(window, text="Estado:")
label_estado.pack()
entry_estado = tk.Entry(window)
entry_estado.pack()

button_generar = tk.Button(window, text="Generar CURP", command=generar_curp)
button_generar.pack()

label_curp = tk.Label(window, text="CURP:")
label_curp.pack()

# Iniciar el bucle principal de la interfaz
window.mainloop()
