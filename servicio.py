class Servicio:
    def __init__(self, nombre, costo_por_hora):
        self.nombre = nombre
        self.costo_por_hora = costo_por_hora

    def calcular_costo(self, horas):
        pass


class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return horas * self.costo_por_hora


class AlquilerEquipos(Servicio):
    def calcular_costo(self, horas):
        return horas * self.costo_por_hora


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas):
        return horas * self.costo_por_hora