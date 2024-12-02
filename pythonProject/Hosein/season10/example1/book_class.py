class Book:
    def __init__(self, title: str, year: str, nevi: str) -> None:
        self.title = title
        self.year = year
        self.nevisandeh = nevi

    def __str__(self):
        return f"{self.title}\n{self.year}\n{self.nevisandeh}"
    

book1 = Book("هنر رندانه به تخم گرفتن", "1400", "چووم")

print(book1)