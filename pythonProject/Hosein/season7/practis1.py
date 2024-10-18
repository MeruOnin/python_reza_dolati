# گرفتن رشته و چاپ طول آن رشته

# if (s := len(input("Enter: "))) > 10:
#     print(s)
# else:
#     print("kos")
# ----------------------------------
# لیست و جمع دو عنصر اول آن

# lis = [1, 2, 3, 4, 5, 10]
# if (n := len(lis)) > 5:
#     print(sum(lis[0:2]))
# --------------------------------------
# مجموع ورودی اعداد کاربر تا زمانی که یک رشته خالی نزده است

# Sum = 0
# while (number := input("Enter your number (space fot exit): ")) != " ":
#     Sum += int(number)
#
# print(Sum)
# --------------------------------------
# چک کردن یک عدد خاص در یک لیست وجود دارد یا خیر

# li = [1, 3, 5, 6]
# if (n := int(input("enter your number"))) in li:
#     print(li.index(n))
# else:
#     print("jos")
# --------------------------------------
# اعداد تصادفی
# from random import randint
# count = 1
# li = []
# while (rand := randint(1, 101)) <= 80:
#     count += 1
#     li.append(rand)
# print(rand, count, li)
# ----------------------------------------
# جمله کاربر و تعداد حروف آن
# if (sentence := input("یک جمله وارد کنید: ")):
#     # شمارش تعداد کلمات
#     word_count = len(sentence.split())
#     # چاپ تعداد کلمات
#     print(f"تعداد کلمات: {word_count}")

