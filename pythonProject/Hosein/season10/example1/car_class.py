class Car:
    def __init__(self, brand: str, year: str, model: str):
        self.brand = brand
        self.year = year
        self.model = model

    def __str__(self):
        return f"{self!r}:\n\tBrand: {self.brand}\n\tYear: {self.year}\n\tModel: {self.model}"
    

tiba1 = Car("siapa", "1401", "tiba1Sx")
print(tiba1)