from time import sleep

from mypy.dmypy_util import send

bookName, bookTitle, names, families = [], [], [], []


def input_user(lst1: list, lst2: list, count: int):
    for k in range(1, count+2):
        nam = yield
        fam = yield
        name = input(f"Your {nam}{k}: ")
        lst1.append(name)
        family = input(f"Your {fam}{k}: ")
        lst2.append(family)


def show(lst1: list, lst2: list):
    for r, u in enumerate(lst1):
        print(f"{r+1}) {u} {lst2[r]}")


def edit(lst1: list, lst2: list):
    while True:
        member_or_Books = yield
        mem_bok = yield
        mem_bok1 = yield
        choice = int(input(f"Enter your id {member_or_Books}: "))
        change = input(f"Enter new {mem_bok} and {mem_bok1} forExample:(Hossein Heidari)\n,"
                       f" If you want to change one of them, put 0 instead: ")
        spl = change.split()
        if spl[0] == "0":
            lst2[choice - 1] = spl[1]
        if spl[1] == "0":
            lst1[choice - 1] = spl[0]
        if spl[0] != "0" and spl[1] != "0":
            lst1[choice - 1] = spl[0]
            lst2[choice - 1] = spl[1]
        print("New information was successfully registered")
        sleep(3)


while True:
    print("**************************************")
    print("Select the desired option\n\t 1)Input user\n\t 2)Input book\n\t 3)User show\n\t 4)Book show\n\t"
          " 5)Edit user\n\t 6)Edit book\n\t 7)Exit")
    choose = input("Your choose: ")

    if choose == "1":
        print("*****************************************")
        countName = int(input("How many user? "))
        g = input_user(names, families, countName)
        next(g)
        for i in range(countName):
            g.send("name"), g.send("last name")
        else:
            continue

    elif choose == "2":
        print("*****************************************")
        countBook = int(input("How many book? "))
        g = input_user(bookName, bookTitle, countBook)
        next(g)
        for i in range(countBook):
            g.send("Book name"), g.send("Book title")
        else:
            continue

    elif choose == "3":
        print("*****************************************")
        print("Members is: ")
        show(names, families)
        continue

    elif choose == "4":
        print("*****************************************")
        print("Books is: ")
        show(bookName, bookTitle)
        continue

    elif choose == "5":
        show(names, families)
        g = edit(names, families)
        next(g)
        g.send("member"), g.send("name"), g.send("last name")
        continue

    elif choose == "6":
        show(names, families)
        g = edit(names, families)
        next(g)
        g.send("books"), g.send("name"),g.send("title")
        continue

    elif choose == "7":
        break

    else:
        print("\nYour choose is wrong!\n\t Try again:")