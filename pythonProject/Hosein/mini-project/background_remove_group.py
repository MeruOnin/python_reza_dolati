import cv2
import os


def remove_background(folder_path):
    # لیست فایل‌های موجود در پوشه
    files = os.listdir(folder_path)

    for file in files:
        # مسیر فایل
        file_path = os.path.join(folder_path, file)

        # بارگذاری تصویر
        image = cv2.imread(file_path)

        # تبدیل تصویر به مقیاس رنگی خاکستری
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # تبدیل تصویر به مقیاس سیاه و سفید
        _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

        # اگر بک‌گراند سفید یا مشکی باشد، حذف شود
        if (binary == 255).all() or (binary == 0).all():
            continue

        # ذخیره تصویر با بک‌گراند تغییر یافته
        cv2.imwrite(file_path, image)


# مسیر پوشه حاوی تصاویر
folder_path = "D:\\clonShop\\Clone-shop--modern--1\\assets\\products_img"

remove_background(folder_path)
