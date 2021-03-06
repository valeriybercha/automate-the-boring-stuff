# Coin Flip Streaks Practice Project
# Chapter 4 - Lists (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

import random

# Importimg itertools module
from itertools import groupby

def coin_flip_streaks():

    # Coin (h)eads and (t)ails
    coin = ["h", "t"]

    coin_flip_list = []
    number_of_streaks = 0

    for i in range(10000):
        coin_flip_list.append(random.choice(coin))
    
    # Grouping elements by counting consecutive streaks with itertool.groupby module
    grouped_coin_list = [(k, sum(1 for i in g)) for k,g in groupby(coin_flip_list)]

    # Looking for 6 consecutive streaks in the list
    for i in grouped_coin_list:
        if 6 in i:
            number_of_streaks += 1
    
    print("Chance of streak: %s%%" % (number_of_streaks/ 100))

coin_flip_streaks()