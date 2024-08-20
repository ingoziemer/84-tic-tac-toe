import pandas as pd


game_on = True
columns = ["A", "B", "C"]
field = pd.DataFrame(columns=columns, index=range(1, 4))
field["A"] = ""
field["B"] = ""
field["C"] = ""


# win condition for columns
def check_col():
    continue_game = None
    for col in columns:
        try:
            if field[col].value_counts()[""] > 0:
                continue_game = True
        except KeyError:
            try:
                if field[col].value_counts()["O"] == 3:
                    print("Player O has won.")
                    continue_game = False
                    break
            except KeyError:
                if field[col].value_counts()["X"] == 3:
                    print("Player X has won.")
                    continue_game = False
                    break
    return continue_game


# win condition for rows
def check_row():
    continue_game = None
    for n in range(1, 4):
        if field["A"][n] == field["B"][n] == field["C"][n]:
            if field["A"][n] == "O":
                print("Player O has won.")
                continue_game = False
                break
            elif field["A"][n] == "X":
                print("Player X has won.")
                continue_game = False
                break
            else:
                continue_game = True
        else:
            continue_game = True
    return continue_game


def check_diagonal():
    if field["A"][1] == field["B"][2] == field["C"][3]:
        if field["A"][1] == "O":
            print("Player O has won.")
            continue_game = False
        elif field["A"][1] == "X":
            print("Player X has won.")
            continue_game = False
        else:
            continue_game = True

    elif field["A"][3] == field["B"][2] == field["C"][1]:
        if field["A"][3] == "O":
            print("Player O has won.")
            continue_game = False
        elif field["A"][3] == "X":
            print("Player X has won.")
            continue_game = False
        else:
            continue_game = True
    else:
        continue_game = True
    return continue_game


def check_win():
    check_diagonal()
    check_row()
    check_col()


def turn(player):
    choice = list(input(f"Player {player.upper()}: "))
    index = int(choice[1])
    if field.at[index, choice[0]] == "":
        field.at[index, choice[0]] = player
    else:
        print("Field is already occupied.")
        turn(player)


print(field)
print("Choose A, B, C for column and 1, 2, 3 for row. e.g.: for 'middle, lower': 'B3'")

while game_on:
    turn("X")
    print(field)
    game_on = check_col()
    if not game_on:
        break
    game_on = check_row()
    if not game_on:
        break
    game_on = check_diagonal()
    if not game_on:
        break

    turn("O")
    print(field)
    game_on = check_col()
    if not game_on:
        break
    game_on = check_row()
    if not game_on:
        break
    game_on = check_diagonal()
    if not game_on:
        break
