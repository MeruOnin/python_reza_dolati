from pprint import pprint

class BaseClass():
    count_base = 0

    def __init__(self, a, **kwargs):
        self.a = a

    def call_me(self):
        print("method in BaseClass")
        self.count_base += 1


class SuperClass1(BaseClass):
    count_SuperClass1 = 0

    def __init__(self, b, **kwargs):
        super().__init__(**kwargs)
        self.b = b

    def call_me(self):
        super().call_me()
        print("method in SuperClass1")
        self.count_SuperClass1 += 1


class SuperClass2(BaseClass):
    count_SuperClass2 = 0

    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        super().call_me()
        print("method in SuperClass2")
        self.count_SuperClass2 += 1


class SubClass(SuperClass1, SuperClass2):
    count_subClass = 0

    def __init__(self, d, e, **kwargs):
        super().__init__(**kwargs)
        self.d = d
        self.e = e

    def call_me(self):
        super().call_me()
        print("method in SubClass")
        self.count_subClass += 1


# a = SubClass()
# a.call_me()
# print(a.count_base, a.count_SuperClass1, a.count_SuperClass2, a.count_subClass)

n = SubClass(a=1, b=2, c=3, d=4, e=5)

pprint([n.a, n.b, n.c, n.d, n.e])
