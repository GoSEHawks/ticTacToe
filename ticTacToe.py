import os
import time
board = [" " for i in range(9)]

def printBoard():
    print('Count avalible Spaces left -> right from the top.')
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(' _ _ _')
    print(row1) 
    print(' _ _ _')
    print(row2)
    print(' _ _ _')
    print(row3)
    print()


def playerMove(icon):
    print('Player {}'.format(icon)," turn.")
    try:
        choice = int(input("Enter your move (1-9): ").strip())
        if choice < 10 :
            if board[choice - 1] == " ":
                board[choice - 1] = icon
            else:
                print('SPACE UNAVALIBLE!')
                time.sleep(2)  
        else:
            print('Input must be a # between 1-8')
            time.sleep(2)        
    except:
        print('Invalid Input, must be a NUMBER')
        time.sleep(2)
    os.system('cls')



def isVictory(icon):
    if  (board[0] == icon and board [1] == icon and board[2] == icon) or\
        (board[3] == icon and board [4] == icon and board[5] == icon) or\
        (board[6] == icon and board [7] == icon and board[8] == icon) or\
        (board[0] == icon and board [3] == icon and board[6] == icon) or\
        (board[1] == icon and board [4] == icon and board[7] == icon) or\
        (board[2] == icon and board [5] == icon and board[8] == icon) or\
        (board[0] == icon and board [4] == icon and board[8] == icon) or\
        (board[2] == icon and board [4] == icon and board[6] == icon):
        return True
    else:
        return False
def isDraw():
    if " " not in board:
        return True
    else:
        return False
# start
while True:
    printBoard()
    playerMove('X')
    if isVictory('X'):
        print('X wins!')
        break
    elif isDraw():
        print('Its a Draw!')
        break
    printBoard()
    playerMove('O')
    if isVictory('O'):
        printBoard()
        print('O wins!')
        break
    elif isDraw():
        print('Its a Draw!')
        break

