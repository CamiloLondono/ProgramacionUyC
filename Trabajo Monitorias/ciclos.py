'''
#ejercicio 1
hora = int(input('por favor digite la hora: '))
minutos = int(input('por favor digite los minutos: '))
print ('la hora dada es ',hora,':',minutos)
if minutos >= 59: # aca se verifica si los minutos dados son iguales o mayores a 59 se cambia la hora y los minutos se reinician
    hora += 1
    minutos = '00'
    print ('la hora un minuto despues es ',hora,':',minutos)
else:
    hora = hora
    minutos += 1
    print ('la hora un minuto despues es ',hora,':',minutos)
------------------------
#ejercicio 2
#estrato
estrato1 = 10
estrato2 = 5
estrato3 = 2
#zonas
rural = 10
urbano = 5
#ingresos mensuales
menos500 = 10
mas500 = 5
nombre = input('Por favor ingrese el nombre de la persona: ')
estrato = input('Por favor ingrese el estrato de la persona: ')
zona = input('Por favor ingrese la zona donde vive (rural o urbano): ')
ingresos = int(input('Por favor ingrese los ingresos: '))
suma = 0
if estrato == '1':
    suma += 10 
elif estrato == '2':
    suma += 5
else:
    suma += 2
if zona == 'rural':
    suma += rural
else: 
    suma += urbano
if ingresos < 500000:
    suma += menos500
else:
    suma += mas500
print (nombre,'La suma de los puntos es de :',suma)
----------------------
#ejercicio 5
año1 = int(input('Ingrese el primer año: '))
año2 = int(input('Ingrese el segundo año: '))
while año2 < año1 :
    año2 = int(input('Ingrese de nuevo el segundo año: '))
    rango = año2 - año1
    if (rango % 4 == 0 and (rango % 100 != 0)) and rango % 10 == 0: # aca compruebo que el año sea bisiesto y sea multiplo de 10 
        print('el rango de los años es de',rango)
    else:
        print('El rango no cumple con las condiciones')
--------------'''
#ejercicio 6
manzanas = int(input('Ingrese el numero de manzanas a comprar: '))
precio = int(input('Ingrese el precio por unidad de  la manzana: '))
if manzanas > 36:
    print ('El valor neto de la compra es de:',manzanas*precio)
    print ('El descuento de la compra es de:',((manzanas*5000)* 0.15))
    print ('El valor total a pagar es de:',manzanas*precio-((manzanas*5000)* 0.15))
    manzanas_exceso = manzanas // 12 - 3
    print ('Las manzanas obsequiadas son:',manzanas_exceso)
else:
    print ('El valor neto de la compra es de:',manzanas*precio)
    print ('El descuento de la compra es de:',((manzanas*5000)* 0.10))
    print ('El valor total a pagar es de:',manzanas*precio-((manzanas*5000)* 0.10))