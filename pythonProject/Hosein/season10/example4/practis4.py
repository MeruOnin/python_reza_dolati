# نوشتن یک mixin برای یک کلاس و چاپ کردن اسم کلاس و ویژگی های آن
# class PrintInfoMixin():
#     def info_print(self):
#         print(f"name class is: {self.__class__.__name__}")
#         print("*"*40)
#         attribute = vars(self)
#         for key, value in attribute.items():
#             print(f"{key}: {value}")


# class Test(PrintInfoMixin):
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age


# obj = Test("Hossein", 12)
# obj.info_print()


# اضافه کردن عملکرد جمع و تفریق و تقسیم و ضرب به یک کلاس دارای دو اتریبیوت x, y
# class MathOperationsMixin():
#     def jam(self):
#         return self.x + self.y
    
#     def menha(self):
#         return self.x - self.y
    
#     def zarb(self):
#         return self.x * self.y
    
#     def taksim(self):
#         return self.x / self.y
    

# class Math(MathOperationsMixin):
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y


# ali = Math(5, 7)

# print(ali.jam())
# print(ali.menha())
# print(ali.taksim())
# print(ali.zarb())



import logging
from functools import wraps

# تنظیمات اولیه logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class LoggerMixin:
    def log_method_call(self, method_name, *args, **kwargs):
        """ثبت اطلاعات متد فراخوانی‌شده"""
        logger.info(f"Method called: {method_name}")
        logger.info(f"Arguments: {args}")
        logger.info(f"Keyword arguments: {kwargs}")

    @staticmethod
    def log_decorator(method):
        """یک دکوریتور برای ثبت فراخوانی متدها"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # ثبت نام متد و آرگومان‌ها
            if isinstance(self, LoggerMixin):
                self.log_method_call(method.__name__, *args, **kwargs)
            return method(self, *args, **kwargs)
        return wrapper

# مثال استفاده:
class MyClass(LoggerMixin):
    def __init__(self, name):
        self.name = name

    @LoggerMixin.log_decorator
    def greet(self, greeting):
        return f"{greeting}, {self.name}!"

    @LoggerMixin.log_decorator
    def add(self, a, b):
        return a + b

# ایجاد یک شیء از کلاس
obj = MyClass("Ali")

# فراخوانی متدها
print(obj.greet(greeting="Hello"))
print(obj.add(10, 20))
