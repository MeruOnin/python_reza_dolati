from rembg import remove
from PIL import Image
import subprocess
import os

# مسیر فایل ورودی (و خروجی)
file_path = 'D:\\jon.png'
temp_path = 'D:\\temp.png'
pngquant_path = 'C:\\Users\\husinw\\Downloads\\New folder\\pngquant\\pngquant.exe'  # مسیر دقیق به pngquant.exe

# باز کردن تصویر ورودی
input_image = Image.open(file_path)

# حذف بک‌گراند
output_image = remove(input_image)

# ذخیره تصویر خروجی به صورت موقت
output_image.save(temp_path, format='PNG')

# استفاده از pngquant برای فشرده‌سازی بیشتر و بازنویسی فایل اصلی
result = subprocess.run([pngquant_path, '--force', '--output', file_path, temp_path], capture_output=True, text=True)

# چاپ خروجی و بررسی خطا
if result.returncode != 0:
    print("Error occurred:", result.stderr)
else:
    # حذف فایل موقت در صورت موفقیت
    os.remove(temp_path)
    print("بک‌گراند تصویر با موفقیت حذف و تصویر اصلی با حجم کمتر ذخیره شد.")
