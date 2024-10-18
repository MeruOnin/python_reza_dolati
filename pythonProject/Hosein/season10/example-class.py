class Area:
    def set(self, x:float, y:float=0)-> None:
        if y != 0:
            self.x = x
            self.y = y
        else:
            self.x = x
    def area_circle(self):
        return 2 * 3.14 * self.x
    
    def area_square(self):
        return self.x ** 2
    
    def area_rectangle(self):
        return self.x * self.y
    
    def area_tringle(self):
        return (self.x * self.y) // 2
    

circle = Area()
square = Area()
rectangle = Area()
triangle = Area()

circle.set(3)
square.set(4)
rectangle.set(6, 9)
triangle.set(2, 6)

print(20 * '-', "AreaCircel", 20 * '-')
print(circle.area_circle())
print(20 * '-', "AreaSquare", 20 * '-')
print(Area.area_square(square))
print(20 * '-', "AreaRectangle", 20 * '-')
print(Area.area_rectangle(rectangle))
print(20 * '-', "AreaTrangle", 20 * '-')
print(Area.area_tringle(triangle))




