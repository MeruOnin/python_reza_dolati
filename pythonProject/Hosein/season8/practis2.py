from shapes import *
Input1 = int(input("Enter your area or Radius: "))
Input2 = int(input("Enter your environment (if not environment enter -0-): "))

if Input2 != 0:
    print(rectngle.area(Input1, Input2))
    print(rectngle.Environment(Input1, Input2))
else:
    print(round(circle.area(Input1)))
    print(round(circle.environment(Input1)))
