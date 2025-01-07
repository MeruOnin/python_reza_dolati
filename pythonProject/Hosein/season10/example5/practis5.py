# ایجاد یک  property برای کلاس Circle 
# from math import pi

# class Circle:
#     def __init__(self, radius)-> None:
#         self.radius = radius

#     @property
#     def radius(self):
#         return self._radius
    
#     @radius.setter
#     def radius(self, radius):
#         if isinstance(radius, float) or isinstance(radius, int):
#             self._radius = radius
#         else:
#             raise ValueError("Error please enter number")
        
#     @property
#     def area(self):
#         return f"your area circel: {2 * pi * self._radius}"
    

# circle1 = Circle(5)
# circle1.radius = 2
# print(circle1.radius)
# print(circle1.area)

# ------------------------------------------------------

# ایجاد یک property برای تبدیل سانت یگراد به فارنهایت
# class Temperature:
#     def __init__(self, cg):
#         self.cg = cg

#     @property
#     def farenhite(self):
#         return f"farenhite is : {(self.cg * 1.8) + 32}"  
    

# c = Temperature(54)
# print(c.farenhite)