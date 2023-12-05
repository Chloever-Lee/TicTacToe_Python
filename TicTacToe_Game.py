#CS506_FL23_Tic Tac Toe project_IP submission: Chloe Lee

file =open('tictactoe.txt', 'a')

#global variable1: board
#this will format the output w/printBoard()
board = [ "-","-","-",
         "-","-","-",
         "-","-","-"]
#Other global variables: current player, winner, gamerunning
#these will be applied toward functions below.
currentPlayer = 'X'
winner = None
gameRunning =True

#print the game board
#each elements are indexed by numbers (1-9) to get user inputs
def printBoard(board):
    print(" | "+ board[0]+ " | " +board[1] + " | " + board[2] +" | " + "\t    1  2  3 ") 
    print("--------------")
    print(" | "+ board[3]+ " | " +board[4] + " | " + board[5] +" | " + "\t    4  5  6 ")  
    print("--------------")
    print(" | "+ board[6]+ " | " +board[7] + " | " + board[8] +" | "+  "\t    7  8  9 ")

#player input by input()
def playerInput(board):
    #ranged input value between 1-9 to process 
    #blank value ("-") will be changed by each turn current player: X, O
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] =currentPlayer
        print(f"The {currentPlayer}'s move is {inp}") 
        #to record moves per user inputs to titactoe.txt file
        file.writelines(f"The {currentPlayer}'s move is {inp}\n")
    
    else:
        print("Not valid! Sorry,next turn!") 
        #display error message,
        #will not provide extra input to cover. Next turn!
        file.writelines("Not valid number.\n") #to record
    return
            
#check for win or tie
#check winners by horizontal, vertical, diagonal w/checkWinner()
def checkWinner(board):
    global winner
    if board[0] == board[1] ==board[2] !='-': #horizontal
        winner = board[0]
        return True
    elif board[3] == board[4] ==board[5] !='-': #horizontal
        winner = board[3]
        return True
    elif board[6] == board[7] ==board[8] !='-':  #horizontal
        winner = board[6]
        return True
    elif board[0] == board[3] ==board[6] !='-': #vertical
        winner = board[0]
        return True 
    elif board[1] == board[4] ==board[7] != '-':  #vertical
        winner = board[1]
        return True
    elif board[2] == board[5] ==board[8] !='-': #vertical
        winner = board[2]
        return True
    elif board[0] == board[4] ==board[8] !='-':  #diagonal
        winner = board[0]
        return True
    elif board[2] == board[4] ==board[6] !='-':  #diagonal
        winner = board[2]
        return True
#check to see if there is a tie w/no winner , but all values are changed
def checkTie(board):
    if "-" not in board: 
        winner = None #this means game is finished, but no winner yet
        return True 
    #return True will go into the loop, but will break per if statement
       
#switchplayers() can switch players for currently playing per X, O values
def switchPlayer():
    global currentPlayer 
    #global statement let you this local change can be reflected in global level
    if currentPlayer == "X": #If the value per currentplayer changes to X,
        currentPlayer = "O"  #then, can be assigned as "O"player
    else:
        currentPlayer = "X"  #a player will be re-assinged as "X"

#main game loop
print("\nWelcome to Tic Tac Toe! Have fun!\n")
file.writelines("Begin\n")
while gameRunning:
    printBoard(board) #to display
    #to take inputs: should have which player's turn in user input statement
    inp = input(f"\n**Player {currentPlayer} ** Enter a number 1-9 or enter 'q' to quit: ")
    
    if inp.lower() == 'q': #if user selects 'q' then exit while loop
        False
        print("Exit.")
        file.writelines("Exit\n") #to record
        break
    #try....except statement is raised not to take string inputs
    try:
        inp = int(inp) #convert input to integer
        playerInput(board) 
        switchPlayer()
        if checkWinner(board):
            print(f"The winner is {winner}.") 
            #f string can tell who is the winner w/ checkWinner()
            file.writelines(f"The winner is {winner}.\n") #to record
            printBoard(board) #just to display again to wrap up the game
            break
        elif checkTie(board):
            print("It is a tie.")
            file.writelines("It is a tie.\n") #to record
            printBoard(board) #just to display again to wrap up 
            break
    except ValueError:
        print("Please enter a valid integer") 
        #user will get a message when they enter a string
        file.writelines("ValueError raised\n") #to record
        
print("Thanks for Playing.")
file.writelines("Thanks for Playing. Game session over.\n") #to record
file.close()
#reference
""" 
Code Coach. (2021, March 6). Python TIC TAC TOE Tutorial | 
    Beginner friendly Tutorial [Video].YouTube.https://www.youtube.com/watch?v=dK6gJw4-NCo

***********************************************************************
*    Title: Python Tic Tac Toe Tutorial | Beginner friendly Tutorial
*    Author: Code Coach
*    Date: March 6, 2021
*    Code version: Python 3.8.5
*    Availability: https://www.youtube.com/watch?v=dK6gJw4-NCo
*
************************************************************************
"""
