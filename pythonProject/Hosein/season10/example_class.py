import math
class Area:
    def __init__(self, x:float, y:float=0)-> None:
        self.x = x
        self.y = y
    def __str__(self):
        if self.y == 0:
            return f"{self.x}"
        else:
            return f"{self.x}  {self.y}"
    def __repr__(self):
        if self.y == 0:
            return f"{self.__class__.__name__}({self.x})"
        else:
            return f"{self.__class__.__name__}({self.x}, {self.y})"
    def area_circle(self):
        return 2 * math.pi * self.x
    
    def area_square(self):
        return self.x ** 2
    
    def area_rectangle(self):
        return self.x * self.y
    
    def area_tringle(self):
        return (self.x * self.y) // 2
    


if __name__ == "__main__":
    circle = Area(3)
    square = Area(4)
    rectangle = Area(6, 9)
    triangle = Area(2, 6)

    print(repr(circle))
    print(square)
    print(rectangle)

    print(20 * '-', "AreaCircel", 20 * '-')
    print(circle.area_circle())
    print(20 * '-', "AreaSquare", 20 * '-')
    print(Area.area_square(square))
    print(20 * '-', "AreaRectangle", 20 * '-')
    print(Area.area_rectangle(rectangle))
    print(20 * '-', "AreaTrangle", 20 * '-')
    print(Area.area_tringle(triangle))




