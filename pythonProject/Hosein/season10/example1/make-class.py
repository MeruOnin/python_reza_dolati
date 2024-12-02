from math import hypot

class Point:
    def move(self, x: int, y: int)-> None:
        self.x = x
        self.y = y

    def reset(self)-> int:
        self.move(0, 0)

    def distnase(self, other: "Point")->float:
        return hypot(self.x-other.x, self.y-other.y)


p1 = Point()
p2 = Point()

p1.reset()

p2.x = 4
p2.y = 6

print(Point.distnase(p1, p2))
