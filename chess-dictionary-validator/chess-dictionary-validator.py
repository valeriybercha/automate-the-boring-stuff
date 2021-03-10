# Chess Dictionary Validator Practice Project
# Chapter 5 - Dictionary and Structuing Data (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

def chess_dictionary_validator(inp):
    
    # Creating a blank chess dictionary
    chess_dictionary = dict()

    # Creating a chess board
    chess_board = list()
    for number in range(1, 9):
        for character in range(97, 105):
            chess_board.append(chr(character) + str(number))
    
    # Adding chess board to chess dictionary
    chess_dictionary["chess_board"] = chess_board

    # Chess pieces
    chess_pieces = ["king", "queen", "rook", "bishop", "knight", "pawn"]
    
    # Blank lists for 'white' and 'black' pieces
    black_white_pieces = list()

    for element in range(2):
        if element == 0:

            # Adding 'white' pieces to the list
            for item in chess_pieces:
                if item == "king" or item == "queen":
                    black_white_pieces.append("w" + item)
                elif item == "rook" or item == "bishop" or item == "knight":
                    for loop in range(1, 3):
                        black_white_pieces.append("w" + item + str(loop))
                elif item == "pawn":
                    for loop in range(1, 9):
                        black_white_pieces.append("w" + item + str(loop))
        else:

            # Adding 'black' pieces to the list
            for item in chess_pieces:
                if item == "king" or item == "queen":
                    black_white_pieces.append("b" + item)
                elif item == "rook" or item == "bishop" or item == "knight":
                    for loop in range(1, 3):
                        black_white_pieces.append("b" + item + str(loop))
                elif item == "pawn":
                    for loop in range(1, 9):
                        black_white_pieces.append("b" + item + str(loop))

    # Adding pieces to dictionary
    chess_dictionary["black_white_pieces"] = black_white_pieces

    # Creating 2 variables for 'piece' and 'position' validation
    piece_validation = inp.split()[0]
    position_validation = inp.split()[1]

    # Verifying if 'piece' and 'position' variables are in the dictionary
    if piece_validation in chess_dictionary["black_white_pieces"]:
        if position_validation in chess_dictionary["chess_board"]:
            print(True)
        else:
            print(False)
    else:
        print(False)

validator = input("Enter a piece and piece position on the board (e.g. 'wking c6'): ")

chess_dictionary_validator(validator)