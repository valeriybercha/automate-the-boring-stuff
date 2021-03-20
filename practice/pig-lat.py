#! python3

# Pig Latin
# Developer: Valery B.
# Language: Python 3.8.5

def pig_lat():
    
    text = input("Enter the English message to translate into Pig Latin: ")
    
    vowels = ["a", "e", "i", "o", "u", "y"]
    punctuation = ".,!?:"
    ending = ["yay", "ay"]
    text_list = []

    for element in text.split():
        
        # Verifying if first letter in a word is a letter    
        if element.isalpha():
            
            # Verifying if first letter in the word is a vowel
            if element[0].lower() in vowels:
                
                # Verifying if word is lowercase or title
                if element.islower() or element.istitle():
                    text_list.append(element + ending[0])
                else:
                    text_list.append(element + ending[0].upper())
            else:
                
                # Verifying if word has a consonant cluster (br, ch, cl...)
                if element[1].lower() in vowels:
                    if element.islower():
                        text_list.append(element[1:] + element[0] + ending[1])
                    elif element.istitle():
                            text_list.append(element[1:].title() + element[0].lower() + ending[1])
                    else:
                        text_list.append(element[1:] + element[0] + ending[1].upper())
                else:
                    if element.islower():
                        text_list.append(element[2:] + element[:2] + ending[1])
                    elif element.istitle():
                            text_list.append(element[2:].title() + element[:2].lower() + ending[1])
                    else:
                        text_list.append(element[2:] + element[:2] + ending[1].upper())
        else:
            
            # Verifying if first element is a letter (means that a punctuation exists in the word)
            if element[0].isalpha():
                if element[0].lower() in vowels:
                    if element.islower() or element.istitle():
                        text_list.append(element[:-1] + ending[0] + element[-1])
                    else:
                        text_list.append(element[:-1] + ending[0].upper() + element[-1])
                else:
                    if element[1].lower() in vowels:
                        if element.islower():
                            text_list.append(element[1:-1] + element[0] + ending[1] + element[-1])
                        elif element.istitle():
                                text_list.append(element[1:-1].title() + element[0].lower() + ending[1] + element[-1])
                        else:
                            text_list.append(element[1:-1] + element[0] + ending[1].upper() + element[-1])
                    else:
                        if element.islower():
                            text_list.append(element[2:-1] + element[:2] + ending[1] + element[-1])
                        elif element.istitle():
                                text_list.append(element[2:-1].title() + element[:2].lower() + ending[1] + element[-1])
                        else:
                            text_list.append(element[2:-1] + element[:2] + ending[1].upper() + element[-1])
            else:
                text_list.append(element)
    return " ".join(text_list)

print(pig_lat())