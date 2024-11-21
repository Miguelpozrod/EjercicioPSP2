import threading
import time
import random

class ProcesadorArchivo(threading.Thread):
    def __init__(self, nombre_archivo, num_lineas):
        super().__init__()
        self.nombre_archivo = nombre_archivo
        self.num_lineas = num_lineas

    def run(self):

        for i in range(self.num_lineas):
            time.sleep(random.uniform(0.1, 0.5))
            print(f"Procesando {self.nombre_archivo} - Línea {i + 1}")


archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt", "archivo4.txt", "archivo5.txt"]

hilos = []

for archivo in archivos:

    num_lineas = random.randint(3, 6)
    hilo = ProcesadorArchivo(nombre_archivo=archivo, num_lineas=num_lineas)
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los archivos han sido procesados.")
