# Table Printer Practice Project
# Chapter 6 - Manipulating strings (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

def printTable(table):
    
    # Finding the maximum length of item on every row
    max_item_on_row = []
    for row in table:
        current_row = []
        for item in row:
            current_row.append(len(item))
        max_item_on_row.append(max(current_row))

    # Creating a new list with formatted rows
    resulted_list = []
    for items in range(len(table[0])):
        new_row = []
        for elem in range(len(table)):
            new_row.append(table[elem][items].rjust(max_item_on_row[elem]))
        resulted_list.append(new_row)

    # Printing the resulted list of items
    for row in resulted_list:
        print(" ".join(row))

tableData = [["apples", "oragnes", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

printTable(tableData)