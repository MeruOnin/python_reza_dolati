#composition
# class Question:
#     def __init__(self, q, a):
#         self.question = q
#         self.answer = a


# class ExamPaper:
#     def __init__(self):
#         self.examp = [Question("What is your name?", "My name is Hossein"), Question("How old are you?", "I am 18 year old")]

#     def __str__(self):
#         for emp in self.examp:
#             print(f"{emp.question}: {emp.answer}\n")

# exmpale = ExamPaper()
# print(exmpale)

#aggrigation
class Students:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class University:
    def __init__(self, students: list[Students]):
        self.students = students



st = [Students("Hossein", "13"), Students("Amir", "1")]
da = University(st)
for i in da.students:
    print(i)