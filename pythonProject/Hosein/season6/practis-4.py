# ----------- مجموع لیست----------
# lis = [2, 6, 8, 10, 98]
# i = 0
# Sum = 0
#
#
# def sumList(li):
#     global i, Sum
#     if i >= len(li):
#         return
#     else:
#         Sum += li[i]
#         i += 1
#         sumList(li)
#     return Sum
#
#
# print(sumList(lis))

# ------------------توان یک عدد-----------------
# i = 0
# def exp(x):
#     global i
#     if i >= 10:
#         return
#     else:
#         print(x ** i)
#         i += 1
#         exp(x)
#
#
# exp(2)

# ----------------------معکوس رشته ----------------------
# i = -2
#
#
# def recursive(s):
#     global i
#     if i == -2:
#         i = len(s) - 1
#         print(s[i].lower(), end="")
#         i -= 1
#         recursive(s)
#     elif i < 0:
#         return
#     else:
#         print(s[i].lower(), end="")
#         i -= 1
#         recursive(s)
#
#
# recursive("Hosi")
# ----------------------تعداد تکرار عنصر در یک لیست -------------------
