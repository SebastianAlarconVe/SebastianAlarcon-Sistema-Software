import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def manejar_error(error):
    logging.error(str(error))
    print("Ocurrió un error:", error)