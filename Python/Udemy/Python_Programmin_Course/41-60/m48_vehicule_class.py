class Vehicle():
     def __init__(self, brand, color):
        self.brand = brand
        self.color = color
     def __str__(self):
         return "El vehiculo de marca {} es de color {}".format(self.brand, self.color)

class Car(Vehicle):

    def __init__(self, brand, color, power, motor):
        Vehicle.__init__(self, brand, color)
        self.power = power
        self.motor = motor
    def __str__(self):
        return Vehicle.__str__(self) + ", {} Cv y motor de {}".format(self.power, self.motor)


my_vehicle = Vehicle('seat', 'verde')
print(my_vehicle)
my_car = Car('seat', 'rojo', '1400', 'gasolina')
print(my_car)
