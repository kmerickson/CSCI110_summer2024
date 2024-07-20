# name: final.py
# This program is a 2 player tic-tac-toe game.
# simply run the file and the rest should make sense enough.
# author: Keegan Erickson
# date: July 17, 2024

import os 
import sys

gridArray = [0, 1, 2, 3, 4, 5, 6, 7, 8] # holds the values of the tic-tac-toe grid
turnFlag = True # used to determine whos turn it is
player = 'X' # keeps track of whos turn it is
Xscore = 0
Oscore = 0 

# draw grid
def drawGrid():
    global gridArray
    """draws the tic-tac-toe grid out using values in gridArray, an array of length 9."""
    print()
    print(" {0} | {1} | {2} ".format(gridArray[0], gridArray[1], gridArray[2]))
    print("---+---+---")
    print(" {0} | {1} | {2} ".format(gridArray[3], gridArray[4], gridArray[5]))
    print("---+---+---")
    print(" {0} | {1} | {2} ".format(gridArray[6], gridArray[7], gridArray[8]))
    print()

# take input char and use that to adjust gridArray to place Xs and Os
def placeXOs(xo, spot):
    """take spot command and put the xo char into it"""
    global gridArray
    gridArray[spot] = xo
    #print(gridArray)

def swapTurn():
    """swap the turn flag after each turn"""
    global turnFlag
    global player
    if turnFlag:
        turnFlag = False
        player = 'O'
    else: 
        turnFlag = True
        player = 'X'

# store score by writing to a file
def saveScore():
    global Xscore
    global Oscore
    fileHandle = open("score.txt", "w")
    fileHandle.write(str(Xscore))
    a = "\n" + str(Oscore)
    fileHandle.write(a)
    fileHandle.close()

# function to read and load the score 
def readScore():
    global Xscore
    global Oscore
    if os.path.isfile("score.txt"):
        fileHandle = open("score.txt", "r")
        scores = fileHandle.readlines()
        Xscore = int(scores[0])
        Oscore = int(scores[1])
        fileHandle.close()


def spotTakenCheck(spot):
    """function to verify if piece is in already taken spot"""
    checkFlag = False
    global gridArray
    isX = gridArray[spot] == 'X'
    isO = (gridArray[spot] == 'O')
    if isX | isO:
        checkFlag = True
    else:
        checkFlag = False
    return checkFlag


# function that checks if 3 of the same pieces have been placed in a row
def gameWonCheck():
    """Takes in gridArray() and checks if a 3 in-a-row is present"""
    gameWonFlag = False
    global gridArray
    if gridArray[0] == gridArray[1] == gridArray[2]:
        gameWonFlag = True
    elif gridArray[3] == gridArray[4] == gridArray[5]:
        gameWonFlag = True
    elif gridArray[6] == gridArray[7] == gridArray[8]:
        gameWonFlag = True
    elif gridArray[0] == gridArray[3] == gridArray[6]:
        gameWonFlag = True
    elif gridArray[1] == gridArray[4] == gridArray[7]:
        gameWonFlag = True
    elif gridArray[2] == gridArray[5] == gridArray[8]:
        gameWonFlag = True
    elif gridArray[0] == gridArray[4] == gridArray[8]:
        gameWonFlag = True
    elif gridArray[6] == gridArray[4] == gridArray[2]:
        gameWonFlag = True
    return gameWonFlag

def test(did_pass):
    """ Print the results of a test. """
    linenum = sys._getframe(1).f_lineno # get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} Failed.".format(linenum))
    print(msg)

def test_suite():
    global gridArray
    gridArray = ['X', 'X', 'X', 3, 4, 5, 'O', 7, 'O']
    drawGrid()
    test(gameWonCheck() == True)

    gridArray = ['X', 2, 'X', 3, 'X', 5, 'O', 7, 'O']
    test(gameWonCheck() == False)

    
def clearScore():
    """resets the score and saves it on score.txt"""
    global Xscore
    global Oscore
    Xscore = 0
    Oscore = 0
    saveScore()

def gameMode():
    """encapsulate game functions into a game mode function"""
    inGameMode = True
    global player
    global Xscore
    global Oscore
    global gridArray

    while inGameMode:
        print("Enter b to return to lobby")
        drawGrid()
        global player
        playerInput = input("{0} player, select a spot number to place your game piece: ".format(player))
        print()
        # probably need to replace if statements with a try block 
        if playerInput == 'b':
            gridArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            inGameMode = False
            break
        else:
            #inputLoop = True
            #while inputLoop:
            try:
                spot = int(playerInput) # variable to hold the spot that was selected which is also varifying it is an int
                isInt = isinstance(spot, int) # double checking if int
                if isInt:
                    if (0 <= spot < 9):
                        if spotTakenCheck(spot):
                            print("That spot is already taken, choose another.")
                        else:
                            placeXOs(player, spot)
                            if gameWonCheck():
                                postGameState = True
                                if player == 'X':
                                    Xscore += 1
                                elif player == 'O':
                                    Oscore += 1
                                print("X score: ", Xscore)
                                print("O score: ", Oscore)
                                saveScore()
                                
                                while postGameState:
                                    print()
                                    drawGrid()
                                    gridArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                                    print("{0} play has gotten 3 in-a-row!!!".format(player))
                                    g = input("Play again? (y/n): ")
                                    print()
                                    if g == 'y':
                                        postGameState = False
                                    elif g == 'n':
                                        postGameState = False
                                        inGameMode = False 
                                    else:
                                        print("Invalid response, please enter y to play again or n to return to the lobby.")
                            swapTurn()                        
                    else:
                        print("When selecting a grid spot, use a number from 0-8")
            except: 
                print("When selecting a grid spot, use a number from 0-8")


inLobbyState = True
# while loop that continues game until a command tells to quit
while inLobbyState:
    readScore()
    print()
    print(" Welcome to a game of tic-tac-toe")
    v = input("Enter q to quit, r to restart score, v to show score, s to start: ")
    if v == 'q':
        inLobbyState = False
    elif v == 's':
        gameMode()
    elif v == 'v':
        print("Score:")
        print("X: ", Xscore)
        print("O: ", Oscore)
    elif v == 'r':
        clearScore()
        print("Score:")
        print("X: ", Xscore)
        print("O: ", Oscore)
    else:
        print()
        print("Invalid entry, try again.")
        print()


#test_suite()


    

