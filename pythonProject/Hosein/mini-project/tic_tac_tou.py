from termcolor import colored

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player, computer = "X", "O"
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2))
com_winners = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))

def print_board():
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n"
        if i == "X":
            print(colored(f"[{i}]", "red"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "blue"), end=end)
        else:
            print(colored(f"[{i}]", "white"), end=end)
        j += 1


def has_empty_space():
    return board.count("X") + board.count("O") != 9


def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False


def is_winner(brd, plyr):
    win = True
    for winner in winners:
        win = True
        for j in winner:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve-1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve-1] = mve
        return True, win
    return False, False


def computer_move():
    mov = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mov = i
            break
    if mov == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mov = j
                break
    if mov == -1:
        for tup in com_winners:
            for h in tup:
                if mov == -1 and can_move(board, h):
                    mov = h
                    break
    return make_move(board, computer, mov)


print(f"Player: {player}\ncomputer: {computer}\n")


while has_empty_space():
    print_board()
    print()
    move = int(input("Choose your move: "))
    moved, win = make_move(board, player, move)
    if not moved:
        print("try again!")
        continue
    if win:
        print("you winner(:")
        break
    elif computer_move()[1]:
        print(colored("you lose!", "yellow"))
        break


print()
print_board()
if board.count("X") + board.count("O") == 9:
    print()
    print(colored("not result", "yellow"))
