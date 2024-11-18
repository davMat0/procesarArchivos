import threading

class ProcesadorArchivo(threading.Thread):
    def __init__(self, archivo, numLineasProcesar):
        super().__init__()
        self.archivo = archivo
        self.numLineasProcesar = numLineasProcesar

    def run(self):
        lineas = self.archivo.splitlines()
        for i in range(min(self.numLineasProcesar, len(lineas))):
            print(self.name , lineas[i])

# Lista de strings simulando archivos
archivos = [
    "Este es un texto\n de ejemplo para\n realizar pruebas",
    "Estas lineas\nDefinen una clase\nEn el método run",
    "Asegúrate de\n que el programa principal\nEspere a que todos terminen\nAntes de imprimir el mensaje"
]

#número de líneas que se van a procesar
numLineasProcesar = 1
hilos = []

# Se crea e inicia un hilo para cada archivo
for contenido in archivos:
    hilo = ProcesadorArchivo(contenido, numLineasProcesar)
    hilos.append(hilo)
    hilo.start()

# Esperar a que los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los archivos han sido procesados")
