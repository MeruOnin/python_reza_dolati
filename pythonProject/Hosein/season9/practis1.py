# گرفتن ورود یاز کاربر نامحدود و ذخیره انها درون یک فایل txt
# with open("output.txt", "w"):
#     file = open("output.txt", "a")
#     while True:
#         Input = input("Enter the text (for exit program write 'Exit'):")
#
#         if Input.lower() != "exit":
#             file.write(Input + "\n")
#             continue
#         else:
#             print("you exit program!!!!!!")
#             file.close()
#             break

# --------------------------------------------------------------

# خواندن یک فایل و حذف فاصله های اضافی بین کلمات
# with open("data.txt", "r", encoding="utf-8") as file:  # باز کردن فایل در حالت خواندن
#     for line in file:
#         print(line.split())
#         cleaned_line = " ".join(line.split())  # حذف فاصله‌های اضافی بین کلمات
#         print(cleaned_line)

# ------------------------------------------------------------------

# خواندن فایل و شماردن تعداد کلمات تکرار شده
# import re
#
# # باز کردن فایل sample.txt در حالت خواندن
# with open("sample.txt", "r", encoding="utf-8") as file:
#     text = file.read().lower()  # خواندن محتوای فایل و تبدیل به حروف کوچک
#
# # استفاده از عبارت باقاعده برای پیدا کردن کلمات
# words = re.findall(r'\b\w+\b', text)  # پیدا کردن تمامی کلمات
#
# # شمارش تعداد تکرار هر کلمه
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# # چاپ هر کلمه و تعداد تکرار آن
# for word, count in word_count.items():
#     print(f"{word}: {count}")

# -----------------------------------------------------------------------

# کپی کردن محتویات فایل یبه فایل دیگر
with open("test.txt", "w", encoding="utf-8") as file:
    f = open("output.txt", "r", encoding="utf-8")
    text = f.read().lower()
    f.close()

    file.write(text)
    print("succesfuly")

# ------------------------------------------------------------------------