from random import randint
x = 0
while True:
    ready = input("Are you ready? ")
    if ready == "yes":
        x += 1
        print(f"({randint(0, 20)})*number{x}*")
    elif ready == "no":
        continue
    else:
        break
