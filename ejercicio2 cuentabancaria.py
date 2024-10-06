class cuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"El saldo de {self.titular} es {self.saldo}.")  


cuenta = cuentaBancaria("Juan", 500)
cuenta.depositar(200)
cuenta.mostrar_saldo()  
cuenta.retirar(100)
cuenta.mostrar_saldo()