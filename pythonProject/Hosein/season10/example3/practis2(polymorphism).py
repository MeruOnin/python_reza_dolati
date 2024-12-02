class Vehicle():
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speed(self):
        print(f"I am {self.name}, I speed is ...")


class Car(Vehicle):
    def speed(self):
        print(f"I am {self.name}, I speed is 10 as 400 km/h")


class Bicycle(Vehicle):
    def speed(self):
        print(f"I am {self.name}, I speed is 5 as 80 km/h")


class Airplane(Vehicle):
    def speed(self):
        print(f"I am {self.name}, I speed is 400 as 1000 km/h")


class Lamborghini(Car):
    def speed(self):
        print(f"I am {self.name}, I speed maximum is 450km/h")


class Benz(Car):
    def speed(self):
        print(f"I am {self.name}, I speed maximum is 378km/h")


c200 = Benz("c200", "blue")
c200.speed()


