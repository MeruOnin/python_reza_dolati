# اعداد زوج بین 0 تا100

# y = 1
# x = 0
# while x <= 100:
#     if x % 2 == 0:
#         print(f"Even{y}: {x}")
#         y += 1
#     x += 1

# --------------مثلث ستاره ای-----------

# i = 1
# j = 0
# while i <= 10:
#     print(f"{'*' * i:>30}", end="")
#     print(f"{'*' * j:<}")
#     i += 1
#     j += 1

# 10 تا دانشجو و 5 گروه یکی از اخر یکی از اول

# numberStudent = 10
# x = 1
# i = 1
# while i <= 5:
#     print(f"Group{x}: {numberStudent, i}")
#     numberStudent -= 1
#     i += 1
#     x += 1

# مقسوم علیه های یک عدد را چاپ کنید!

# i = 1
# h = 1
# number = int(input("Enter your number: "))
# while i <= number:
#     if number % i == 0:
#         print(f"number{h}: {i}")
#         h += 1
#     i += 1

# مشخص کردن عدد کامل

# i = 1
# List = []
# Number = int(input("Enter your number: "))
# while i <= Number:
#     if Number % i == 0:
#         List.append(i)
#     i += 1
# Len = len(List)
# Sum = sum(List[0:(Len-1)])
# if Sum == Number:
#     print("Your number is full.")
# else:
#     print("Your number is not full!")

#   1,1,2,3,5,8,13,...چاپ اعداد کاموناتی

# l1 = []
# i = 1
# x, y = 1, 0
#
# while i <= 10:
#     l1.append(x)
#     x, y = x+y, x
#     i += 1
# print(l1)
