class Termostato:
    def __init__(self, temperatura_inicial):
        self.temperatura = temperatura_inicial  # Cambiar 'temperatura_inicial' a 'temperatura'

    def aumentar_temperatura(self, grados):
        self.temperatura += grados

    def disminuir_temperatura(self, grados):
        self.temperatura -= grados

    def mostrar_temperatura(self):
        print(f"La temperatura actual es {self.temperatura}°C.")


termostato = Termostato(20) 
termostato.mostrar_temperatura() 
termostato.aumentar_temperatura(5) 
termostato.mostrar_temperatura()  
termostato.disminuir_temperatura(3) 
termostato.mostrar_temperatura() 