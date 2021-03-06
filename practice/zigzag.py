# Zigzag: Short program
# Course: Automate the Boring Stuff with Python
# Developer: Valeriy B.

import time

def zigzag():
    
    # Counting variable
    count = 1

    # Infinite loop
    while True:

        # Checking for odd and even cases
        indent_odd = 4
        indent_even = 1

        if count % 2 == 0:        
            for i in range(4):
                print(indent_even * " " + "*" * 8)
                indent_even += 1
                time.sleep(0.1)
        else:
            for i in range(5):
                print(indent_odd * " " + "*" * 8)
                indent_odd -= 1
                time.sleep(0.1)
        count += 1

zigzag()