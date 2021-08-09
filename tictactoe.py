def x_win(game):
    for i in range(3):
        if game[3 * i] == game[3 * i + 1] == game[3 * i + 2] == "X":
            return True
        elif game[i] == game[i + 3] == game[i + 6] == "X":
            return True
    if game[2] == game[4] == game[6] == "X":
        return True
    elif game[0] == game[4] == game[8] == "X":
        return True
    return False


def o_win(game):
    for i in range(3):
        if game[3 * i] == game[3 * i + 1] == game[3 * i + 2] == "O":
            return True
        elif game[i] == game[i + 3] == game[i + 6] == "O":
            return True
    if game[2] == game[4] == game[6] == "O":
        return True
    elif game[0] == game[4] == game[8] == "O":
        return True
    return False


def move(player):
    while True:
        global board
        coordinates = input("Enter the coordinates:")
        coordinates = coordinates.split()

        if coordinates[0].isdigit() and coordinates[1].isdigit():
            if 1 <= int(coordinates[0]) <= 3 and 1 <= int(coordinates[1]) <= 3:
                if board[(int(coordinates[0]) - 1) * 3 + (int(coordinates[1]) - 1)] == "_":
                    board[3 * (int(coordinates[0]) - 1) + (int(coordinates[1]) - 1)] = player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    print("---------")
    print(f"| {board[0]} {board[1]} {board[2]} |")
    print(f"| {board[3]} {board[4]} {board[5]} |")
    print(f"| {board[6]} {board[7]} {board[8]} |")
    print("---------")

    if x_win(board):
        print("X wins")
        exit(0)
    elif o_win(board):
        print("O wins")
        exit(0)
    elif len([x for x in board if x == "_"]) == 0:
        print("Draw")
        exit(0)


board = list("_________")
print("---------")
print(f"| {board[0]} {board[1]} {board[2]} |")
print(f"| {board[3]} {board[4]} {board[5]} |")
print(f"| {board[6]} {board[7]} {board[8]} |")
print("---------")

while True:
    move("X")
    move("O")
