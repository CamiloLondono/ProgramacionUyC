import tkinter as tk
from datetime import datetime

def generar_curp():
    # Obtener datos de la interfaz
    nombre = entry_nombre.get().upper()
    apellido_paterno = entry_apellido_paterno.get().upper()
    apellido_materno = entry_apellido_materno.get().upper()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    sexo = entry_sexo.get().upper()
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

# Crear la ventana principal
window = tk.Tk()
window.title("Generador de CURP")
window.geometry("300x200")

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

label_fecha_nacimiento = tk.Label(window, text="Fecha de Nacimiento (dd/mm/yyyy):")
label_fecha_nacimiento.pack()
entry_fecha_nacimiento = tk.Entry(window)
entry_fecha_nacimiento.pack()

label_sexo = tk.Label(window, text="Sexo (M/F):")
label_sexo.pack()
entry_sexo = tk.Entry(window)
entry_sexo.pack()

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