class Duck:
    def move(self):
        print("I am swimming...")


class Person:
    def move(self):
        print("I am walking...")


class Plane:
    def move(self):
        print("I am flynig...")

def func(obj):
    obj.move()

duck = Duck()
human = Person()
plane = Plane()

func(duck)
func(human)
func(plane)