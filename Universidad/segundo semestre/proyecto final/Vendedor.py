__author__="Camilo Londoño"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from Usuario import Usuario
from SerializacionBoleto import SerializacionBoleto
from Boletos import Boletos
import datetime

class Vendedor(Usuario):
    """Clase que hereda de la clase Usuario, representa a los vendedores de la aplicacion"""
    pass

    def venderBoletoBaloto(self,varId,varFecha,varCedula,varNum1,varNum2,varNum3,varNum4,varNum5,varNum6):
        """Metodo que permite vender boletos de baloto.
    
    Args:
    parametro1: varId(int) = varId
    parametro2: varFecha(str) = varFecha
    parametro3: varCedula(int) = varCedula
    parametro4: varNum1(int) = varNum1
    parametro5: varNum2(int) = varNum2
    parametro6: varNum3(int) = varNum3
    parametro7: varNum4(int) = varNum4
    parametro8: varNum5(int) = varNum5
    parametro9: varNum6(int) = varNum6
    return:
      None"""
        miSerializacionBoleto = SerializacionBoleto()
        boletosBaloto = miSerializacionBoleto.leerBoleto()
        boletos = []
        id = len(boletosBaloto)+1 #id secuencial
        fechaActual2 = datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y')
        varId.set(id)
        varFecha.set(fechaActual2)
        cedula = varCedula.get()
        num1 = varNum1.get()
        boletos.append(num1)
        num2 = varNum2.get()
        boletos.append(num2)
        num3 = varNum3.get()
        boletos.append(num3)
        num4 = varNum4.get()
        boletos.append(num4)
        num5 = varNum5.get()
        boletos.append(num5)
        num6 = varNum6.get()
        boletos.append(num6)
        miBoleto = Boletos(id, fechaActual2, cedula, boletos)
        miSerializacionBoleto.escribirBoleto(str(id)+'\n')
        miSerializacionBoleto.escribirBoleto(fechaActual2+'\n')
        miSerializacionBoleto.escribirBoleto(str(cedula)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num1)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num2)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num3)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num4)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num5)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num6)+'\n')


    def venderBoletoRevancha(self,varId,varFecha,varCedula,varNum1,varNum2,varNum3,varNum4,varNum5,varNum6):
        """Metodo que permite vender boletos de revancha.
    
    Args:
    parametro1: varId(int) = varId
    parametro2: varFecha(str) = varFecha
    parametro3: varCedula(int) = varCedula
    parametro4: varNum1(int) = varNum1
    parametro1: varNum2(int) = varNum2
    parametro1: varNum3(int) = varNum3
    parametro1: varNum4(int) = varNum4
    parametro1: varNum5(int) = varNum5
    parametro1: varNum6(int) = varNum6
    return:
      None"""
        miSerializacionBoleto = SerializacionBoleto()
        boletosBaloto = miSerializacionBoleto.leerBoleto()
        boletos = []
        id = len(boletosBaloto)+1
        fechaActual2 = datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y')
        varId.set(id)
        varFecha.set(fechaActual2)
        cedula = varCedula.get()
        num1 = varNum1.get()
        boletos.append(num1)
        num2 = varNum2.get()
        boletos.append(num2)
        num3 = varNum3.get()
        boletos.append(num3)
        num4 = varNum4.get()
        boletos.append(num4)
        num5 = varNum5.get()
        boletos.append(num5)
        num6 = varNum6.get()
        boletos.append(num6)
        miRevancha = Boletos(id, fechaActual2, cedula, boletos)
        miSerializacionBoleto.escribirBoleto(str(id)+'\n')
        miSerializacionBoleto.escribirBoleto(fechaActual2+'\n')
        miSerializacionBoleto.escribirBoleto(str(cedula)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num1)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num2)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num3)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num4)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num5)+'\n')
        miSerializacionBoleto.escribirBoleto(str(num6)+'\n')
