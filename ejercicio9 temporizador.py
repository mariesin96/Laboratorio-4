class Temporizador:
    def __init__(self, tiempo_inicial):
        self.tiempo_restante = tiempo_inicial

    def iniciar(self):
        print(f"Temporizador iniciadoo con {self.tiempo_restante} segundos.")

    def pausar(self):
        print(f"Temporizador pausado con {self.tiempo_restante} segundos_restantes.")

    def mostrar_tiempo(self):
        print(f"Tiempo restante: {self.tiempo_restante} segundos.")


Temporizador = Temporizador(60)
Temporizador.iniciar()
Temporizador.mostrar_tiempo()
Temporizador.pausar()