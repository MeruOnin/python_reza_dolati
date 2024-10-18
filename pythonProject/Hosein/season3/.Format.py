# x = 5
# y = 8
# s = x * y
# p = (2 * x) + (2 * y)
# print(" s is : ریال{:<20,}".format(5424556))

# -------------------------

dic = {"Allah": "God", "sign": "symbol", "good": "great", "every": "each", "match": "choose"}
Input = int(input("Enter your phrase('Allah'{1}-'sign'{2}-'good'{3}-'every'{4}-'match'{5}): "))
if Input == 1:
    print(f"Your phrase mani: {dic["Allah"]}")
elif Input == 2:
    print(f"Your phrase mani: {dic["sign"]}")
elif Input == 3:
    print(f"Your phrase mani: {dic["good"]}")
elif Input == 4:
    print(f"Your phrase mani: {dic["every"]}")
elif Input == 5:
    print(f"Your phrase mani: {dic["match"]}")
else:
    print("kos matheret!")