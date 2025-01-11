# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if isinstance(other, Point):
#             return self.x + other.x, self.y + other.y
#         else:
#             raise ValueError("hahahahaha")
#
#
# p1 = Point(1, 4)
# p2 = Point(3, 7)
# result = p1 + p2
#
# print(result)

# ------------------------------------------------------------------
# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.imag = imag
#         self.real = real
#
#     def __add__(self, other):
#         if isinstance(other, ComplexNumber):
#             return f"{self.real + other.real} + {self.imag + other.imag}i"
#         else:
#             raise ValueError("hahahahahahahah")
#
#     def __sub__(self, other):
#         if isinstance(other, ComplexNumber):
#             return f"{self.real - other.real} - {self.imag - other.imag}i"
#         else:
#             raise ValueError("Invalid Error")
#
#     def __mul__(self, other):
#         if isinstance(other, ComplexNumber):
#             return f"{self.real * other.real} * {self.imag * other.imag}"
#         else:
#             raise ValueError("Invalid Error")
#
#
# c1 = ComplexNumber(4, 8)
# c2 = ComplexNumber(2, 2)
# print(c1+c2)
# print(c1-c2)
# print(c1*c2)

# ----------------------------------------------------------

class Matrix:
    def __init__(self, indexes_rtl_z_: list):
        self.indexes = indexes_rtl_z_

    def __add__(self, other):
        if isinstance(other, Matrix):
            matrix_list = list()
            for i, j in enumerate(self.indexes):
                matrix_list.append(j + other.indexes[i])
            return matrix_list
        else:
            raise ValueError("hahahah")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            matrix_list = list()
            for i, j in enumerate(self.indexes):
                matrix_list.append(j - other.indexes[i])
            return matrix_list
        else:
            raise ValueError("hahahah")


m1 = Matrix([1, 2, 3, 4])
m2 = Matrix([5, 6, 7, 8])
print(m1+m2)
print((m1-m2))