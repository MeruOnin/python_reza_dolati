# name = bytearray("Hossein", "utf-8")
# li = [hex(i) for i in name]
# print(li)
# ----------------------------------
# name = 0x48
# bytarray = bytearray(chr(name), "utf-8")
# print(bytarray)
# print(type(bytarray))
# ----------------------------------
# name = bytearray("Hossein", "utf-8")
# name[0] = 0x45
# print(name)
# ----------------------------------
name = bytes("Hossein", "utf-8")
name2 = bytes("Anahita", "utf-8")
name3 = name2+name
print(name3)
print(type(name3))
# ----------------------------------
# name = bytearray("Hossein", "utf-8")
# li = [i for i in name]
# print(li)
# ----------------------------------
# name = bytes("Hossein", "utf-8")
# name1 = bytearray("AmirH", "utf-8")
# if name[0] in name1:
#     print('yes')
# else:
#     print("no")
# ----------------------------------
