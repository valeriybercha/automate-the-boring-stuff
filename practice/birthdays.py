# Friends birthdays
# Python practice exercises
# Course: Automate the Boring Stuff with Python
# Developer: Valeriy B.

def friends_birthdays():
    
    # Creating a birtday dictionary
    birthday = {"John": "Dec 12", "Alice": "Sep 3", "Steve": "Jan 22", "Harry": "Aug 2", "Bob": "Oct 15"}

    while True:
        name = input("Enter a name: ").capitalize()

        # Stop the program if input remains blank
        if name == "":
            break
        
        # Verifying if name is in dictionary
        if name in birthday:
            print(f"{name} birthday is on {birthday[name]}")
        else:
            print(f"{name} is not on the list. Would you like to add your friend's birthday to the list?")
            
            # Asking user if he wants to add a new friend birthday to the list
            question = input("(y)es or (n)o: ")
            if question.lower() == "y":
                bday = input(f"Type {name} birtday date: ").capitalize()
                birthday[name] = bday
                print(f"{name} was added to the list")
            else:
                print("Ok. Let's try again")

friends_birthdays()
