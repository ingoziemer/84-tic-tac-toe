import os

print('Welcome to the Tic Toe Game: \n')

board_list = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/Mac
    else:
        os.system('clear')


def displayboard(array):
    for roll in array:
        print(" | ".join(roll))
        print("-" * 10)


displayboard(board_list)


def check_for_win(board, player):
    print(player)
    # Check rows
    for x in board:
        if all([cell == player for cell in x]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def draw(board):
    for y in board:

        if all([cell != '_' for cell in y]):
            return True


Game_on = True
active_player = 'X'

while Game_on:

    try:
        row, col = map(int, input('Please enter a (row and column) E.g 0,1,2 : ').split(','))

    except IndexError:
        print('list index out of range(0, 1, 2)')
        row, col = map(int, input('Please enter a (row and column) E.g 0,1,2 : ').split(','))

    if board_list[row][col] == '_':

        board_list[row][col] = active_player

        displayboard(board_list)

        # Check win
        if check_for_win(board_list, active_player):
            displayboard(board_list)
            print(f"Player {active_player} wins!")
            break

        # Check draw
        if draw(board_list):
            displayboard(board_list)
            print("The game is a draw!")
            break

        # Switch players
        active_player = "O" if active_player == 'X' else "X"
    else:
        print('Selected Cell is not Empty, Please choose another Cell')
        clear_screen()
        continue