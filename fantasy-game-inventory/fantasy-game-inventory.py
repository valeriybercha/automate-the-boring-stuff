# Fantasy Game Inventory Practice Project
# Chapter 5 - Dictionary and Structuing Data (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

# Fantasy Game Inventory
def display_inventory(inventory):

    # Creating blank inventory list    
    display_stuff = list()
    display_stuff.append("Inventory:")
    
    # Creating items variable
    items = 0

    # Looping through stuff dictionary
    for k, v in inventory.items():
        display_stuff.append(f"{v} {k}")
        items += v
    
    # Formatting inventory accordingly
    display_stuff.append(f"Total numbner of items: {items}")
    return "\n".join(display_stuff)

# List to Dictionary function for Fantasy Game Inventory
def add_to_inventory(invent, added_items):
    
    # Blank dictionary
    result = dict()

    # Checking whether an element from the dragon_loot list is in the inv dictionary
    for element in added_items:
        if element in invent.keys():
            result[element] = invent[element] + added_items.count(element)
        else:
            result[element] = added_items.count(element)
    
    # Checking if an element from the inv dictionary is not in resulted dictionary
    for element in invent.keys():
        if element not in result.keys():
            result[element] = invent[element]
    return result

inv = {"gold coin": 42, "rope": 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = add_to_inventory(inv, dragon_loot)

print(display_inventory(inv))