#گرفتن دو ورودی و بگوید که عدد یک رقمی چند بار تکرار شده

# def repeat(number, single_digit):
#     count = 0
#     while number > 0:
#         if number % 10 == single_digit:
#             count += 1
#         number //= 10
#     return count
#
#
# number = int(input("Enter your number: "))
#
# while True:
#     digit = int(input("Enter your single digit number: "))
#     if len(str(digit)) == 1:
#         break
#     else:
#         print("***********************\nShould was your number one digit...\n***********************")
#
# print(f"The number of {digit} in {number} repetitions : {repeat(number=number, single_digit=digit)} ")


# تابع مجموع فاکتوریل عدد که کاربر وارد کرده

# def factorial(x):
#     factory = 1
#     for i in range(1, x+1):
#         factory *= i
#     return factory
#
#
# def sum_factorial(x):
#     sum_factory = 0
#     for i in range(1, x+1):
#         sum_factory += factorial(i)
#     return sum_factory
#
#
# fact = int(input("Enter the number to get the factorial: "))
# print(f"Factorial is: {factorial(fact)}\nfactorial sum is: {sum_factorial(fact)}")

