# Comma Code Practice Project
# Chapter 4 - Lists (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

def comma_code(arr):
    
    # Formatting the types of values
    formatted_list = []
    for i in arr:
        if type(i) == int:
            formatted_list.append(str(i))
        else:
            formatted_list.append(i)
    
    # If list len is 1 we print the first element
    if len(formatted_list) == 1:
        print(formatted_list[0])

    # If list len is 2 we print first and second elementss
    elif len(formatted_list) == 2:
        print(f"{formatted_list[0]} and {formatted_list[1]}")
    
    # Logic for printing elements if list len > 2
    elif len(formatted_list) > 2:
        print(", ".join(formatted_list[:-1]) + " and " + formatted_list[-1])
    else:

        # Printing the message if list is empty
        print("Look's like you list is empty")

spam = ["bananas", "tofu", "cats"]

comma_code(spam)