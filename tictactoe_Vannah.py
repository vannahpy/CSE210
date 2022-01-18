import numpy as np

"""author: Vannah Pyatt
TIC-TAC-TOE"""


def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''
    # assign/get the first player

    # create a board
    board = create_board()
    winner = "none"
    player = "x"
    round = 0

    while winner == "none":
        display_board(board)
        board= make_move(player, board)
        player = next_player(player)
        winner = is_winner(board, winner, round)
        round += 0.5
    else:
        if winner == "draw":
            print("This is a draw!")
        else:
            print(f"There is a winner! Congratulations player {winner}!!!")
        display_board(board)
        print("Thank you for playing :)")

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    board = np.array([["1","2","3"], ["4","5","6"],["7","8","9"]])
    return board

def display_board(board):
    ''' Displays the current board
        return: None
    '''
    print(board)

def is_winner(board, winner, round):
    ''' return: winner o or x, or draw if there is no winner '''
    if round == 4:
        winner = "draw"
    else:
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2]:
                winner = board[row][0]
            elif board.T[row][0] == board.T[row][1] == board.T[row][2]:
                winner = board[row][0]
            elif board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
                winner = board[1][1]
            else:
                winner = "none"
    return winner

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''
    choice = input(f"Make a move player {player}. Choose an empty position 1 through 9: ")   
    choiceindex = np.where(board==choice)
    while np.size(choiceindex) == 0:
        print("That was an invalid choice.")
        choice = input(f"Make a move player {player}. Choose an empty position 1 through 9: ")   
        choiceindex = np.where(board==choice)
    else: 
        board[choiceindex] = player

    return board

def next_player(player):
    ''' return: x if current is o, otherwise x '''
    if player == "x":
        player = "o"
    else:
        player = "x"
    return player

# run main if this has been called from the command line
if __name__ == "__main__":
    main()