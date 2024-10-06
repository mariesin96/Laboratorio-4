class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = "despierto"

    def dormir(self):
        self.estado = "dormido"

    def despertar(self):
        self.estado = "despierto"

    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.edad} años y está {self.estado}.")

persona = Persona("Ana", 30)
persona.mostrar_estado()  # Debería mostrar "Ana tiene 30 años y está despierto."
persona.dormir()
persona.mostrar_estado()  # Debería mostrar "Ana tiene 30 años y está dormido."
persona.despertar()
persona.mostrar_estado()  # Debería mostrar "Ana tiene 30 años y está despierto."