# Modeling a chess game board

import pprint

def chess_board_modeling():
    
    # White player board
    board_white = {
        "wrook_one": "a8",
        "wknight_one": "b8", 
        "wbishop_one": "c8",
        "wqueen": "d8",
        "wking": "e8",
        "wbishop_two": "f8",
        "wknight_2": "g8",
        "wrook_two": "h8",
        "pawn_one": "a7",
        "pawn_two": "b7",
        "pawn_three": "c7",
        "pawn_four": "d7",
        "pawn_five": "e7",
        "pawn_six": "f7",
        "pawn_seven": "g7",
        "pawn_eight": "h7"
    }

    # Black player board
    board_black = {
        "brook_one": "a1",
        "bknight_one": "b1",
        "bbishop_one": "c1",
        "bqueen": "d1",
        "bking": "e1",
        "bbishop_two": "f1",
        "bknight_2": "g1",
        "brook_two": "h1",
        "pawn_one": "a2",
        "pawn_two": "b2",
        "pawn_three": "c2",
        "pawn_four": "d2",
        "pawn_five": "e2",
        "pawn_six": "f2",
        "pawn_seven": "g2",
        "pawn_eight": "h2"
    }

    game_count = 1
    player = ""
    
    # Chess board modeled by the dictionary
    players_moves = dict()

    while True:
        
        # Stop the game if player type's 'q'
        if player == "q":
            break
        
        # Game logic for Black player
        if game_count % 2 == 0:
            player = input("Black: Enter a piece and move position on the board: ")
            piece_and_move = player.split()
            if piece_and_move[0] in board_black:
                board_black.pop(piece_and_move[0])
                board_black[piece_and_move[0]] = piece_and_move[1]
                players_moves[piece_and_move[0]] = piece_and_move[1]
                game_count += 1
            else:
                if player == "moves":
                    print(players_moves)
                elif player == "show":
                    print(board_black)
                else:
                    print("This position is not found")
            
        
        # Game logic for White player
        else:
            player = input("White: Enter a piece and move position on the board: ")
            piece_and_move = player.split()
            if piece_and_move[0] in board_white:
                board_white.pop(piece_and_move[0])
                board_white[piece_and_move[0]] = piece_and_move[1]
                players_moves[piece_and_move[0]] = piece_and_move[1]
                game_count += 1
            else:
                if player == "moves":
                    print(players_moves)
                elif player == "show":
                    print(board_white)
                else:
                    print("This position is not found")
            
chess_board_modeling()