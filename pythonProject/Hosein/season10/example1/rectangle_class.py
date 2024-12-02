class Rectangle:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def area(self):
        return f"Your rectangle area is: {self.x * self.y}"
    
    def perimetr(self):
        return f"Your rectangle perimetr is: {(2 * self.x) + (2 * self.y)}"
    

rectangle1 = Rectangle(12.5, 5)
print(rectangle1.area())
print(rectangle1.perimetr())
