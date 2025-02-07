class Filter:
    def __set_name__(self, owner, name):
        self.value = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.value]
    
    def __set__(self, instance, value):
        if value:
            instance.__dict__[self.value] = value
        else:
            raise ValueError(f"Invalid Erorr : {value!r}")
        
    def __delete__(self, instance):
        del instance.__dict__[self.value]


class Parent:
    child_name = Filter()
    father_name = Filter()
    mother_name = Filter()

    def __init__(self, child_name, father_name, mother_name):
        self.child_name = child_name
        self.father_name = father_name
        self.mother_name = mother_name

    
p = Parent("hossein", "khoda", "Zahra")
print(p.child_name)
print(p.father_name)
print(p.mother_name)
print(p.__dict__)
