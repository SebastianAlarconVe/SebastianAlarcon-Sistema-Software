# Excepción cuando hay errores en clientes
class ClienteError(Exception):
    pass

# Excepción cuando hay errores en servicios
class ServicioError(Exception):
    pass

# Excepción cuando hay errores en reservas
class ReservaError(Exception):
    pass