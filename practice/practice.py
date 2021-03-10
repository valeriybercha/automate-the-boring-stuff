# Python practice exercises
# Course: Automate the Boring Stuff with Python
# Developer: Valeriy B.


# Intro

# Password check
def password():
    passwordFile = open('practice/secretPasswordFile.txt')
    secretPassword = passwordFile.read()
    yourPassword = input("Type the pasword: ")
    if yourPassword == secretPassword:
        print("Access granted")
        if yourPassword == "12345":
            print ("That password is not good at all")
    else:
        print("Access denied")


# Dictionaries and structuring data

# Character count
def character_count(st):
    count = {}
    
    # My method
    for c in st:
        count[c] = st.count(c)
    return count

    # Other method
    for character in st:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    print(count)

# Pretty character count
import pprint
def pretty_character_count(st):
    count = {}
    for c in st:
        count[c] = st.count(c)
    return pprint.pformat(count)

message = "It was a bright cold day in April, and the clocks were striking thirteen."

# Tic-Tac-Toe Board
def tic_tac_toe_board():
    
    # Game board dictionary
    the_board = {
        "top_l": " ", "top_m": " ", "top_r": " ",
        "mid_l": " ", "mid_m": " ", "mid_r": " ",
        "bot_l": " ", "bot_m": " ", "bot_r": " "
    }

    # Printing game board
    def game_board(board):
        print(board["top_l"] + "|" + board["top_m"] + "|" + board["top_r"])
        print("------------")
        print(board["mid_l"] + "|" + board["mid_m"] + "|" + board["mid_r"])
        print("------------")
        print(board["bot_l"] + "|" + board["bot_m"] + "|" + board["bot_r"])
        print("------------")

    game_board(the_board)

    board_space = ""
    player = ""
    count = 1
    
    # Looping for the 9 times
    while count != 10:
        
        # Stop the game if user input is 'q'
        if board_space == "q":
            break
        
        # Selecting the player 'X' or 'O'
        if count % 2 == 0:
            board_space = input("Player 'O' - Choose a space on the board: ")
            player = "O"
        else:
            board_space = input("PLayer 'X' - Choose a space on the board: ")
            player = "X"

        # Verifying if user input space is in the board dictionary
        if board_space in the_board:

            # Verifying if the board spot is not already taken
            if the_board[board_space] == " ":
                the_board[board_space] = player
                count += 1
                game_board(the_board)
            else:
                print("This space is already taken")
        else:
            print("Input space could not be found")    

tic_tac_toe_board()