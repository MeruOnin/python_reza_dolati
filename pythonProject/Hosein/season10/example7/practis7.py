class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return self.x + other.x, self.y + other.y
        else:
            raise ValueError("hahahahaha")


p1 = Point(1, 4)
p2 = Point(3, 7)
result = p1 + p2

print(result)
