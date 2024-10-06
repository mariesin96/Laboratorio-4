class biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro}'  agregado a la biblioteca.")

    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f"libro '{libro}' eliminado de la biblioteca.")

        else:
            print(f"libro '{libro}' no encontrado")


    def mostrar_libros(self):
        if self.libros:
            print("libros en la bibliotec:")
            for libro in self.libros:
                print(f"-  {libro}")
        else:
            print("No hay libros n la biblioteca")

biblioteca = biblioteca()


biblioteca.agregar_libros("cien años de soledad")
biblioteca.agregar_libros("El principito")
biblioteca.agregar_libros("1984")


biblioteca.mostrar_libros()


biblioteca.eliminar_libro("El principito")


biblioteca.mostrar_libros()


biblioteca.eliminar_libro("El hobbit")