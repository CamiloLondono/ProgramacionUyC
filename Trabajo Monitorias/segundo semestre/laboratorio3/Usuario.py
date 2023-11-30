class Usuario:
    def __init__(self, nombre, apellido, cedula, telefono, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo

    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - Cédula: {self.__cedula}, Teléfono: {self.__telefono}, Correo: {self.__correo}"
