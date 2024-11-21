import threading
import time
import random


class SesionUsuario:
    def iniciar_sesion(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario
        print(f"Sesión iniciada para el usuario: {self.nombre_usuario}")

    def mostrar_sesion(self):
        print(f"Usuario actual en sesión: {self.nombre_usuario}")

datos_sesion = threading.local()


def gestionar_sesion(nombre_usuario):

    datos_sesion.sesion = SesionUsuario()

    datos_sesion.sesion.iniciar_sesion(nombre_usuario)

    time.sleep(random.uniform(0.5, 2))

    datos_sesion.sesion.mostrar_sesion()


usuarios = ['Ana', 'Carlos', 'Beatriz', 'David', 'Elena']

hilos = []

for i, usuario in enumerate(usuarios):
    hilo = threading.Thread(target=gestionar_sesion, args=(usuario,), name=f"Hilo-{i + 1}")
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todas las sesiones han sido gestionadas.")
