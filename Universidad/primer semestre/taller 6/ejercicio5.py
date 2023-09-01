#ejercicio 5:

def calcular_recibosA(aguacasaA,electricidadcasaA,gascasaA,internetcasaA,televisioncasaA):
    pagar = (aguacasaA+electricidadcasaA+gascasaA+internetcasaA+televisioncasaA)
    return pagar
def calcular_recibosB(aguacasaB,electricidadcasaB,gascasaB,internetcasaB,televisioncasaB):
    pagar = (aguacasaB+electricidadcasaB+gascasaB+internetcasaB+televisioncasaB)
    return pagar
def calcular_pagomayor(pagocasaA,pagocasaB):
    pagar = 0
    if pagocasaA > pagocasaB:
        pagar = pagocasaA
        print ('la vivienda que debe pagar mas dinero es la vivienda a'.format(pagar))
    else:
        pagar = pagocasaB
        print ('la vivienda que debe pagar mas dinero es la casa b'.format(pagar))
def calcular_reciboagua(aguacasaA,aguacasaB):
    pagar = 0
    if aguacasaA > aguacasaB:
        pagar = aguacasaA
        print ('la casa que debe pagar mas por el agua es la casa a'.format(pagar))
    else:
        pagar = aguacasaB
        print ('la casa que debe pagar mas por el agua es la b '.format(pagar))
aguacasaA = int(input('por favor ingrese el precio del resivo del agua de la casa a '))
electricidadcasaA = int(input('por favor ingrese el precio del resivo de la electricidad de la casa a '))
gascasaA = int(input('por favor ingrese el precio del resivo del gas de la casa a '))
internetcasaA = int(input('por favor ingrese el precio del resivo del internet de la casa a '))
televisioncasaA = int(input('por favor ingrese el precio del resivo television de la casa a '))
aguacasaB = int(input('por favor ingrese el precio del resivo del agua de la casa b '))
electricidadcasaB = int(input('por favor ingrese el precio del resivo de la electricidad de la casa b '))
gascasaB = int(input('por favor ingrese el precio del resivo del gas de la casa b '))
internetcasaB = int(input('por favor ingrese el precio del resivo del internet de la casa b '))
televisioncasaB = int(input('por favor ingrese el precio del resivo de la television de la casa b '))
pagocasaA = 0
pagocasaB = 0
pagomayor = 0
pagomayor_agua = 0
pagocasaA = calcular_recibosA(aguacasaA,electricidadcasaA,gascasaA,internetcasaA,televisioncasaA)
pagocasaB = calcular_recibosB(aguacasaB,electricidadcasaB,gascasaB,internetcasaB,televisioncasaB)
pagomayor = calcular_pagomayor(pagocasaA,pagocasaB)
pagomayor_agua = calcular_reciboagua(aguacasaA,aguacasaB)