from os import system, name
import random


board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
valid = {0,1,2,3,4,5,6,7,8,9}
xs = []
os = []
turn = 0


def drawboard():
    # Clears the screen
    if name in ('nt', 'dos'):
        command = 'cls'
    else: command = 'clear'
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
    else: return False


def clearboard():
    for i in range(len(board)):
        board[i] = " "


def promptPlayAgain():
    global valid, xs, os
    playAgain = input("Enter yes to play again. ").lower()
    if playAgain == "yes" or playAgain == "y":
        for i in range(len(board)):
            board[i] = str(i + 1)
        valid = {0,1,2,3,4,5,6,7,8,9}
        xs = []
        os = []
        return True
    else: return False


def OsChoice():
    global valid
    
    # If it's the second turn and the center isn't taken, take the center
    if 4 in valid:
        choice = {4}
    # Prioritizes 3 Os, then block 3 Xs
    elif len(temp := winorblock(os, valid)) > 0:
        choice = temp
    elif len(temp := winorblock(xs, valid)) > 0:
        choice = temp
    # If it's the fourth turn, O is in center, and X has at least one corner, take an edge
    elif len(valid) == 6 and 4 in os and any(i in xs for i in (0, 2, 4, 6)):
        choice = valid & {1, 3, 5, 7}
    # Otherwise, take a corner if available
    elif 0 in valid or 2 in valid or 6 in valid or 8 in valid:
        choice = valid & {0, 2, 6, 8}
    else: choice = valid
    
    return random.choice(list(choice))


def winorblock(positions, valid):
    best = set()
    
    # Checking for two of the same player in a row
    for i in positions:
        for j in positions:
            if (i,j) in ((1,2), (3,6), (4,8)): best.add(0)
            if (i,j) in ((0,2), (4,7)): best.add(1)
            if (i,j) in ((0,1), (4,6), (5,8)): best.add(2)
            if (i,j) in ((0,6), (4,5)): best.add(3)
            if (i,j) in ((0,8), (1,7), (2,6), (3,5)): best.add(4)
            if (i,j) in ((3,4), (2,8)): best.add(5)
            if (i,j) in ((0,3), (2,4), (7,8)): best.add(6)
            if (i,j) in ((1,4), (6,8)): best.add(7)
            if (i,j) in ((0,4), (2,5), (6,7)): best.add(8)
    
    # Uses the intersection of the best and valid sets
    return best & valid


def welcomePlayer():
    drawboard()
    clearboard()
    
    print(
        "Welcome to tic-tac-toe! You'll be using the numbers above to indicate where you want to play.\n(looks like your numpad)"
    )
    input("Press Enter to continue")


def promptCorrectEntry(choice):
    drawboard()
    print(f"{choice} is not a valid input. Enter a number from 1 to 9 to select a square.")
    input("Press Enter to continue.")


def getPlayerChoice():
    while True:
        drawboard()
        print("It is X's turn. Please choose a square.")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            promptCorrectEntry(choice)
            continue

        if choice < 1 or choice > 9:
            promptCorrectEntry(choice)
            continue

        if board[choice - 1] != " ":
            drawboard()
            print(
                f"You're not allowed to choose a square that has already been chosen."
            )
            input("Press Enter to continue.")
            continue
    
        return choice - 1


def updateBoard(player, choice):
    global turn
    board[choice] = player
    xs.append(choice) if player == "X" else os.append(choice)
    valid.remove(choice)
    turn += 1


def game():

    welcomePlayer()
    
    while True: 
        choice = getPlayerChoice()
        updateBoard("X", choice)

        if turn >= 5 and checkwinner("X"):
            break        
        elif turn == 9:
            drawboard()
            print("It's a draw!")
            break

        choice = OsChoice()
        updateBoard("O", choice)
        
        if turn >= 5 and checkwinner("O"):
            break
        

if __name__ == "__main__":
    game()
    while promptPlayAgain():
        game()