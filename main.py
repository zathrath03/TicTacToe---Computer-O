from os import system, name
import random

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
valid = [0,1,2,3,4,5,6,7,8,9]
xs = []
os = []

def drawboard():
    # Clears the screen
    command = 'clear'
    if name in ('nt', 'dos'):
        command = 'cls'
    system(command)

    # Prints the board
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[0] + '|' + board[1] + '|' + board[2])


def checkwinner(player):
    if ((board[6] == board[7] == board[8] != " ")
            or (board[3] == board[4] == board[5] != " ")
            or (board[0] == board[1] == board[2] != " ")
            or (board[6] == board[3] == board[0] != " ")
            or (board[7] == board[4] == board[1] != " ")
            or (board[8] == board[5] == board[2] != " ")
            or (board[6] == board[4] == board[2] != " ")
            or (board[8] == board[4] == board[0] != " ")):
        drawboard()
        print(f"Player {player} wins!")
        return True


def clearboard():
    for i in range(len(board)):
        board[i] = " "


def promptPlayAgain():
    guess = input("Enter yes to play again. ").lower()
    if guess == "yes" or guess == "y":
        for i in range(len(board)):
            board[i] = str(i + 1)
        return True


def OsChoice():
    """
    valid = []
    xs = []
    os = []

    for i in range(len(board)):
        if board[i] == " ":
            valid.append(i)
        if board[i] == "X":
            xs.append(i)
        elif board[i] == "O":
            os.append(i)
    """
    # If it's the second turn and the center isn't taken, take the center
    if 4 in valid:
        valid = [4]
    # Prioritizes 3 Os, then block 3 Xs
    elif len(temp := winorblock(os, valid)) > 0:
        valid = temp
    elif len(temp := winorblock(xs, valid)) > 0:
        valid = temp
    # If it's the fourth turn, O is in center, and X has at least one corner, take an edge
    elif len(valid) == 6 and 4 in os and any(i in xs for i in (0, 2, 4, 6)):
        valid = list(set(valid) & {1, 3, 5, 7})
    # Otherwise, take a corner if available
    elif 0 in valid or 2 in valid or 6 in valid or 8 in valid:
        valid = list(set(valid) & {0, 2, 6, 8})

    return random.choice(valid)


def winorblock(positions, valid):
    best = []
    
    # Checking for two of the same player in a row
    for i in positions:
        for j in positions:
            if (i,j) in ((1,2), (3,6), (4,8)): best.append(0)
            if (i,j) in ((0,2), (4,7)): best.append(1)
            if (i,j) in ((0,1), (4,6), (5,8)): best.append(2)
            if (i,j) in ((0,6), (4,5)): best.append(3)
            if (i,j) in ((0,8), (1,7), (2,6), (3,5)): best.append(4)
            if (i,j) in ((3,4), (2,8)): best.append(5)
            if (i,j) in ((0,3), (2,4), (7,8)): best.append(6)
            if (i,j) in ((1,4), (6,8)): best.append(7)
            if (i,j) in ((0,4), (2,5), (6,7)): best.append(8)
    
    # Uses the intersection of the best and valid sets
    return list(set(best) & set(valid))


def game():
    turn = 0
    player = "X"

    drawboard()
    clearboard()

    print(
        "Welcome to tic-tac-toe! You'll be using the numbers above to indicate where you want to play.\n(looks like your numpad)"
    )
    input("Press Enter to continue")

    while True: 
        drawboard()
        print(f"It is {player}'s turn. Please choose a square.")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            drawboard()
            print(
                f"{choice} is not a valid input. Enter a number from 1 to 9 to select a square."
            )
            input("Press Enter to continue.")
            continue

        if choice < 1 or choice > 9:
            drawboard()
            print(
                f"{choice} is not a valid input. Enter a number from 1 to 9 to select a square."
            )
            input("Press Enter to continue.")
            continue

        if board[choice - 1] != " ":
            drawboard()
            print(
                f"You're not allowed to choose a square that has already been chosen."
            )
            input("Press Enter to continue.")
            continue

        board[choice - 1] = player
        xs.append(choice-1)
        valid.remove(choice-1)
        turn += 1

        if turn >= 5 and checkwinner(player):
            break
        
        if turn == 9:
            drawboard()
            print("It's a draw!")
            break

        choice = OsChoice()
        board[choice] = "O"
        os.append(choice)
        valid.remove(choice)
        turn += 1
        
        if turn >= 5 and checkwinner("O"):
            break
        

if __name__ == "__main__":
    game()
    while promptPlayAgain():
        game()