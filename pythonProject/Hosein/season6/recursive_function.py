# def recursive_fact(x):
#     if x == 0 or x == 1:
#         return 1
#     return x * recursive_fact(x-1)
#
#
# print(recursive_fact(5))
# ------------------timer--------------------
# from time import sleep
# def rec_timer(x):
#     sleep(1)
#     if x == 0:
#         return 0
#     print(x)
#     sleep(1)
#     rec_timer(x-1)
#
#
# rec_timer(10)
# ------------------fibonacci--------------------
# fib = [0, 1]
# i = 0
#
#
# def rec_fibonacci(x):
#     if len(fib) >= x:
#         return
#     global i
#     fib.append(fib[i]+fib[i+1])
#     i += 1
#     rec_fibonacci(x)
#     return fib
#
#
# print(rec_fibonacci(10))
# ------------------mezrab--------------------
# def math(li: list):
#     s = 1
#     for j in li:
#         s *= j
#     return s
#
#
# lst = []
# i = 0
#
#
# def rec_num_mul5(x):
#     global i
#     if i == len(str(x)):
#         return
#     if int(x[i]) <= 5:
#         lst.append(int(x[i]))
#     i += 1
#     rec_num_mul5(x)
#     return math(lst)
#
#
# print(rec_num_mul5("2879156342"))
# ------------------mezrab1--------------------
# def mul5(x):
#     if x == 0:
#         return 1
#     if x % 10 >= 5:
#         return x % 10 * mul5(x//10)
#     else:
#         return mul5(x//10)
#
#
# print(mul5(1029397824))
# -----------------------------------
# حاصل ضرب ارقام بالاتر از 5
# def mul5(x):
#     if x == 0:
#         return 1
#     elif x % 10 >= 5:
#         return x % 10 * mul5(x//10)
#     elif x % 10 < 5:
#         return mul5(x // 10)
#
#
# print(mul5(345))

# اعداد بخش پذیر به 5 را چاپ کند

# def func(x):
#     if x < 3:
#         return
#     elif x % 3 == 0:
#         print(x)
#         func(x-1)
#     else:
#         func(x-1)
#
#
# func(12)

# دنباله فیبوناچی
# lis = [0, 1]
# i = 0
# j = 1
#
#
# def fib(x):
#     global i, j, lis
#     if x == 0:
#         return 0
#     else:
#         h = i + j
#         i = j
#         j = h
#         lis.append(h)
#     fib(x - 1)
#     return lis
#
#
# print(fib(5))
