# Collatz Sequence Practice Project
# Chapter 3 - Functions (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

def collatz():
    
    # Result variable
    result = 0
    print("Enter number:")
    
    # While result not equal 1 looping through the function
    while result != 1:
        
        # Using try and except for handling non integer inputs
        try:
            
            # User input variable
            number = int(input())
            
            if number % 2 == 0:
                result = number // 2
            else:
                result = 3 * number + 1
            print(result)
        except:
            print("You must enter an integer number")

collatz()