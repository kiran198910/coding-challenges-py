# Write a program for 2 player TIC TAC TOE GAME
"""
A simple 2-player Tic Tac Toe game implementation for the command line.
Functions:
    display_game_board(board):
        Displays the current state of the game board.
    player_input():
        Prompts Player 1 to choose their marker ('X' or 'O').
    place_marker(board, marker, position):
        Places the given marker ('X' or 'O') at the specified position on the board and displays the updated board.
    full_board_check(board, count):
        Checks if there are any remaining empty positions on the board and returns the updated count.
    win_check(board, marker):
        Placeholder for function to check if the given marker has a winning combination on the board.
Main Execution:
    - Initializes the game board.
    - Prompts Player 1 to select their marker.
    - Assigns the other marker to Player 2.
    - Alternates turns between players, allowing them to place their markers.
    - Continues until the board is full.
    - (Win checking functionality to be implemented.)
"""


def display_game_board(board):
    print("Current board values :: ")
    # print(f"{board[1:]}")
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")

def player_input():
    player_input = input("Player 1 enter your choide preference from X or O : ")
    return player_input

def place_marker(board, marker, position):
    print(board, marker, position)
    board[position] = marker
    display_game_board(board)

def full_board_check(board, count):
    for item in board:
        if item.strip():
            count -= 1
    print(f"Remaining position at board {count}")
    return count


def win_check(board: list, marker: str):
    player_win_check = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for p1,p2,p3 in player_win_check:
        if board[p1] == board[p2] == board[p3] == marker:
           return True
    else:
        return False

if __name__ == "__main__":
    print("Welcome to the Game!")
    default_game_board = ["#", " ", " ", " ", " ", " ", " "," "," "," "]
    # Display existing game Board
    display_game_board(default_game_board)

    player2 = ""
    count = 10

    while True:
        marker = player_input()
        print(f"Player 1 slected {marker}")
        # Ask user to select there sign X or O - Player Input
        if marker not in ["X", "O"]:
            print("Not a valid input please select symbol X or O")
            continue
        break
    # As per player one choice assign other value to the player 2
    if marker == "X":
        player2 = "O"
    else:
        player2 = "X"

    while full_board_check(default_game_board, count):
        # Check for board position availibility 
        # # Choose position
        position_player1 = int(input("Enter position for the position (1-9) :: "))
        if not position_player1 in range(1,10):
            continue
        place_marker(default_game_board, marker, position_player1)
        if win_check(default_game_board, marker):
            print(f"Congragulation!! Player1 own the game!")
            break

        position_player2 = int(input("Enter position for the position (1-9) :: "))
        if position_player2 not in range(1,10):
            continue
        place_marker(default_game_board, player2, position_player2)
        if win_check(default_game_board, marker):
            print(f"Congragulation!! Player2 own the game!")
            break

        





    
