from enum import Enum
import random

class Player(Enum):
    X = 1
    O = 2
    NONE = 3

class TicTacToeBoard:
    moves = []
    currentBoard = [Player.NONE, Player.NONE, Player.NONE, Player.NONE, Player.NONE, Player.NONE, Player.NONE, Player.NONE, Player.NONE]
    winner = Player.NONE
    simulatePlayerO = False

    def __init__(self, simulatePlayerO):
        # determine which player start first
        randomInt = random.randint(0, 1)

        if (randomInt == 0):
            self.currentPlayer = Player.X
        else:
            self.currentPlayer = Player.O

        print(f'Player {self.currentPlayer.name} will make the first move!')
        
        self.simulatePlayerO = simulatePlayerO

    def printBoard(self):
        print ('--------------')
        print ('Current board:')
        for i in range(0, len(self.currentBoard)):
            if (self.currentBoard[i] == Player.NONE):
                square = str(i + 1)
            else:
                square = self.currentBoard[i].name

            if (i % 3 == 2):
                print(square)
            else:
                print(square, end='')
        
        print ('--------------\n')

    def isWinner(self, board, player):
        # The list of position winning positions
        winningCombinations = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7)
            ]
        
        # Determine if the player has taken any of possible the winning combinations
        for combination in winningCombinations:
            if (board[combination[0] - 1] == player and
                board[combination[1] - 1] == player and
                board[combination[2] - 1] == player):
                return True
            
        return False

    def recordMove(self, nextMove):
        # Make sure nextMove value is a valid position on the board
        try:
            position = int(nextMove)
        except TypeError as e:
            raise TypeError('Position must be an integer') from e

        if (position < 1 or position > len(self.currentBoard)):
            raise ValueError('Invalid position')
        
        index = position - 1
        
        # Make sure the position is not already taken
        if (self.currentBoard[index] != Player.NONE):
            raise ValueError('Position already taken')
        
        self.currentBoard[index] = self.currentPlayer
        self.moves.append((self.currentPlayer, position))

        # Determine if current player won
        if (self.isWinner(self.currentBoard, self.currentPlayer)):
            self.winner = self.currentPlayer
            return

        # Determine if all positions are filled
        if (len(self.moves) == len(self.currentBoard)):
            self.currentPlayer = Player.NONE
            return

        # Switch to next player
        if (self.currentPlayer == Player.X):
            self.currentPlayer = Player.O
        else:
            self.currentPlayer = Player.X

    def saveMovesToFile(self):
        # Save moves to file, and also print out the moves
        print('Saving moves to tictactoe.txt...')
        movesFile = open('tictactoe.txt', 'w')

        for move in self.moves:
            text = f'{move[0].name}:{move[1]}'
            movesFile.write(text + '\n')

    def simulatePlayerONextMove(self):
        print('Simulating next move by Player O...', end='')

        # Call minimax to determine the best move to make, then call recordMove using the result
        result = self.minimax(self.currentBoard, Player.O)
    
        position = result[1] + 1
        print('Player O selects position ' + str(position))
        self.recordMove(position)
    
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
            if (board[i] == Player.NONE):
                # Make a copy of current board before trying next move
                # Then make the next move as the next player, and call minimax
                boardWithNewMove = board.copy()
                boardWithNewMove[i] = player

                if (player == Player.X):
                    nextPlayer = Player.O
                else:
                    nextPlayer = Player.X

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
    
print('Welcome to TicTacToe!')

# Ask user whether this is 1 player or 2 player game
# For 1 player game, user will be Player X and Player O will be simulated by AI based algorithm
# For 2 players game, both Player X and Player O will require user input for the next move
while(True):
    # Keep looping for input until we have a valid input (1 or 2)
    try:
        numberOfPlayers = int(input('Enter number of players (1 or 2): '))

        if (numberOfPlayers < 1 or numberOfPlayers > 2):
            raise ValueError()
    except:
        print('Error: Invalid input. Enter 1 or 2')
    else:
        if (numberOfPlayers == 1):
            simulatePlayerO = True
            print('Hello Player X. You will be playing against AI-based Player O!')
        else:
            simulatePlayerO = False
            print('Hello Player X and Player O!')
        break

print('\nStarting game...')

# Create the game instance
game = TicTacToeBoard(simulatePlayerO)
game.printBoard()

# Keep looping for next move until either someone wins or no more moves can be made
while(True):
    if (game.currentPlayer == Player.NONE):
        # No more moves. The board is filled up
        print ('Game finished in a tie!')
        break
    elif (game.currentPlayer == Player.O and game.simulatePlayerO == True):
        # Simulate Player O using AI-based algorithm
        game.simulatePlayerONextMove()
        game.printBoard()
    else:
        # Ask for user input for the next move
        nextMove = input(f'Player {game.currentPlayer.name}, enter your next move: ')

        try:
            # RecordMove will update current player to the other player, so next
            # iteration will ask for move from the other player
            game.recordMove(nextMove)
        except Exception as e:
            # recordMove could raise exception if the move is invalid
            # Print error and next loop iteration will handle same user again
            print(f'Error: {e}')
        else:
            # No error from recordMove(). Print game board
            game.printBoard()

    if (game.winner != Player.NONE):
        # A game winner is recorded. Break from the loop.
        print(f'Player {game.winner.name} won!')
        break

# Save the move history to file
game.saveMovesToFile()


