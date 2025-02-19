class Cliente: 
    def __init__(self, nombre, _DNI, cantidad_kilos, pago_compra, repetir_compra):
        self.nombre = nombre
        self._numero_dni = _DNI 
        self.cantidad = cantidad_kilos
        self.precio = self.calcular_precio() 
        self.pago_compra = pago_compra
        self._repetir_la_compra = repetir_compra

    def calcular_precio(self):
        return self.cantidad * 1500 
    
    def pago_de_compra(self):
        if self.pago_compra:
            return f"El cliente pagó la compra, con un precio de {self.precio} pesos."
        return "El cliente no pagó la compra."

    def repetir_compra(self):
        if self.repetir_compra:
            return "El cliente repitió la compra."
        return "El cliente no repitió la compra."

nombre = input("Proporcione el nombre del cliente: ")
numero_dni = int(input("Ingrese el número de documento del cliente: "))
cantidad_kilos = int(input("Ingrese la cantidad de kilos que el cliente compró: "))
repetir_compra = input("¿El cliente repitió la compra? (si/no): ").strip().lower() == "si" 
pago_compra = input("¿El cliente pagó la compra? (si/no): ").strip().lower() == "si"

# Creación de clientes
cliente1 = Cliente(nombre, numero_dni, cantidad_kilos, pago_compra, repetir_compra)
cliente2 = Cliente("Ariel", 2333, 25, True, True)

# Salida de datos
print(f"\nEl cliente {cliente1.nombre}, con DNI {cliente1._numero_dni}, compró {cliente1.cantidad} kilos, con un precio total de {cliente1.precio} pesos. {cliente1.repetir_compra()} {cliente1.pago_de_compra()}")
print(f"El cliente {cliente2.nombre}, con DNI {cliente2._numero_dni}, compró {cliente2.cantidad} kilos, con un precio total de {cliente2.precio} pesos. {cliente2.repetir_compra()} {cliente2.pago_de_compra()}")
