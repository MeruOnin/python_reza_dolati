class Student:
    def __init__(self, name:str, age: int, scores: list[float]) -> None:
        self.name = name
        self.age = age
        self.scores = scores

    def add_score(self):
        while True:
            try:
                score = float(input("Enter your score: "))
                self.scores.append(score)
                print("succefully")
                break
            except:
                print("pleas enter number type: ")
                continue
        
    def average(self):
        return f"Your average scores:\n\t{(sum(self.scores)) / (len(self.scores))}"
    

ali = Student("ali", 13, [12, 19, 20, 12])

ali.add_score()

print(ali.average())