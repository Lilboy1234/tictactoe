import os
import math
import sys
import random

def clear():
    os.system("clear")

clear()

board = [["[]","[]","[]"],
         ["[]","[]","[]"],
         ["[]","[]","[]"]]

print("Your X robot is O Unoccupied is []")

def move(choice):
    if 1 <= int(choice) <= 9:
        if board[math.floor((int(choice)/3)-0.01)][(int(choice)-1)%3] == "[]":
            board[math.floor((int(choice)/3)-0.01)][(int(choice)-1)%3] = "X"
            return 0
        else:
            return 1
    else:
        return 1


def turn():
    idk = []
    for i in range(3):
        idk.append("".join(board[i]))
    convertedString = "\n".join(idk)
    print(f"The board is:\n{convertedString}")
    playerChoice = input("which position would you like to move to (left to right top to bottom): ")
    outcome = move(playerChoice)
    if outcome == 1:
        while outcome == 1:
            playerChoice = input("Try Again: ")
            outcome = move(playerChoice)
    idk = []
    for i in range(3):
        idk.append("".join(board[i]))
    convertedString = "\n".join(idk)
    print(f"The board is:\n{convertedString}")
    playerWon = False
    for i in range(6):
        if i % 2 == 1:
            if board[0][i%3] == "X" and board[1][i%3] == "X" and board[2][i%3] == "X":
                playerWon = True
                break
        elif i % 2 == 0:
            if board[i%3][0] == "X" and board[i%3][1] == "X" and board[i%3][2] == "X":
                playerWon = True
                break
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        playerWon = True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        playerWon = True
    
    if playerWon == True:
        print("PLAYER HAS WON!")
        sys.exit()
    notDraw = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == "[]":
                notDraw = True
    if notDraw == False:
        print("DRAW")
        sys.exit()

    print("robot's turn now")

def aiTurn():
    #priority 1.win 2.block 3.center 4.random corner or edge
    #20% it purposefully makes a random move instead of winning
    #40% it purposefully makes a random move instead of taking center
    #20% it purposefully makes a random move instead of blocking
    boardNumbers = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
    aiWon = False
    moveMade = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                boardNumbers[i][j] = 1
            elif board[i][j] == "O":
                boardNumbers[i][j] = 2
            elif board[i][j] == "[]":
                boardNumbers[i][j] = 0
            else:
                print("bro how :sob:")
    for i in range(6):
        if i % 2 == 1:
            if (boardNumbers[0][i%3] + boardNumbers[1][i%3] + boardNumbers[2][i%3]) == 4:
                for j in range(3):
                    if boardNumbers[j][i%3] == 0 and moveMade == False:
                        randomNum = random.randint(1,5)
                        if 1 < randomNum:
                            board[j][i%3] = "O"
                            moveMade = True
                            aiWon = True
        elif i % 2 == 0:
            if (boardNumbers[i%3][0] + boardNumbers[i%3][1] + boardNumbers[i%3][2]) == 4:
                for j in range(3):
                    if boardNumbers[i%3][j] == 0 and moveMade == False:
                        randomNum = random.randint(1,5)
                        if 2 < randomNum:
                            board[i%3][j] = "O"
                            aiWon = True
                            moveMade = True
    if (boardNumbers[0][0] + boardNumbers[1][1] + boardNumbers[2][2]) == 4:
        for i in range(3):
            if boardNumbers[i][i] == 0 and moveMade == False:
                randomNum = random.randint(1,5)
                if 1 < randomNum:
                    board[i][i] = "O"
                    aiWon = True
                    moveMade = True

    elif (boardNumbers[0][2] + boardNumbers[1][1] + boardNumbers[2][0]) == 4:
        randomNum = random.randint(1,5)
        if moveMade == False and 1 < randomNum:
            if boardNumbers[0][2] == 0:
                board[0][2] = "O"
                aiWon = True
                moveMade = True
            elif boardNumbers[1][1] == 0:
                board[1][1] = "O"
                aiWon = True
                moveMade = True
            elif boardNumbers[2][0] == 0:
                board[2][0] = "O"
                aiWon = True
                moveMade = True

    for i in range(6):
        if i % 2 == 1:
            if (boardNumbers[0][i%3] + boardNumbers[1][i%3] + boardNumbers[2][i%3]) == 2 and boardNumbers[0][i%3] != 2 and boardNumbers[1][i%3] != 2 and boardNumbers[2][i%3] != 2:
                for j in range(3):
                    if boardNumbers[j][i%3] == 0 and moveMade == False:
                        randomNum = random.randint(1,5)
                        if 1 < randomNum:
                            board[j][i%3] = "O"
                            moveMade = True
        elif i % 2 == 0:
            if (boardNumbers[i%3][0] + boardNumbers[i%3][1] + boardNumbers[i%3][2]) == 2 and boardNumbers[i%3][0] != 2 and boardNumbers[i%3][1] != 2 and boardNumbers[i%3][2] != 2:
                for j in range(3):
                    if boardNumbers[i%3][j] == 0 and moveMade == False:
                        randomNum = random.randint(1,5)
                        if 1 < randomNum:
                            board[i%3][j] = "O"
                            moveMade = True
    if (boardNumbers[0][0] + boardNumbers[1][1] + boardNumbers[2][2]) == 2 and boardNumbers[0][0] != 2 and boardNumbers[1][1] != 2 and boardNumbers[2][2] != 2:
        for i in range(3):
            if boardNumbers[i][i] == 0 and moveMade == False:
                randomNum = random.randint(1,5)
                if 1 < randomNum:
                    board[i][i] = "O"
                    moveMade = True

    elif (boardNumbers[0][2] + boardNumbers[1][1] + boardNumbers[2][0]) == 2 and boardNumbers[0][2] != 2 and boardNumbers[1][1] != 2 and boardNumbers[2][0] != 2:
        randomNum = random.randint(1,5)
        if moveMade == False and 1 < randomNum:
            if boardNumbers[0][2] == 0:
                board[0][2] = "O"
                moveMade = True
            elif boardNumbers[1][1] == 0:
                board[1][1] = "O"
                moveMade = True
            elif boardNumbers[2][0] == 0:
                board[2][0] = "O"
                moveMade = True
    randomNum = random.randint(1,10)
    if boardNumbers[1][1] == 0 and moveMade == False and 4 < randomNum:
        board[1][1] = "O"
        moveMade = True
    
    avabiableMoves = []
    if moveMade == False:
        for i in range(3):
            for j in range(3):
                if board[i][j] == "[]":
                    avabiableMoves.append([i,j])
        randomNum = random.randint(0,len(avabiableMoves)-1)
        board[avabiableMoves[randomNum][0]][avabiableMoves[randomNum][1]] = "O"
        moveMade = True

    for i in range(6):
        if i % 2 == 1:
            if board[0][i%3] == "O" and board[1][i%3] == "O" and board[2][i%3] == "O":
                aiWon = True
                break
        elif i % 2 == 0:
            if board[i%3][0] == "O" and board[i%3][1] == "O" and board[i%3][2] == "O":
                aiWon = True
                break
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        aiWon = True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        aiWon = True


    if aiWon == True:
        print("AI WON")
        idk = []
        for i in range(3):
            idk.append("".join(board[i]))
        convertedString = "\n".join(idk)
        print(f"The board was:\n{convertedString}")
        sys.exit()
    




    

while True:
    turn()
    aiTurn()
