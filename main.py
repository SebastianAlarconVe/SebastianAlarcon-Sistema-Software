from servicio import ReservaSala, AlquilerEquipos, AsesoriaEspecializada
from manejo_errores import manejar_error


def main():
    try:
        print("Sistema de Servicios")

        opcion = input("Seleccione servicio (1 Sala, 2 Equipos, 3 Asesoria): ")

        horas = int(input("Ingrese numero de horas: "))

        if opcion == "1":
            servicio = ReservaSala("Reserva de sala", 50)

        elif opcion == "2":
            servicio = AlquilerEquipos("Alquiler de equipos", 30)

        elif opcion == "3":
            servicio = AsesoriaEspecializada("Asesoria especializada", 80)

        else:
            raise ValueError("Opcion no valida")

        costo = servicio.calcular_costo(horas)

        print("El costo total es:", costo)

    except Exception as e:
        manejar_error(e)


if __name__ == "__main__":
    main()