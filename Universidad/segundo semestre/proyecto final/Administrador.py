__author__="Camilo Londoño"
__copyright__="Copyright 2023, Universidad del Valle"
__credits__=["Universidad del Valle", "Steven Cordoba", "Camilo Londoño", "Juan Pablo Bernal"]
__license__="GPL"
__version__="1.0.0"
__maintainer__="Estudiantes de la Universidad del Valle"
__email__="steven.cordoba@correounivale.edu.co"
__status__="Pruebas"
from SerializacionUsuarios import SerializacionUsuarios
from SerializacionBaloto import SerializacionBaloto
from SerializacionRevancha import SerializacionRevancha
from Usuario import Usuario
from Baloto import Baloto
from Revancha import Revancha
from random import randrange
import datetime


class Administrador(Usuario):
    """Clase que hereda de la clase Usuario, representa al administrador de la aplicacion"""
    pass

    def realizarSorteoBaloto(self,varNum1, varNum2, varNum3, varNum4, varNum5, varNum6):
        """Metodo que permite realizar los sorteos de baloto
        Args:
    parametro1: varNum1(int) = varNum1
    parametro2: varNum2(int) = varNum2
    parametro3: varNum3(int) = varNum3
    parametro4: varNum4(int) = varNum4
    parametro5: varNum5(int) = varNum5
    parametro6: varNum6(int) = varNum6
    return:
      None"""
        miSerializacionBaloto = SerializacionBaloto()
        balotosCompletos = miSerializacionBaloto.leerBaloto()
        baloto = []
        fechaActual2 = datetime.datetime.strftime(datetime.datetime.now(),'%d/%m/%Y')
        id = len(balotosCompletos)+1
        while len(baloto) <6:
            numero = (randrange(1,45,2))
            if numero in baloto:
                pass
            else:
                baloto.append(numero)
        miBaloto = Baloto(id, fechaActual2, baloto)
        varNum1.set(baloto[0])
        varNum2.set(baloto[1])
        varNum3.set(baloto[2])
        varNum4.set(baloto[3])
        varNum5.set(baloto[4])
        varNum6.set(baloto[5])
        miSerializacionBaloto.escribirBaloto(str(id)+'\n')
        miSerializacionBaloto.escribirBaloto(fechaActual2+'\n')
        miSerializacionBaloto.escribirBaloto((str(baloto[0])+'\n'))
        miSerializacionBaloto.escribirBaloto((str(baloto[1])+'\n'))
        miSerializacionBaloto.escribirBaloto((str(baloto[2])+'\n'))
        miSerializacionBaloto.escribirBaloto((str(baloto[3])+'\n'))
        miSerializacionBaloto.escribirBaloto((str(baloto[4])+'\n'))
        miSerializacionBaloto.escribirBaloto((str(baloto[5])+'\n'))


    def realizarSorteoRevancha(self,varNum1, varNum2, varNum3, varNum4, varNum5, varNum6):
        """Metodo que permite realizar los sorteos de revancha
        Args:
    parametro1: varNum1(int) = varNum1
    parametro2: varNum2(int) = varNum2
    parametro3: varNum3(int) = varNum3
    parametro4: varNum4(int) = varNum4
    parametro5: varNum5(int) = varNum5
    parametro6: varNum6(int) = varNum6
    return:
      None"""
        miSerializacionRevancha = SerializacionRevancha()
        revanchasCompletos = miSerializacionRevancha.leerRevancha()
        revancha = []
        fechaActual = datetime.datetime.now() 
        fechaActual2 = datetime.datetime.strftime(fechaActual,'%d/%m/%Y')
        id = len(revanchasCompletos)+1
        while len(revancha) <6:
            numero = (randrange(2,44,2))
            if numero in revancha:
                pass
            else:
                revancha.append(numero)
        miBaloto = Revancha(id, fechaActual2, revancha)
        varNum1.set(revancha[0])
        varNum2.set(revancha[1])
        varNum3.set(revancha[2])
        varNum4.set(revancha[3])
        varNum5.set(revancha[4])
        varNum6.set(revancha[5])
        miSerializacionRevancha.escribirRevancha(str(id)+'\n')
        miSerializacionRevancha.escribirRevancha(fechaActual2+'\n')
        miSerializacionRevancha.escribirRevancha((str(revancha[0])+'\n'))
        miSerializacionRevancha.escribirRevancha((str(revancha[1])+'\n'))
        miSerializacionRevancha.escribirRevancha((str(revancha[2])+'\n'))
        miSerializacionRevancha.escribirRevancha((str(revancha[3])+'\n'))
        miSerializacionRevancha.escribirRevancha((str(revancha[4])+'\n'))
        miSerializacionRevancha.escribirRevancha((str(revancha[5])+'\n'))
    
    def crearVendedor(self,varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,varPassword):
        """Metodo que permite crear a los vendedores de la aplicacion.
    
    Args:
    parametro1: varCedula(int) = varCedula
    parametro2: varNombre(str) = varNombre
    parametro3: varApellido(str) = varApellido
    parametro4: varEdad(int) = varEdad
    parametro5: varTelefono(int) = varTelefono
    parametro6: varEmail(int) = varEmail
    parametro7: varDireccion(str) = varDireccion
    parametro8: varPassword(str) = varPassword
    return:
      None"""
        miSerializacion = SerializacionUsuarios()
        cedula = varCedula.get()
        nombre = varNombre.get()
        apellido = varApellido.get()
        edad = varEdad.get()
        telefono = varTelefono.get()
        email = varEmail.get()
        direccion = varDireccion.get()
        password = varPassword.get()
        if cedula != '' and nombre != '' and apellido != '' and edad != '' and telefono != '' and email != '' and direccion != '' and password != '':        
            miSerializacion.escribirArchivoUsuarios(cedula+'\n')
            miSerializacion.escribirArchivoUsuarios(nombre+'\n')
            miSerializacion.escribirArchivoUsuarios(apellido+'\n')
            miSerializacion.escribirArchivoUsuarios(edad+'\n')
            miSerializacion.escribirArchivoUsuarios(telefono+'\n')
            miSerializacion.escribirArchivoUsuarios(email+'\n')
            miSerializacion.escribirArchivoUsuarios(direccion+'\n')
            miSerializacion.escribirArchivoUsuarios('Vendedor'+'\n')
            miSerializacion.escribirArchivoUsuarios(password+'\n')
        else:
            print('Todos los campos son obligatorios')
    
    def eliminarVendedor(self,varCedula,listaUsuarios):
        """Metodo que permite eliminar a los vendedores de la aplicacion.
    
    Args:
    parametro1: varCedula(int) = varCedula
    parametro2: listaUsuarios(str) = listaUsuarios

    return:
      None"""
        miSerializacion = SerializacionUsuarios()
        validacion = False
        texto = ""
        for i in listaUsuarios:
            if (varCedula.get() == i.getCedula()):
                listaUsuarios.remove(i)
                validacion = True
                print('el usuario fue eliminado de la plataforma')
            else:
                pass
        
        if validacion == False:
            print('El usuario no se encuentra en la plataforma')  
        for j in listaUsuarios:
            texto = texto+str(j.getCedula())+'\n'+j.getNombre()+'\n'+j.getApellido()+'\n'+str(j.getEdad())+'\n'+str(j.getTelefono())+'\n'+j.getEmail()+'\n'+j.getDireccion()+'\n'+j.getRol()+'\n'+j.getPassword()+'\n'
        miSerializacion.sobreescribirArchivoUsuarios(texto)
    
    def buscarCedula(self,varCedula,varNombre,varApellido,varEdad,varTelefono,varEmail,varDireccion,listaUsuarios):
        """Metodo que permite buscar la cedula del vendedor a eliminar.
    
    Args:
    parametro1: varCedula(int) = varCedula
    parametro2: varNombre(str) = varNombre
    parametro3: varApellido(str) = varApellido
    parametro4: varEdad(int) = varEdad
    parametro5: varTelefono(int) = varTelefono
    parametro6: varEmail(int) = varEmail
    parametro7: varDireccion(str) = varDireccion
    parametro8: listaUsuarios(str) = listaUsuarios
    return:
      None"""
        validacion = False
        for i in listaUsuarios:
            if (varCedula.get() == i.getCedula()):
                validacion = True
                print('el usuario si esta registrado en la plataforma')
                varNombre.set(i.getNombre())
                varApellido.set(i.getApellido())
                varEdad.set(i.getEdad())
                varTelefono.set(i.getTelefono())
                varEmail.set(i.getEmail())
                varDireccion.set(i.getDireccion())
            else:
                pass
        if validacion == False:
            print('El usuario no esta registrado en la plataforma')        

    def consultarTodosResultadosBaloto(self,listaBaloto,todosBaloto):
        """Metodo que permite consultar todos los resultados de Baloto.
    Args:
    parametro1: listaBaloto(str) = listaBaloto
    parametro2: todosBaloto(str) = todosBaloto
    return:
      None"""
        miSerializacionBaloto = SerializacionBaloto()
        ResultadoTodosBaloto = miSerializacionBaloto.leerBaloto()
        variable = ''
        for i in ResultadoTodosBaloto:
            variable = variable +((str(i.getId())+'-'+i.getFecha()+'-'+i.getListaNumeros()[0]+'-'+i.getListaNumeros()[1]+'-'+i.getListaNumeros()[2]+'-'+i.getListaNumeros()[3]+'-'+i.getListaNumeros()[4]+'-'+i.getListaNumeros()[5])+'\n')
        todosBaloto.set(variable)
    
    def consultarTodosResultadoRevancha(self,listaRevancha,todosRevancha):
        """Metodo que permite consultar todos los resultados de Revancha.
    Args:
    parametro1: listaRevancha(str) = listaRevancha
    parametro2: todosRevancha(str) = todosRevancha
    return:
      None"""
        miSerializacionRevancha = SerializacionRevancha()
        ResultadoTodosRevancha = miSerializacionRevancha.leerRevancha()
        variable = ''
        for i in ResultadoTodosRevancha:
            variable = variable +((str(i.getId())+'-'+i.getFecha()+'-'+i.getListaNumeros()[0]+'-'+i.getListaNumeros()[1]+'-'+i.getListaNumeros()[2]+'-'+i.getListaNumeros()[3]+'-'+i.getListaNumeros()[4]+'-'+i.getListaNumeros()[5])+'\n')
        todosRevancha.set(variable)