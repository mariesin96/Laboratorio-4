class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea  '{tarea}' agregada a la lista.")

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"Tarea '{tarea}' eliminada de la lista.")

        else:
            print(f"Tarea '{tarea}' no encontrada.")


    def mostrar_tareas(self):
        if self.tareas:
            print("tareas pendientes:",",".join(self.tareas))

Lista_De_Tareas = ListaDeTareas()


Lista_De_Tareas.agregar_tarea("Hacer la compra")
Lista_De_Tareas.agregar_tarea("Estudiar para  el examen")
Lista_De_Tareas.agregar_tarea("Limpiar la casa")
Lista_De_Tareas.mostrar_tareas()
Lista_De_Tareas.eliminar_tarea("Estudiar parz  el examen")
Lista_De_Tareas.mostrar_tareas()
Lista_De_Tareas.eliminar_tarea("ir al cine")
