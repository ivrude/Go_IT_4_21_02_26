a = int(input())

matrix = [[" " for _ in range(a)] for _ in range(a)]
win = False
current_player = "x"

while True:
    h = int(input())
    w = int(input())
    matrix[h-1][w-1] = current_player
    print(matrix)
    for i in range(a):
        if matrix[h-1][i] != current_player:
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



