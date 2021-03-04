# Rock, Paper, Scissors Game
# Developer: Valeriy B.
# Language: Python 3.8.5

import random, sys

def rock_paper_scissors():
    
    # Moves dictionary with the first letter as key and move as value
    moves = {
        "r": "ROCK",
        "p": "PAPER",
        "s": "SCISSORS"
    }
    
    # Game status list with wins on the first position, losses on second and ties on third
    status = [0 , 0 , 0]

    # Player and opponent varibles
    opponent = ""
    player = ""
    
    # Game main logic
    while not 3 in status[:2]:
        
        # Randomly choosing a move
        opponent = random.choice(["r", "p", "s"])
        
        # Printing current game status
        print(f"{status[0]} Wins, {status[1]} Losses, {status[2]} Ties")
        print("Enter your move: (r)ock (p)aper (s)cissors")
        
        # Player input
        player = input().lower()

        if player == "q":
            print("Game over")
            sys.exit()
        
        # Printing player's input
        if player in moves:
            print(moves[player] + " versus...")
        else:
            print("You have to choose only between (r)ock (p)aper (s)cissors")
        
        # Printing opponents move
        print(moves[opponent])
        
        # Game result logic
        if (player == "r" and opponent == "s") or ((player == "p" and opponent == "r") or (player == "s" and opponent == "p")):
            print("You win!")
            status[0] += 1
        elif (opponent == "r" and player == "s") or ((opponent == "p" and player == "r") or (opponent == "s" and player == "p")):
            print("You lose!")
            status[1] += 1
        elif player == opponent:
            print("It's a tie!")
            status[2] += 1
        elif player == "q":
            print("Game over")
            break
        else:
            print("You have to choose only between (r)ock (p)aper (s)cissors")
        
        if status[0] == 3:
            print(f"{status[0]} WINS! CONGRATS! YOU WIN THE GAME!")
        elif status[1] == 3:
            print(f"{status[1]} LOSSES! YOU LOSE THE GAME")


rock_paper_scissors()