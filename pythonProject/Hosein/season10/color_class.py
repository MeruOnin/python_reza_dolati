class Color:
    def __init__(self, name: str, rgb: int)-> None:
        self.name = name
        self.rgb = rgb

    @property
    def name(self):
        return self._name

    @property
    def rgb(self):
        return self._rgb

    @name.setter
    def name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f"{name!r}")
        
    @rgb.setter
    def rgb(self, rgb):
        if isinstance(rgb, int):
            self._rgb = rgb
        else:
            raise ValueError("please enter number")
        
    @name.deleter
    def name(self):
        del self._name


c = Color("dfdf", 0xffff)
print(c.name)
print(c.rgb)
c.name = "red"
c.rgb = 0xf443
print("*" * 40)
print(c.name)
print(c.rgb)
del c.name
print(c.name)
