i = 100
limite = 45000
c1 = 2
c2 = 8
calculo = 0
operacion1 = 0
while i <= limite:
    operacion = 0
    operacion = ((c1*i)+c2)
    operacion1 += operacion
    i += 1
    calculo = operacion1
    #print (operacion)
print (calculo)
#print (calculo)
i = 1
a = 1
b = 100
limite1 = 45000
limite2 = 99   
calculo = 0
calculo1 = 0
calculo2 = 0
calculo3 = 0
operacion1 = 0
operacion2 = 0
operacion3 = 0
while i <= limite1:
    operacion = 0
    operacion = (i)
    operacion1 += operacion
    i += 1
    calculo1 = operacion1
while a <= limite2:
    operacion = 0
    operacion = (a)
    operacion2 += operacion
    a += 1
    calculo2 = operacion2
while b <= limite1:
    operacion = 0
    operacion = 1
    operacion3 += operacion
    b += 1
    calculo3 = operacion3*8
calculo = (2*(calculo1-calculo2))+calculo3
print (calculo)