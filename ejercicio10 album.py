class Album:
    def __init__(self):
        self.fotos = []

    def agregar_fotos(self, foto):
        self.fotos.append(foto)
        print(f"Foto  '{foto}' agregada al album.")

    def eliminar_foto(self, foto):
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"Foto '{foto}' eliminada del album.")
        else:
            print(f"Foto '{foto}' no encontrada.")

    def mostrar_fotos(self):
        if self.fotos:
            print("fotos en el album",",".join(self.fotos))
        else:
            self.new_method()

    def mostrar_fotos(self):
        if self.fotos:
            print("Fotos en el álbum:", ", ".join(self.fotos))
        else:
            print("El álbum está vacío.")

album = Album()


album.agregar_fotos("vacaciones_playa.jpg")
album.agregar_fotos("cumplaños_2024.jpg")
album.agregar_fotos("boda_amigo.jpg")

album.mostrar_fotos()
album.eliminar_foto("cumpleaños_2024.jpg")
album.mostrar_fotos()
album.eliminar_foto("fiesta_nueva.jpg")