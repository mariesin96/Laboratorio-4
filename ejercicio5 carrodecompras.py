class CarritodeCompras:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos y sus precios

    def agregar_producto(self, producto, precio):
        if producto in self.productos:
            print(f"El producto '{producto}' ya está en el carrito.")
        else:
            self.productos[producto] = precio
            print(f"Producto '{producto}' agregado con éxito al carrito.")

    def quitar_producto(self, producto):
        if producto in self.productos:
            del self.productos[producto]
            print(f"Producto '{producto}' eliminado del carrito.")
        else:
            print(f"El producto '{producto}' no está en el carrito.")

    def mostrar_productos(self):
        if self.productos:
            print("Productos en el carrito:")
            for producto, precio in self.productos.items():
                print(f"- {producto}: ${precio}")
        else:
            print("El carrito está vacío.")

    def calcular_total(self):
        total = sum(self.productos.values())
        print(f"El total del carrito es: ${total:.2f}")
        return total


carrito = CarritodeCompras()
carrito.agregar_producto("Manzanas", 3.50)   
carrito.agregar_producto("Pan", 2.00)       
carrito.mostrar_productos()                 
carrito.calcular_total()           