# -----------------------1--------------------------
# def cen(works):
#     w = None
#     while True:
#         work = yield
#         if work in works:
#             work = "*" * len(work)
#             print(work)
#         else:
#             work = work
#             print(work)
#
#
# g = cen(["kony", "haromy", "koskesh"])
# next(g)
# g.send("kony")
# g.send("hosein")
# g.send("haromy")
# -----------------------2--------------------------
# def spl(spliter=" "):
#     while True:
#         word = yield
#         print(word.split(spliter))
#
#
# g = spl()
# next(g)
# g.send("Hosein Ali Amir Hadi Asghar")
# ------------------function-Attribute------------------
def func():
    print("love")


setattr(func, "age", "18")
print(getattr(func, "age", "000"))