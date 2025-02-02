# def sum_list(lis: list[int]):
#     try:
#         sum = int()
#         for i in lis:
#             sum += i
#         print(sum)
#     except TypeError as te:
#         print(te.__class__.__name__)


# sum_list([1, 4, 5, "6", 7])
# print("ok!")

#------------------------------------------------

# try:
#     with open("file1.txt", "r") as file:
#         file.read()
# except FileNotFoundError as fne: 
#     print(fne.__class__.__name__)

#---------------------------------------------------

# def dict_key(dic: dict, key: str):
#     try:
#         print(dic[key])
#     except KeyError as ke:
#         print(ke.__class__.__name__)


# dict_key({"s": 54, "g": 43}, "s")

#------------------------------------------------------

# def str_to_int(string: str):
#     try:
#         number = int(string)
#         print(number)
#     except ValueError as ve:
#         print(ve.__class__.__name__)


# str_to_int("k")

