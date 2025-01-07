from pprint import pprint


class UserList(list["User"]):
    def search(self, user_name):
        user_search: list["User"] = []
        for user in self:
            if user_name in user.user_name:
                user_search.append(user)
        return user_search
    
    def append(self, object):
        if not isinstance(object, User):
            raise TypeError("Erorr")
        return super().append(object)

class User:
    all_users: list["User"] = UserList()
    def __init__(self, user_name: str, email: str, password: str, **kwargs) -> None:
        self.user_name = user_name
        self.email = email
        self.password = password
        User.all_users.append(self)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.password!r})"
    
    def __str__(self) -> str:
        return f"you is {self.user_name}" 


class Seller(User):
    def __init__(self, shaba, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.password!r}, {self.shaba!r})"

    def order(self, order: "Order"):
        return f"{self.user_name} is seller {order}"


class Buyer(User):
    def __init__(self, phone, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

    def __repr__(self):
        return f"{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.password!r}, {self.phone!r})"
    

class SellerAndBuyer(Seller, Buyer):
    def __init__(self, score: int, **kwargs):
        super().__init__(**kwargs)
        self.score = score

    def __repr__(self):
        return f"{self.__class__.__name__}(user_name={self.user_name!r}, email={self.email!r}, password={self.password!r}, phone={self.phone!r},shaba={self.shaba!r}, score={self.score!r})"
    

user6 = SellerAndBuyer(user_name="Hossein", password="1234", email="H@gmail.com", phone="09913945649", shaba="9889", score=20)

print(User.all_users)
pprint(SellerAndBuyer.__mro__)

print(User.all_users.search("o"))



