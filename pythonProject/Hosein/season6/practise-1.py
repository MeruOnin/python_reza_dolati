# تابع len
# def length(s):
#     count = 0
#     for i in s:
#         count += 1
#     return count
#
#
# Input = {1,5,6,7 ,9}
# print(f"Your length: {length(Input)}")

# تابع min . max
# def maximum(a, b=0, *c):
#     while True:
#         if type(a) == int:
#             maxi = a
#             if b > maxi:
#                 maxi = b
#             for i in range(len(c)):
#                 if c[i] > maxi:
#                     maxi = c[i]
#             break

#         elif type(a) != int and type(a) != str:
#             maxi = 0
#             for i in range(len(a)):
#                 if a[i] > maxi:
#                     maxi = a[i]
#             if b > maxi:
#                 maxi = b
#             for j in range(len(c)):
#                 if c[j] > maxi:
#                     maxi = c[j]
#             break

#         elif type(a) == str:
#             maxi = "a"
#             for i in a:
#                 if ord(i.lower()) > ord(maxi.lower()):
#                     maxi = i
#             break
#     return maxi
#
#
# print(maximum("REZA"))

# تابع sum
# def total(a, b=0, *c):
#     while True:
#         if type(a) == int:
#             som = a + b
#             for i in range(len(c)):
#                 som += c[i]
#             break
#
#         elif type(a) != int and type(a) != str:
#             a = tuple(a)
#             som = 0
#             for i in range(len(a)):
#                 som += a[i]
#             som += b
#             for j in range(len(c)):
#                 som += c[j]
#             break
#
#         elif type(a) == str:
#             som = 0
#             for i in a:
#                 som += ord(i)
#             som = chr(som)
#             break
#     return som
#
#
# x = {23, 98, 76}
# print(total(x))

# تابع sqrt
# def sqrt(x):
#     y = int(x ** (1 / 2))
#     if y ** 2 == x:
#         return f"{y} * {y} => {x}...This number is square"
#     else:
#         return "This number is not square!"
#
#
# input_user = int(input("Enter your number: "))
# print(sqrt(input_user))

# تابع of
def of(a, b):
    dis_count = (a * b) // 100
    final_price = a - dis_count
    return final_price


firs_price = int(input("Enter your price: "))
discount_percent = int(input("Enter your discount percent: "))
print("The final price of the product is:", of(a=firs_price, b=discount_percent))

# تابع chartype
# from string import ascii_lowercase, ascii_uppercase, digits, punctuation
#
# lowerCase = list(ascii_lowercase)
# upperCase = list(ascii_uppercase)
# number = list(digits)
# symbol = list(punctuation)
#
#
# def char_type(x):
#     if x in lowerCase:
#         return "Your character is a lowercase letter"
#     elif x in upperCase:
#         return "Your character is a uppercase letter"
#     elif x in number:
#         return "Your character is a number"
#     elif x in symbol:
#         return "Your character is a symbol"
#     else:
#         return "Your character is unknown"
#
#
# Input = input("Enter your character: ")
# print("******************", '\n', char_type(Input), sep="")

