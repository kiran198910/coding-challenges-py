# Write a program for 2 player TIC TAC TOE GAME


def display_game_board(board):
    print("Current board values :: ")
    print(f"{board[1:]}")

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


def win_check(board, marker):
    pass

if __name__ == "__main__":
    print("Welcome to the Game!")
    default_game_board = ["#", " ", " ", " ", " ", " ", " "," "," "," "]
    # Display existing game Board
    display_game_board(default_game_board)

    player2 = ""
    count = 10

    marker = player_input()
    print(f"Player 1 slected {marker}")

    while True:
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
        place_marker(default_game_board, marker, position_player1)
        position_player2 = int(input("Enter position for the position (1-9) :: "))
        place_marker(default_game_board, player2, position_player2)
    
    # win check


    
