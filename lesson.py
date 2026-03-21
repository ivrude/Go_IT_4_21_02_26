import random

a = int(input())

matrix = [[" " for _ in range(a)] for _ in range(a)]
win = False
current_player = "x"

while True:
    if current_player == "x":
        h = int(input())
        w = int(input())

    else:
        h = random.randint(1, a)
        w = random.randint(1, a)

    if matrix[h - 1][w - 1] == " ":
        matrix[h-1][w-1] = current_player

        for col in matrix:
            print(col)
    else:
        print("Invalid move!")
        continue

    for i in range(a):
        if matrix[h-1][i] != current_player:
            win = False
            break
        else:
            win = True
    if not win:
        for i in range(a):
            if matrix[i][w - 1] != current_player:
                win = False
                break
            else:
                win = True
    if not win:
        for i in range(a):
            if matrix[i][i] != current_player:
                win = False
                break
            else:
                win = True
    if not win:
        for i in range(a):
            if matrix[i][a - i - 1] != current_player:
                win = False
                break
        else:
            win = True

    if win:
        print(f"{current_player} wins!")
        break
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"



