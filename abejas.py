class Cliente: 
    def __init__(self, nombre, _DNI, cantidad_kilos, repetir_compra):
        self.nombre = nombre
        self._numero_dni = _DNI 
        self.cantidad = cantidad_kilos
        self.precio = self.calcular_precio() 
        self.mensaje_repetir_compra = self.repetir_compra(repetir_compra)

    def calcular_precio(self):
        return self.cantidad * 1500 
    
    def pago_compra(self, calcular_precio):
        if pago_de_compra == True:
            print(f"El cliente pago la compra, con un precio de {self.calcular_precio}")
        else:
            return "El cliente no pago la compra"
    
    def repetir_compra(self, repetir_compra):
        if repetir_compra:
            return "El cliente repitió la compra"
        else:
            return "El cliente no repitió la compra"

nombre = input("Proporcione el nombre del cliente: ")
numero_dni = int(input("Ingrese el número de documento del cliente: "))
cantidad_kilos = int(input("Ingrese la cantidad de kilos que el cliente compró: "))
repetir_compra = input("¿El cliente repitió la compra? (si/no): ").strip().lower() == "si" 
pago_de_compra = input("El cliente pago la compra? si/no: ").strip().lower() == "si"

cliente1 = Cliente(nombre, numero_dni, cantidad_kilos, repetir_compra)
cliente2 = Cliente("Ariel", 2333, 25, True)

# Salida de datos
print(f"\nEl cliente {cliente1.nombre}, con DNI {cliente1._numero_dni}, compró {cliente1.cantidad} kilos, con un precio total de {cliente1.precio} pesos. {cliente1.mensaje_repetir_compra}")
print(f"El cliente {cliente2.nombre}, con DNI {cliente2._numero_dni}, compró {cliente2.cantidad} kilos, con un precio total de {cliente2.precio} pesos. {cliente2.mensaje_repetir_compra}")
