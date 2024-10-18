from PIL import Image
import os


def convert_to_png(input_path):
    # چک کردن وجود فایل ورودی
    if not os.path.exists(input_path):
        print(f"فایل {input_path} وجود ندارد")
        return False

    try:
        # بارگذاری تصویر
        img = Image.open(input_path)

        # گرفتن نام فایل بدون پسوند
        file_name, _ = os.path.splitext(input_path)

        # تعیین مسیر خروجی
        output_path = f"{file_name}.png"

        # ذخیره تصویر با فرمت PNG
        img.save(output_path, "PNG")
        print(f"تصویر به فرمت PNG تبدیل شد و در {output_path} ذخیره شد.")

        # حذف نسخه قبلی عکس
        os.remove(input_path)
        print(f"نسخه قبلی عکس {input_path} حذف شد.")

        return True
    except Exception as e:
        print(f"خطا در تبدیل فایل {input_path}: {e}")
        return False


def convert_folder_to_png(folder_path):
    # چک کردن وجود پوشه ورودی
    if not os.path.exists(folder_path):
        print("پوشه ورودی وجود ندارد")
        return

    # بررسی تمامی فایل‌های موجود در پوشه
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # تبدیل فایل به فرمت PNG
        if os.path.isfile(file_path):
            convert_to_png(file_path)


# مسیر پوشه ورودی را مشخص کنید
folder_path = "D:\\logo\\آذربایجان غربی"

convert_folder_to_png(folder_path)
