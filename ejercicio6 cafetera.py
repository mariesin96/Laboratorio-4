class cafetera:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self._nivel_actual = 0 

    def llenar(self):
        self._nivel_actual = self.capacidad
        print("la  cafetera ha sido llenada.")

    def servir_taza(self):
        if self._nivel_actual > 0:
            self._nivel_actual -= 1
            print("se ha servido una taza de cafe.")
        else:
            print("No hay cafe. llena la  cafetera.")

    def mostrar_nivel(self):
        print(f"Nivel actual de cafe: {self._nivel_actual} tazas.")

cafetera = cafetera (5)

cafetera.mostrar_nivel()
cafetera.servir_taza()
cafetera.llenar()
cafetera.mostrar_nivel()
cafetera.servir_taza()
cafetera.mostrar_nivel()

