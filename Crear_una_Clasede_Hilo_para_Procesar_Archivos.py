import threading
import time
import random

datos_locales = threading.local()

def procesar_usuario(*args, **kwargs):

    datos_locales.id = args[0]
    datos_locales.nombre = kwargs.get('nombre', 'Desconocido')
    datos_locales.edad = kwargs.get('edad', 'No especificada')

    tiempo_procesamiento = random.uniform(0.5, 2)
    time.sleep(tiempo_procesamiento)


    print(f"Hilo {threading.current_thread().name} -> Usuario ID: {datos_locales.id}, "
          f"Nombre: {datos_locales.nombre}, Edad: {datos_locales.edad}")


usuarios = [
    (1, {'nombre': 'Ana', 'edad': 30}),
    (2, {'nombre': 'Carlos', 'edad': 22}),
    (3, {'nombre': 'Beatriz', 'edad': 27}),
    (4, {'nombre': 'David', 'edad': 35}),
    (5, {'nombre': 'Elena', 'edad': 29})
]

hilos = []

for i, (id_usuario, datos_usuario) in enumerate(usuarios):
    hilo = threading.Thread(target=procesar_usuario,
                            args=(id_usuario,),
                            kwargs=datos_usuario,
                            name=f"Hilo-{i + 1}")
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los usuarios han sido procesados.")
