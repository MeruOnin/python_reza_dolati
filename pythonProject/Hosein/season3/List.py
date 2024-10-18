code1 = input("Enter your code: ")
name1 = input("Enter your name: ")
age1 = input("Enter your age: ")
number1 = input("Enter your number: ")
code2 = input("Enter your code1: ")
name2 = input("Enter your name1: ")
age2 = input("Enter your age1: ")
number2 = input("Enter your number1: ")
d = {
    code1: {"Name": name1,
            "Age": age1,
            "Number": number1},
    code2: {"Name1": name2, "Age1": age2, "Number1": number2}
    }
find = input("Enter your code: ")
if find in d:
    print(d[find]["Name", "Age"])
else:
    print("NO pain NO gain")
