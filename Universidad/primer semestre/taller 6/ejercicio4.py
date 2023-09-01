#ejercicio 4:

def calcular_sueldo(sueldo):
    pago = sueldo
    if sueldo > 1000000:
        descuento = (sueldo*6)/100
        pago = (sueldo-descuento)
    else:
        pago
    return pago
def calcular_salud(sueldo):
    pagar = (sueldo*87.5)/100
    pagarsalud = (sueldo-pagar)
    return pagarsalud
def calcular_pension(sueldo):
    pagar = (sueldo*84)/100
    pagarpension = (sueldo-pagar)
    return pagarpension
def calcular_arl(sueldo):
    pagar = (sueldo*96.5)/100
    pagararl = (sueldo-pagar)
    return pagararl
sueldo = int(input('por favor ingrese el sueldo del empleado '))
sueldoneto = 0
salud = 0
pension = 0
arl = 0
sueldoneto = calcular_sueldo(sueldo)
salud = calcular_salud(sueldo)
pension = calcular_pension(sueldo)
arl = calcular_arl(sueldo)
print ('el sueldo del trabajador es de {}, lo que paga por salud es {}, lo que paga por pension es de {} y lo que paga en arl es {}'.format(sueldoneto,salud,pension,arl))
