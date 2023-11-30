cadena = "Hola, mundo!"
longitud = len(cadena)
print("Longitud de la cadena:", longitud)

subcadena = cadena[1:4]  # Obtiene los caracteres en las posiciones 1, 2 y 3
print("Subcadena:", subcadena)


cadena_con_espacios = "    Hola, mundo!    "
cadena_sin_espacios = cadena_con_espacios.strip()
print(cadena_sin_espacios)
print(cadena_con_espacios)