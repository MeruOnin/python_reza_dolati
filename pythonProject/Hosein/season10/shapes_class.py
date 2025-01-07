class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.perimeter_value = float()
        self.area_vlaue = float()

    def show(self):
        for key, value in self.__dict__.items():
            try:
                print(f"{key}:{value}")
            except:
                print("sorry!..")

    def __str__(self):
        return f"name class is: {self.__class__.__name__}"


# length, width
class Rectangle(Shape):
    def perimeter(self):
        self.perimeter_value = 2 * (self.length + self.width)
    
    def area(self):
        self.area_vlaue = self.length * self.width

    def __call__(self, **kwargs):
        super().__init__(**kwargs)


# rule, height, side1, side2
class Traingle(Shape):
    def perimeter(self):
        self.perimeter_value = self.rule + self.height + self.side1 + self.side2
    
    def area(self):
        self.area_vlaue = (self.rule * self.height) / 2 

    
rectangle = Rectangle(length=5, width=3)
rectangle.perimeter()
rectangle.area()
rectangle.show()
print("*"*30)
rectangle(length=3, width=4)
rectangle.perimeter()
rectangle.area()
rectangle.show()
print("*" * 20)
traingle = Traingle(rule=5, height=6, side1=3.5, side2=3.5)
traingle.perimeter()
traingle.area()
traingle.show()



