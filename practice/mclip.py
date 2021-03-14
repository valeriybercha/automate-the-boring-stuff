#! python3

# A multi-clipboard program
# Developer: Valery B.
# Language: Python 3.8.5

# Usage: Type in terminal (for Linux): python3 mclip.py agree

# Creating a dictionary with keywords as keys and messages as values
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",}

# Importing modules
# Pyperclip module should be installed: sudo pip3 install pyperclip
import sys, pyperclip

# Verifying if len of sys.argv < 2: means that nothing was typed as a keyfrase (first element is the filename)
if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyfrase] - copy phrase text")
    sys.exit()

# Keyfrase is the second element in the list
keyfrase = sys.argv[1]

# Checking if the keyfrase is in the TEXT dictionary
if keyfrase in TEXT:
    pyperclip.copy(TEXT[keyfrase])
    print(f"Text for {keyfrase} was coppied to clipboard")
else:
    print("Your input wasn't found")

# Printing message from the clipboard
resulted = pyperclip.paste()
print("Coiped text: " + resulted)