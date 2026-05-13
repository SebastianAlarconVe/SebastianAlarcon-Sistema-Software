def registrar_log(mensaje):

    archivo = open("logs.txt", "a")

    archivo.write(mensaje + "\n")

    archivo.close()