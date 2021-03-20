#! python3

# Adding bullets to Wiki Markup
# Developer: Valery B.
# Language: Python 3.8.5

# Usage: 1. Copy some text to clipboard; 2. Run the application; 3. Paste the text

import pyperclip

def point_adder():
    
    # Creating a variable to temporary store the copied text
    clipboard_text = pyperclip.paste()

    # Adding bullets to every row in text
    clipboard_text_list = []
    for row in clipboard_text.split("\n"):
        clipboard_text_list.append("* " + row)

    
    # Formatting list to string and copy text to clipboard
    formatted_text = "\n".join(clipboard_text_list)
    try:
        pyperclip.copy(formatted_text)
        print("Formatted text was successfully copied to clipboard")
    except:
        print("Something went wrong...")

point_adder()
