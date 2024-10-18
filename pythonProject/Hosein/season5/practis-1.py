# نمایش اعداد ما بین دو عدد

# l2 = []
# for j in range(1, 3):
#     number = int(input(f"Enter your number{j}: "))
#     l2.append(number)
#
# l1 = []
# Min = min(l2)
# Max = max(l2)
# i = Min
# while i < Max-1:
#     Min += 1
#     l1.append(Min)
#     i += 1
# print(f"numbers between: {l1}")
# ----------------2-----------------

# x = int(input("x: "))
# y = int(input("y: "))
# Min = min(x, y)
# Max = max(x, y)
# l1 = []
# for i in range(Min, Max-1):
#     append = l1.append(Min)
#     Min += 1
# print(l1)

# مقسوم علیه های مشترک و بزرگترین آنها

# number1 = int(input("Enter your number1: "))
# number2 = int(input("Enter your number2: "))
#
# i, j = 1, 1
# l1, l2 = [], []
# while j <= number1:
#     if number1 % j == 0:
#         l1.append(j)
#     j += 1
#     while i <= number2:
#         if number2 % i == 0:
#             l2.append(i)
#         i += 1
# sl1, sl2 = set(l1), set(l2)
# eshterak = list(sl1.intersection(sl2)))
# print("max:", max(eshterak))
# --------------2--------------

# x = int(input("x: "))
# y = int(input("y: "))
# Min = min(x, y)
# Max = max(x, y)
# l1 = []
# for i in range(1, Min+1):
#     if Min % i == 0 and Max % i == 0:
#         l1.append(i)
# print(max(set(l1)))

# کوچکترین مضرب مشترک 2 عدد

# number1 = int(input("Enter your number1: "))
# number2 = int(input("Enter your number2: "))
#
# l1, l2 = [], []
# for i in range(1, 101):
#     if i % number1 == 0:
#         l1.append(i)
# for j in range(1, 101):
#     if j % number2 == 0:
#         l2.append(j)
# sl1, sl2 = set(l1), set(l2)
# subscription = sl2.intersection(sl1)
# if subscription:
#     print("Min:", min(subscription))
# else:
#     print("does not subscribe!")
# -------------2---------------

# x = int(input("x: "))
# y = int(input("y: "))
# i = 1
# l1, l2 = [], []
# for j in range(1, min(x, y) + 1):
#     l1.append(x * i)
#     l2.append(y * i)
#     i += 1
# print(min(set(l1).intersection(set(l2))))

# تعداد رقم های عدد

# count = 0
# Input = input("Enter your number: ")
# for i in Input:
#     count += 1
# Input = int(Input)
# print(count)
# print(type(Input))

# ستاره ها

# Input = int(input("Enter rows: "))
# i = 1
# while i <= Input:
#     print(f"{'*' * i:>30}", end="")
#     print()
#     i += 1
# for _ in range(Input-1, 0, -1):
#     print(f"{'*' * _:>30}", end="")
#     print()

# لیست حدسی

# from random import choice
# listName = ["Hossein", "Ali", "Mohsen", "Mobina", "Anahita", "Mohammad", "Hadi", "Amir", "Darya", "Sahel"]
# print('Imagine a name in your mind as {"Hossein", "Ali", "Mohsen", "Mobina", "Anahita", "Mohammad", "Hadi", '
#         '"Amir", "Darya", "Sahel"}:)')
# Input = input("Are you ready: ")
# if Input.lower() == "yes":
#     while True:
#         Choice = choice(listName)
#         print(f"Your mental name is: {Choice}")
#         guessRight = input("Did I guess right? ")
#         if guessRight == "no":
#             listName.remove(Choice)
#             continue
#         else:
#             print("*" * 40)
#             print("welcom!")
#             break

