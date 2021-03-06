# Character Picture Grid Practice Project
# Chapter 4 - Lists (Automate the Boring Stuff with Python)
# Developer: Valeriy B.

def picture_grid(grid):
    
    # Creating result list
    resulted_list = []

    # Looping through grid columns
    for column in range(len(grid[0])):
        
        # Creating row string
        row_grid = ""

        # Looping through grid rows
        for row in range(len(grid)):
            row_grid += grid[row][column]
        resulted_list.append(row_grid + "\n")
    
    print("".join(resulted_list)[:-1])


grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0",],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

picture_grid(grid)