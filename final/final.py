#final


gridArray = [0, 1, 2, 3, 4, 5, 6, 7, 8]
turnFlag = True # used to determine whos turn it is
player = 'X'

# draw grid
def drawGrid():
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
    gridArray[spot] = xo
    #print(gridArray)

 # swap the turn flag after each turn
def swapTurn():
    global turnFlag
    global player
    if turnFlag:
        turnFlag = False
        player = 'O'
    else: 
        turnFlag = True
        player = 'X'

# store score by writing to a file

# function to verify if piece is in spot chosen    
def spotTakenCheck(spot):
    print("in spotTakenCheck()")
    checkFlag = False
    if gridArray(spot) == 'X' | gridArray(spot) == 'O':
        checkFlag = True
        print("in if gridArray(spot) == 'X' | gridArray(spot) == 'O':")
        print("checkFlag(spot) = ", checkFlag)
    else:
        checkFlag = False
        print("in the else:")
        print("checkFlag(spot) = ", checkFlag)

    return checkFlag


# function that checks if 3 of the same pieces have been placed in a row
def gameWonCheck():
    """Takes in gridArray() and checks if a 3 in-a-row is present"""
    gameWonFlag = False
    if gridArray[0] == gridArray[1] == gridArray[2]:
        gameWonFlag = True
    elif gridArray[3] == gridArray[4] == gridArray[5]:
        gameWonFlag = True
    elif gridArray[6] == gridArray[7] == gridArray[8]:
        gameWonFlag = True
    elif gridArray[0] == gridArray[3] == gridArray[6]:
        gameWonFlag = True
    elif gridArray[0] == gridArray[4] == gridArray[7]:
        gameWonFlag = True
    elif gridArray[0] == gridArray[5] == gridArray[8]:
        gameWonFlag = True
    elif gridArray[0] == gridArray[4] == gridArray[8]:
        gameWonFlag = True
    elif gridArray[6] == gridArray[4] == gridArray[2]:
        gameWonFlag = True
    return gameWonFlag

# encapsulate game functions into a game mode function
def gameMode():
    inGameMode = True
    
    while inGameMode:
        print("Enter b to return to lobby")
        drawGrid()
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
                print("in try block")
                spot = int(playerInput) # variable to hold the spot that was selected which is also varifying it is an int
                isInt = isinstance(spot, int) # double checking if int
                #if (gridArray[spot] == 'X') | (gridArray[spot] == 'O'):
                #    print("That spot has already been taken, try another.")
                if isInt:
                    if (0 <= spot < 9):
                        placeXOs(player, spot)
                        if gameWonCheck():
                            postGameState = True
                            # need to put a function in here that records who won to a txt file
                            while postGameState:
                                print()
                                drawGrid()
                                print("{0} play has gotten 3 in-a-row!!!".format(player))
                                g = input("Play again? (y/n)")
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
                print("in except block")
                print("When selecting a grid spot, use a number from 0-8")
        
        #check if game has been won
        

       


flag = True
# while loop that continues game until a command tells to quit
while flag:
    print(" Welcome to a game of tic-tac-toe")
    v = input("Enter q to quit, r to restart score, s to start: ")
    if v == 'q':
        flag = False
    elif v == 's':
        gameMode()




    

