# --------------------1------------------------
# li = [1, 5, 8, 19]
#
#
# def enu(lis, start=0):
#     count = start
#     for i in lis:
#         yield count, i
#         count += 1
#
#
# for i in enu(li):
#     print(i)
# --------------------2------------------------
# def fibonacci(x):
#     j = 0
#     li_fib = [0, 1]
#     for i in range(x-2):
#         s = li_fib[j] + li_fib[i + 1]
#         li_fib.append(s)
#         j += 1
#     yield li_fib
#
#
# print(list(fibonacci(10)))
# --------------------3------------------------
# li = [1, 9, 89, 7]
#
#
# def sum_gen(x:list):
#     yield x
#     total = 0
#     count = 1
#     for i in x:
#         total += i
#         yield li[0:count], total
#         count += 1
#
#
#
# sg = sum_gen(li)
# for i in sg:
#     print(i)
# --------------------4------------------------
# def reverse(s):
#     for i in reversed(s):
#         yield i
#
#
# print(tuple(reverse("Hossein")))
# --------------------5------------------------
# def even_or_odd(even_or_odd:str="e", count=0):
#     counter = 0
#     if even_or_odd.lower() == "o":
#         counter = 1
#     for i in range(count):
#         yield counter
#         counter += 2
#
#
# print(list(even_or_odd("O", 4)))
# --------------------6------------------------
# def star(x=0):
#     for i in range(1, x+1):
#         yield str(i) * i
#
#
# for j in star(5):
#     print(j)