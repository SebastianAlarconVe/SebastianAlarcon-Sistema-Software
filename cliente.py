from excepciones import ClienteError
class Cliente:

    def __init__(self, nombre, email, telefono):

        if nombre == "":
            raise ClienteError("El nombre no puede estar vacío")

        if "@" not in email:
            raise ClienteError("Email inválido")

        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono


    def get_nombre(self):
        return self.__nombre


    def get_email(self):
        return self.__email


    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - {self.__email}"