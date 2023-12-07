import random

#CS506_FL23_Tic Tac Toe project_TP submission: Chloe Lee, Taeko Owaki
class TicTacToeBoard:
    def __init__(self):
        self.file =open('tictactoe.txt', 'a')

        print("\nWelcome to Tic Tac Toe! Have fun!\n")
        self.file.writelines("Begin\n")

        self.board = [ "-","-","-","-","-",
                "-","-","-","-","-",
                "-","-","-","-","-",
                "-","-","-","-","-",
                "-","-","-","-","-"]
        
        self.winner = None
        self.simulatePlayerO = False

        # Ask user whether this is 1 player or 2 player game
        # For 1 player game, user will be Player X and Player O will be simulated by AI based algorithm
        # For 2 players game, both Player X and Player O will require user input for the next move
        while(True):
            # Keep looping for input until we have a valid input (1 or 2)
            try:
                numberOfPlayers = int(input("Enter number of players (1 or 2): "))

                if (numberOfPlayers < 1 or numberOfPlayers > 2):
                    raise ValueError()
            except:
                print('Error: Invalid input. Enter 1 or 2')
            else:
                if (numberOfPlayers == 1):
                    self.simulatePlayerO = True
                    print("Hello Player X. You will be playing against AI-based Player O!")
                else:
                    self.simulatePlayerO = False
                    print("Hello Player X and Player O!")
                break

        if self.simulatePlayerO:
            self.file.writelines("PlayerO simulated by AI.\n") #to record
        else:
            self.file.writelines("Two player game.\n") #to record

        # determine which player start first
        randomInt = random.randint(0, 1)

        if (randomInt == 0):
            self.currentPlayer = "X"
        else:
            self.currentPlayer = "O"

        print(f"Player {self.currentPlayer} will make the first move!")
        self.file.writelines(f"Player {self.currentPlayer} starts first.\n") #to records

    #print the game board
    #each elements are indexed by numbers (1-9) to get user inputs
    def printBoard(self):
        print(" | " + self.board[0]+ " | " + self.board[1] + " | " + self.board[2] +" | " + self.board[3] + " | " + self.board[4] +" | " + "\t    1  2  3  4  5 ") 
        print("-----------------------")
        print(" | " + self.board[5]+ " | " + self.board[6] + " | " + self.board[7] +" | " + self.board[8] + " | " + self.board[9] +" | " + "\t    6  7  8  9  10 ")  
        print("-----------------------")
        print(" | " + self.board[10]+ " | " + self.board[11] + " | " + self.board[12] +" | " + self.board[13] + " | " + self.board[14] +" | "+  "\t    11 12 13 14 15 ") 
        print("-----------------------")
        print(" | " + self.board[15]+ " | " + self.board[16] + " | " + self.board[17] +" | " + self.board[18] + " | " + self.board[19] +" | " + "\t    16 17 18 19 20")  
        print("-----------------------")
        print(" | " + self.board[20]+ " | " + self.board[21] + " | " + self.board[22] +" | " + self.board[23] + " | " + self.board[24] +" | "+  "\t    21 22 23 24 25 ")

    #player input by input()
    def playerInput(self, inp):
        #try....except statement is raised not to take string inputs
        try:
            inp = int(inp) #convert input to integer
        except ValueError:
            #user will get a message when they enter a string
            print("Please enter a valid integer")
            self.file.writelines("ValueError raised\n") #to record
            return False

        #ranged input value between 1-25 to process 
        #blank value ("-") will be changed by each turn current player: X, O
        if inp >= 1 and inp <= 25 and self.board[inp-1] == "-":
            self.board[inp-1] = self.currentPlayer
            print(f"The {self.currentPlayer}'s move is {inp}") 
            #to record moves per user inputs to titactoe.txt file
            self.file.writelines(f"The {self.currentPlayer}'s move is {inp}\n")
            return True
        
        else:
            print("Not valid! Try again!") 
            #display error message,
            #will not provide extra input to cover. Next turn!
            self.file.writelines("Not valid number.\n") #to record
            return False
            
    #check for win or tie
    #check winners by horizontal, vertical, diagonal w/checkWinner()
    def checkWinner(self):
        if self.isWinner(self.board, self.currentPlayer):
            self.winner = self.currentPlayer
            print(f"The winner is {self.winner}.") 
            self.file.writelines(f"The winner is {self.winner}.\n") #to record
            return True
            
        return False

    #check to see if there is a tie w/no winner , but all values are changed
    def checkTie(self):
        if "-" not in self.board: 
            self.winner = None #this means game is finished, but no winner yet
            print("It is a tie.")
            self.file.writelines("It is a tie.\n") #to record
            return True 
        #return True will go into the loop, but will break per if statement
       
    #switchplayers() can switch players for currently playing per X, O values
    def switchPlayer(self):
        #global statement let you this local change can be reflected in global level
        if self.currentPlayer == "X": #If the value per currentplayer changes to X,
            self.currentPlayer = "O"  #then, can be assigned as "O"player
        else:
            self.currentPlayer = "X"  #a player will be re-assinged as "X"

    def recordQuit(self):
        print("Exit.")
        self.file.writelines("Exit\n") #to record

    def closeSession(self):
        print("Thanks for Playing.")
        self.file.writelines("Thanks for Playing. Game session over.\n") #to record
        self.file.close()

    # Determine if the player has won
    def isWinner(self, boardToCheck, playerToCheck):
        # Board index
        # 0  1  2  3  4  
        # 5  6  7  8  9 
        # 10 11 12 13 14
        # 15 16 17 18 19
        # 20 21 22 23 24
        winningCombinations = [
            # horizontal
            (0, 1, 2), (1, 2, 3), (2, 3, 4),            # 1st row
            (5, 6, 7), (6, 7, 8), (7, 8, 9),            # 2nd row
            (10, 11, 12), (11, 12, 13), (12, 13, 14),   # 3rd row
            (15, 16, 17), (16, 17, 18), (17, 18, 19),   # 4th row
            (20, 21, 22), (21, 22, 23), (22, 23, 24),   # 5th row

            # vertical
            (0, 5, 10), (5, 10, 15), (10, 15, 20),      # 1st column
            (1, 6, 11), (6, 11, 16), (11, 16, 21),      # 2nd column
            (2, 7, 12), (7, 12, 17), (12, 17, 22),      # 3rd column
            (3, 8, 13), (8, 13, 18), (13, 18, 23),      # 4th column
            (4, 9, 14), (9, 14, 19), (14, 19, 24),      # 5th column

            # diagonal - top left to bottom right
            (2, 8, 14), (1, 7, 13), (7, 13, 19),
            (0, 6, 12), (6, 12, 18), (12, 18, 24),
            (5, 11, 17), (11, 17, 23), (10, 16, 22),

            # diagonal - top right to bottom left
            (2, 6, 10), (3, 7, 11), (7, 11, 15),
            (4, 8, 12), (8, 12, 16), (12, 16, 20),
            (9, 13, 17), (13, 17, 21), (14, 18, 22)
        ]

        # Determine if the player has taken any of possible the winning combinations
        for combination in winningCombinations:
            if boardToCheck[combination[0]] == boardToCheck[combination[1]] == boardToCheck[combination[2]] == playerToCheck:
                return True
            
        return False
    
    def simulatePlayerONextMove(self):
        print('Simulating next move by Player O...', end='')

        # Call minimax to determine the best move to make, then call recordMove using the result
        result = self.minimax(self.board, "O")
    
        position = result[1] + 1
        print('Player O selects position ' + str(position))
        return str(position)
    
    # Based on reference:
    # Surma, G. (2021, October 13). Tic Tac Toe - Creating Unbeatable AI - Greg Surma - Medium. Medium. https://gsurma.medium.com/tic-tac-toe-creating-unbeatable-ai-with-minimax-algorithm-8af9e52c1e7d
    def minimax(self, board, player):
        # If player won, return Score 1 and Move -1 (No move)
        if (self.isWinner(board, player)):
            return (1, -1)
        
        moveIndex = -1
        score = -2

        # Try all board position that is not taken
        for i in range(len(board)) :
            if (board[i] == "-"):
                # Make a copy of current board before trying next move
                # Then make the next move as the next player, and call minimax
                boardWithNewMove = board.copy()
                boardWithNewMove[i] = player

                if (player == "X"):
                    nextPlayer = "O"
                else:
                    nextPlayer = "X"

                scoreForTheMove = -self.minimax(boardWithNewMove, nextPlayer)[0]

                # If score returned is larger than other position tried so far,
                # Keep the score and the move
                if (scoreForTheMove > score):
                    score = scoreForTheMove
                    moveIndex = i

        if (moveIndex == -1):
            # Return score 0 because there is no good move
            return (0, moveIndex)
        
        # Return the score and move index with highest score returned among the non taken positions
        return (score, moveIndex)


#main game loop
game = TicTacToeBoard()

while True:
    game.printBoard() #to display

    if (game.simulatePlayerO == True and game.currentPlayer == "O"):
        inp = game.simulatePlayerONextMove()
    else:
        #to take inputs: should have which player's turn in user input statement
        inp = input(f"\n**Player {game.currentPlayer} ** Enter a number 1-25 or enter 'q' to quit: ")
        
        if inp.lower() == 'q': #if user selects 'q' then exit while loop
            game.recordQuit()
            break
   
    # playerInput returns False if input is invalid. Don't switch player in that case.
    if game.playerInput(inp):
        if game.checkWinner():
            game.printBoard() #just to display again to wrap up the game
            break
        elif game.checkTie():
            game.printBoard() #just to display again to wrap up 
            break

        game.switchPlayer()
        
game.closeSession()
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
