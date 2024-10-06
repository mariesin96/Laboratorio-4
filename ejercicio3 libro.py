class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # Estado inicial

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True 
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def mostrar_estado(self):
        estado = "disponible" if self.disponible else "prestado"  
        print(f"El libro '{self.titulo}' está {estado}.") 


libro = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro.mostrar_estado()  # Debería mostrar "El libro 'Cien Años de Soledad' está disponible."
libro.prestar()         # Debería mostrar "El libro 'Cien Años de Soledad' ha sido prestado."
libro.mostrar_estado()  # Debería mostrar "El libro 'Cien Años de Soledad' está prestado."
libro.devolver()        # Debería mostrar "El libro 'Cien Años de Soledad' ha sido devuelto."
libro.mostrar_estado()  # Debería mostrar "El libro 'Cien Años de Soledad' está disponible."