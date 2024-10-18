# ------------------------1----------------------------
# تعداد زوج و فرد یک لیست lambda
# li = [2, 6, 9, 10, 6, 7, 33]
# print(len(list(filter(lambda x: x % 2 == 0, li))))
# print(len(list(filter(lambda y: y % 2 != 0, li))))
# ------------------------2----------------------------
# مرتب سازی lambda
# li = [("Ali", 9), ("Reza", 1), ("Hosein", 7)]
# print(sorted(li, key=lambda x: x[1]))
# ------------------------3----------------------------
# dict lamda
# li = [{'weight': 90, 'color': "red"},
#       {'weight': 30, 'color': "blue"},
#       {'weight': 100, 'color': "yellow"}
#       ]
# li.sort(key=lambda x: x['color'])
# print(li)
# ------------------------4----------------------------
# filter زوج و فرد
# li = [2, 7, 9, 18, 259, 87, 4, 10]
# print(list(filter(lambda x: x % 2 == 0, li)))
# print(list(filter(lambda x: x % 2 != 0, li)))
# ------------------------5----------------------------
# map مکعب  مربع
# li = [2, 7, 9, 18, 259, 87, 4, 10]
# print(li)
# print(list(map(lambda x: x ** 2, li)))
# print(list(map(lambda x: x ** 3, li)))
# ------------------------6----------------------------
# شروع رشته با یک کاراکتر مشخض شده
# st = "Hossein"
# Lambda = lambda x: x[0] == 'h'
# print(Lambda(st.lower()))
# ------------------------7----------------------------
# رشته وارد شده عددی است یا خیر
# st = "23.6"
# Lambda = lambda x: x.replace(".", "", 1).isnumeric()
# print(Lambda(st))
