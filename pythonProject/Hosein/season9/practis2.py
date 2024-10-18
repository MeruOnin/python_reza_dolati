# def parse(str_json: str, key_json: str):
#     import json
#     jl = json.loads(str_json)
#     tj = type(str_json)
#     tjl = type(jl)
#     return jl, tjl, str_json, tj, jl[key_json]
#
#
# s = '{"f": 23, "a": 35}'
# print(parse(s, "f"), end="\n")
import csv
import json


# def parse(str_json: str, key: str, value):
#     import json
#     jl = json.loads(str_json)
#     jl[key] = value
#     return json.dumps(jl)
#
#
# s = '{"f": 23, "a": 35}'
# print(parse(s, "hosein", 18), end="\n")


# import json
# from collections import Counter
#
#
# def count_unique_values(json_string):
#     # تبدیل رشته JSON به لیست دیکشنری‌ها
#     data = json.loads(json_string)
#     print(data)
#     # استخراج مقادیر منحصر به فرد
#     values = [item['color'] for item in data]
#
#     # شمارش تعداد هر مقدار منحصر به فرد
#     value_counts = Counter(values)
#     print(value_counts)
#     return dict(value_counts)
#
#
# # مثال استفاده:
# json_string = '[{"color": "red"}, {"color": "blue"}, {"color": "red"}, {"color": "green"}]'
# result = count_unique_values(json_string)
# print(result)


# def comid(string_json1, string_json2):
#     data1 = json.loads(string_json1)
#     data2 = json.loads(string_json2)
#
#     if isinstance(data1, dict) and isinstance(data2, dict):
#         combit_data = {**data1, **data2}
#     elif isinstance(data1, list) and isinstance(data2, list):
#         combit_data = data2 + data1
#     else:
#         raise ValueError("باید هر دو فایل یا دیشکنری باشد یا لیست")
#
#     return json.dumps(combit_data)
#
#
# d = '{"color": "red", "age": "green"}'
# d1 = '{"name": "hossein", "height": 54}'
#
# print(comid(d, d1))


# import json
# import csv
#
# json_string = '[{"color": "green", "age": "23", "name": "hossein"}, {"color": "red", "age": "24", "name": "amir"}]'
#
#
# def csv_file(str_json):
#     data = json.loads(str_json)
#
#     # استخراج کلیدها از اولین دیکشنری
#     row1 = list(data[0].keys())
#
#     # باز کردن فایل CSV با newline=''
#     with open("csv_file.csv", "w", newline='') as file:
#         write = csv.writer(file)
#
#         # نوشتن هدر (کلیدهای دیکشنری)
#         write.writerow([row1[0], row1[1], row1[2]])
#
#         # نوشتن مقادیر هر دیکشنری
#         for i in data:
#             write.writerow([i[row1[0]], i[row1[1]], i[row1[2]]])
#
#
# # فراخوانی تابع
# csv_file(json_string)

# import csv
#
#
# def sum_csv_column(file_path, column_name):
#     total = 0
#
#     # باز کردن فایل CSV
#     with open(file_path, mode='r') as file:
#         csv_reader = csv.DictReader(file)
#
#         # پیمایش سطرهای فایل
#         for row in csv_reader:
#             # چک کردن اینکه مقدار ستون عددی است یا خیر
#             value = row[column_name]
#             if value.isdigit():  # اگر مقدار عددی باشد
#                 total += int(value)  # جمع کردن مقدار عددی
#
#     return total
#
#
# # مثال استفاده
# file_path = 'csv_file.csv'
# column_name = 'age'
# result = sum_csv_column(file_path, column_name)
# print(f'The sum of the column "{column_name}" is: {result}')
