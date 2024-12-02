class ListAnimals(list["Animals"]):
    def search(self, animal_search):
        animals_search: list["Animals"] = list()
        for animal in self:
            if animal_search in animal.name:
                animals_search.append(animal)
        return animals_search


class Animals():
    list_animals: list["Animals"] = ListAnimals()

    def __init__(self, name: str, goneh: str, **kwargs) -> None:
        self.name = name
        self.goneh = goneh
        Animals.list_animals.append(self)

    def make_sound(self):
        print("Generic animal sound")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.goneh!r})"
    

class Mammals(Animals):
    def __init__(self, legs:int, **kwargs):
        super().__init__(**kwargs)
        self.legs = legs

    def make_sound(self):
        print("Generic mammals sound")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, goneh={self.goneh!r}, legs={self.legs})"


class Dog(Mammals):
    def __init__(self, nezad: str, **kwargs):
        super().__init__(**kwargs)
        self.nazad = nezad

    def make_sound(self):
        print("Hop Hop!")

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, goneh={self.goneh!r}, legs={self.legs}, nezad={self.nazad!r})"


hopy = Dog(nezad="hosky", name="hopy", legs=4, goneh="vahshi")

an1 = Animals("wolf", "aram")

print(Animals.list_animals.search("w"))


