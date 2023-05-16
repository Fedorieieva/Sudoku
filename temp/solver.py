import random
import copy


def valid(grid, num, position):
    # Check if the number is already in the same row or column
    for i in range(9):
        if num == grid[position[0]][i]:
            return False
    for i in range(9):
        if num == grid[i][position[1]]:
            return False
    # Check if the number is already in the same 3x3 sub-grid
    for i in range((position[0] // 3) * 3, (position[0] // 3) * 3 + 3):
        for j in range((position[1] // 3) * 3, (position[1] // 3) * 3 + 3):
            if num == grid[i][j]:
                return False
    return True     # Return True if the number can be placed at the given location


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j     # Return the location of the empty cell
    return False        # Return False if no empty cell is found


def solve(grid):
    if not find_empty(grid):
        return True     # If the grid is completely filled, return True
    else:
        position = find_empty(grid)     # Find an empty cell on the grid
        for i in range(1, 10):      # Try each number from 1 to 9 at the empty cell
            if valid(grid, i, position):        # If the number is valid at the empty cell
                grid[position[0]][position[1]] = i      # Place the number at the empty cell
                if solve(grid):     # Recursively solve the puzzle
                    return True     # If the puzzle is solved, return True
                # If the puzzle cannot be solved, backtrack by removing the number from the empty cell
                grid[position[0]][position[1]] = 0
    return False        # If the puzzle cannot be solved, return False


def generate():
    grid = [[0 for i in range(9)] for j in range(9)]   # Initialize a 9x9 grid with all zeros
    row = random.randrange(9)       # Choose a random row
    col = random.randrange(9)       # Choose a random column
    num = random.randrange(1, 10)   # Choose a random number from 1 to 9

    for i in range(25):     # Fill 25 cells with valid random numbers
        # If the chosen number is not valid or the cell is already filled, choose new random numbers
        while not valid(grid, num, (row, col)) or grid[row][col] != 0:
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1, 10)
        grid[row][col] = num    # Place the valid random number at the chosen cell

    copy_grid = copy.deepcopy(grid)     # Create a deep copy of the grid
    if not solve(copy_grid):        # If the puzzle cannot be solved generate new grid
        grid = generate()

    return grid
