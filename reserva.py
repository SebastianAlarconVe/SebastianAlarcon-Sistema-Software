from excepciones import ReservaError
class Reserva:

    def __init__(self, cliente, servicio, horas):

        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores a cero")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "pendiente"


    def confirmar(self):
        self.estado = "confirmada"


    def cancelar(self):
        self.estado = "cancelada"


    def procesar(self):

        costo = self.servicio.calcular_costo(self.horas)

        return costo
    