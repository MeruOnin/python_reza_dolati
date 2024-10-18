# تابع range به وسیله تابع عادی
# def list_range(x, y, z=1):
#     li = []
#     while x <= y:
#         li.append(x)
#         x += z
#     return li

# تابع range به وسیله ژنراتور


# def generator(start, end, step=1):
#     while start <= end:
#         yield start
#         start += step


# زمان اجرای تابع ساده و ژنراتور
# start = perf_counter()
# lr = list_range(1, 10000000)
#
# for i in lr:
#     if i == 3:
#         break
#     s = 0
#     s += i
# end = perf_counter()
# print(end - start)


# --------------------------------
# start1 = perf_counter()
# gr = generator(1, 10000000000000000000000000000000)
# for i in gr:
#     if i == 3:
#         break
#     s = 0
#     s += i
# end1 = perf_counter()
# print(end1 - start1)
# silvent
