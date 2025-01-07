from asyncio import sleep
from datetime import datetime


class Product:
    def __init__(self, name_product: str, price: float)-> None:
        self.name_product = name_product
        self.price = price

    def __str__(self):
        return f"{self.name_product}"
    

class CommentUsers:
    def __init__(self, product_name: str, user_name: str, description: str, like: int, dislike: int)-> None:
        self.product_name = product_name
        self.user_name = user_name
        self.description = description
        self.like = like
        self.dislike = dislike
        self.date = datetime.now()

    def show(self):
        print(f"product: {self.product_name}\n"
              f"name: {self.user_name}\n"
              f"description: {self.description}\n"
              f"like: {self.like}\n"
              f"dislike: {self.dislike}\n"
              f"date: {self.date}")
        
    def __call__(self, like: int, dislike: int)-> None:
        self.like += like
        self.dislike += dislike
        
    @classmethod
    def info(cls):
        return f"class name: {cls.__name__}"

    @classmethod
    def sencorShip(cls, product_name: str, user_name: str, description: str, like: int, dislike: int):
        sc = description.replace("بیشعور", "****")
        return cls(product_name, user_name, sc, like, dislike)  
    
    @staticmethod
    def elapse_time(time):
        return time - datetime.now()


a = CommentUsers("moz", "Hosy", "یک موز بسیار بیشعور بود!", 4, 2)  
a.show() 
print("*"*40)
a2 = CommentUsers.sencorShip("moz", "Hosy", "یک موز بسیار بیشعور بود!", 4, 2)  
a2.show()   
print(a2.info())
print("*"*40)
print(a2.elapse_time(a2.date))
a2(like=1, dislike=0)
a2.show()
