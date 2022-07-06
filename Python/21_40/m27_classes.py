""" Uso de Clases POO en Python """


class Vehicule:
    def __init__(self, color, velocity, brand) -> None:
        self.color = color
        self.velocity = velocity
        self.brand = brand

    def show(self):
        print(
            f"Color: {self.color}, Velocidad: {self.velocity}, Marca: {self.brand}")

    def start(self):
        print("Iniciando vehiculo")
        self.show()

    def accelerate(self):
        if (self.velocity == 0):
            self.velocity = 10
        else:
            self.velocity = self.velocity + 10
        print(f"Acelerando a {self.velocity} km/h")

    def brake(self):
        if (self.velocity > 10):
            self.velocity = self.velocity - 10
        else:
            self.velocity = 0
        print(f"Frenando a {self.velocity} km/h")

# Clase herencia
class Moto(Vehicule):
    def __init__(self, color, velocity, brand, tire=2) -> None:
        # Llamada al constructor de la clase padre
        super().__init__(color, velocity, brand) 
        self.tire = tire
    
    def show(self):
        print(
            f"Moto -> Brand: {self.brand}, Color: {self.color}, Velocity: {self.velocity}, and {self.tire} Tyres")

# Clase herencia
class Car(Vehicule):
    def __init__(self, color, velocity, brand, tire=4) -> None:
        # Llamada al constructor de la clase padre
        super().__init__(color, velocity, brand) 
        self.tire = tire
    
    def show(self):
        print(
            f"Moto -> Brand: {self.brand}, Color: {self.color}, Velocity: {self.velocity}, and {self.tire} Tyres")

def process():
    toyota = Car('red', 100, 'Toyota')
    toyota.start()
    toyota.accelerate()
    toyota.show()
    print(type(toyota))

    renault = Car('blue', 120, 'Renault',4)
    renault.start()
    renault.accelerate()
    renault.accelerate()
    renault.show()
    print(type(renault))

    yamaha = Moto('blue', 120, 'Yamaha')
    yamaha.start()
    yamaha.accelerate()
    yamaha.accelerate()
    yamaha.brake()
    yamaha.show()
    print(type(yamaha))

process()
