import random

playerOne = {"Health" : 20 , "Number" : 0 , "Guess" : 0} #creates playerOne information dictionary
playerTwo = {"Health" : 20 , "Number" : 0 , "Guess" : 0} #creates playerTwo information dictionary
gameTypePR = "P" #probably don't need these if I optimized more
gameOnYN = "Y"
pointType1 = False
pointType2 = False
gameOn = True

def AskP1 () : # gets Number and Guess from P1
    playerOne["Number"] = input("Player One, What is your secret number? ")
    print("Thank you")
    playerOne["Guess"] = input("PlayerOne, what is your guess? ")
    print("Thank you")

def AskP2 () : # Gets number and guess from P2
    playerTwo["Number"] = input("Player Two, what is your secret number? ")
    print("Thank you")
    playerTwo["Guess"] = input("Player Two, what is your guess? ")
    print("Thank you")

def GameRandomMode () : #game order for random mode
    AskP1()
    BotRandom()
    CHECKP1()
    CHECKP2()

def BotRandom () : # gets random numbers for guess and number for bot
    playerTwo["Number"] = random.randint(0, 10)
    playerTwo["Guess"] = random.randint(0, 10)
    print("Player Two Bot has selected numbers")

def GamePlayerMode () : # game order for PVP mode
    AskP1()
    AskP2()
    CHECKP1()
    CHECKP2()


def GameTypinator (gameTypePR) : #determines gamemode
    if gameTypePR == "P" :
        return GamePlayerMode()
    elif gameTypePR == "R":
        return GameRandomMode()

def CHECKP1 () : #Checks to see if P1 recieves or deals damage
    if playerOne["Guess"] == playerTwo["Number"] :
        pointType1 = True
    else :
        pointType1 = False
    return P1Adjustment(pointType1)

def CHECKP2 () : #Checks to see if P2 recieves or deals damage
    if playerTwo["Guess"] == playerOne["Number"] :
        pointType2 = True
    else :
        pointType2 = False
    return P2Adjustment(pointType2)


def P1Adjustment (pointType1) : #handles adjustments with P1's Health and Attack damage
    if pointType1 == True :
        playerTwo["Health"] -= 3
        print("3 damage done to Player Two")
    elif pointType1== False :
        playerOne["Health"] -= 1
        print("1 damage to Player 1")

def P2Adjustment (pointType2) : #handles adjustments with P1's Health and Attack damage
    if pointType2 == True :
        playerOne["Health"] -= 3
        print("3 damage to Player One")
    elif pointType2 == False :
        playerTwo["Health"] -= 1
        print("1 damage to Player 2")

def WhoGetsTheDub () : #determines winner or draw at the end of the game
    if playerOne["Health"] > playerTwo["Health"] :
        return print("Player One is the Winner!!! ")
    elif playerTwo["Health"] > playerOne["Health"] :
        return print("Player Two is the Winner!!!")
    elif playerOne["Health"] == playerTwo["Health"] :
        return print("It's a draw!")

print("Welcome to the greatest guessing game of all time!") #code for bare bones of the game
gameOnYN = input("Would you like to play? Y/N: ") #determines if player wants to play
while gameOnYN == "Y" :
    if gameOnYN == "N" :
        print("Thank you for playing!")
        break
    gameTypePR = input("Awesome! Would you like to play against a bot or another player? P/R : ") #asks player(s) if they want to do PVP or P v bot
    while playerOne["Health"] > 0 and playerTwo["Health"] > 0 :
        GameTypinator(gameTypePR) #sets gamemode
        print("Player One Health: " + str(playerOne["Health"]))
        print("Player Two Health: " + str(playerTwo["Health"]))
    if playerOne["Health"] <= 0 or playerTwo ["Health"] <= 0 :
        WhoGetsTheDub() #determines winner
        break