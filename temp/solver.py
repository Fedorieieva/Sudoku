import random
import copy


# class Solver:
#     def __init__(self):
#         self._board = [[0 for i in range(9)] for j in range(9)]   # Initialize a 9x9 grid with all zeros
#
#     @staticmethod
#     def valid(board, num, position):
#         # Check if the number is already in the same row or column
#         for i in range(9):
#             if num == board[position[0]][i]:
#                 return False
#         for i in range(9):
#             if num == board[i][position[1]]:
#                 return False
#         # Check if the number is already in the same 3x3 sub-grid
#         for i in range((position[0] // 3) * 3, (position[0] // 3) * 3 + 3):
#             for j in range((position[1] // 3) * 3, (position[1] // 3) * 3 + 3):
#                 if num == board[i][j]:
#                     return False
#         return True     # Return True if the number can be placed at the given location
#
#     @staticmethod
#     def find_empty(board):
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == 0:
#                     return i, j     # Return the location of the empty cell
#         return False        # Return False if no empty cell is found
#
#     @staticmethod
#     def solve(board):
#         if not Solver.find_empty(board):
#             return True     # If the grid is completely filled, return True
#         else:
#             position = Solver.find_empty(board)     # Find an empty cell on the grid
#             for i in range(1, 10):      # Try each number from 1 to 9 at the empty cell
#                 if Solver.valid(board, i, position):        # If the number is valid at the empty cell
#                     board[position[0]][position[1]] = i      # Place the number at the empty cell
#                     if Solver.solve(board):     # Recursively solve the puzzle
#                         return True     # If the puzzle is solved, return True
#                     # If the puzzle cannot be solved, backtrack by removing the number from the empty cell
#                     board[position[0]][position[1]] = 0
#         return False        # If the puzzle cannot be solved, return False
#
#     def generate(self):
#         row = random.randrange(9)       # Choose a random row
#         col = random.randrange(9)       # Choose a random column
#         num = random.randrange(1, 10)   # Choose a random number from 1 to 9
#
#         for i in range(30):     # Fill 25 cells with valid random numbers
#             # If the chosen number is not valid or the cell is already filled, choose new random numbers
#             while not Solver.valid(self._board, num, (row, col)) or self._board[row][col] != 0:
#                 row = random.randrange(9)
#                 col = random.randrange(9)
#                 num = random.randrange(1, 10)
#             self._board[row][col] = num    # Place the valid random number at the chosen cell
#
#         copy_grid = copy.deepcopy(self._board)     # Create a deep copy of the grid
#         if not Solver.solve(copy_grid):        # If the puzzle cannot be solved generate new grid
#             self._board = self.generate()
#
#         return self._board
#
#     @staticmethod
#     def calculate_score(board, row, col):
#         score = 0
#
#         # Check the number of empty cells in the same row
#         for c in range(9):
#             if board[row][c] == 0:
#                 score += 1
#
#         # Check the number of empty cells in the same column
#         for r in range(9):
#             if board[r][col] == 0:
#                 score += 1
#
#         # Check the number of empty cells in the same 3x3 box
#         box_start_row = (row // 3) * 3
#         box_start_col = (col // 3) * 3
#         for r in range(box_start_row, box_start_row + 3):
#             for c in range(box_start_col, box_start_col + 3):
#                 if board[r][c] == 0:
#                     score += 1
#
#         return score
#
#     @staticmethod
#     def find_best_indexes(board):
#         scores = []
#
#         for row in range(9):
#             for col in range(9):
#                 if board[row][col] == 0:
#                     score = Solver.calculate_score(board, row, col)
#                     scores.append((score, row, col))
#
#         scores.sort(key=lambda x: x[0])  # Sort the scores based on the first element (score) in ascending order
#
#         best_indexes = [(row, col) for _, row, col in scores]
#
#         # Find best indexes for the row
#         for row in range(9):
#             for col in range(9):
#                 if board[row][col] == 0:
#                     score = Solver.calculate_score(board, row, col)
#                     if score == scores[0][0]:
#                         best_indexes.append((row, col))
#
#         # Find best indexes for the column
#         for col in range(9):
#             for row in range(9):
#                 if board[row][col] == 0:
#                     score = Solver.calculate_score(board, row, col)
#                     if score == scores[0][0]:
#                         best_indexes.append((row, col))
#
#         return best_indexes
#
#     @staticmethod
#     def choose_best_place(board):
#         best_place = None
#         best_options = float('inf')
#
#         for row in range(9):
#             for col in range(9):
#                 if board[row][col] == 0:
#                     options = 0
#                     possible_num = 0
#
#                     for num in range(1, 10):
#                         if Solver.valid(board, num, (row, col)):
#                             options += 1
#                             possible_num = num
#
#                     if options == 1:
#                         return row, col, possible_num
#
#                     if options < best_options:
#                         best_options = options
#                         best_place = (row, col)
#
#         return best_place


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

    for i in range(30):   # Fill 20 cells with valid random numbers
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

def find_best_indexes(board):
    scores = []

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                score = calculate_score(board, row, col)
                scores.append((score, row, col))

    scores.sort(key=lambda x: x[0])  # Sort the scores based on the first element (score) in ascending order

    best_indexes = [(row, col) for _, row, col in scores]

    # Find best indexes for the row
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                score = calculate_score(board, row, col)
                if score == scores[0][0]:
                    best_indexes.append((row, col))

        # Find best indexes for the column
    for col in range(9):
        for row in range(9):
            if board[row][col] == 0:
                score = calculate_score(board, row, col)
                if score == scores[0][0]:
                    best_indexes.append((row, col))

    return best_indexes


def calculate_score(board, row, col):
    score = 0

    # Check the number of empty cells in the same row
    for c in range(9):
        if board[row][c] == 0:
            score += 1

    # Check the number of empty cells in the same column
    for r in range(9):
        if board[r][col] == 0:
            score += 1

    # Check the number of empty cells in the same 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for r in range(box_start_row, box_start_row + 3):
        for c in range(box_start_col, box_start_col + 3):
            if board[r][c] == 0:
                score += 1

    return score
