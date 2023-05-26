import copy
import random
# from solver import Solver
from config import*
#
#
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
#         return True  # Return True if the number can be placed at the given location
#
#     @staticmethod
#     def find_empty(board):
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] == 0:
#                     return i, j  # Return the location of the empty cell
#         return False  # Return False if no empty cell is found
#
#     @staticmethod
#     def solve(board):
#         if not Solver.find_empty(board):
#             return True  # If the grid is completely filled, return True
#         else:
#             position = Solver.find_empty(board)  # Find an empty cell on the grid
#             for i in range(1, 10):  # Try each number from 1 to 9 at the empty cell
#                 if Solver.valid(board, i, position):  # If the number is valid at the empty cell
#                     board[position[0]][position[1]] = i  # Place the number at the empty cell
#                     if Solver.solve(board):  # Recursively solve the puzzle
#                         return True  # If the puzzle is solved, return True
#                     # If the puzzle cannot be solved, backtrack by removing the number from the empty cell
#                     board[position[0]][position[1]] = 0
#         return False  # If the puzzle cannot be solved, return False
#
#     def generate(self):
#         row = random.randrange(9)  # Choose a random row
#         col = random.randrange(9)  # Choose a random column
#         num = random.randrange(1, 10)  # Choose a random number from 1 to 9
#
#         for i in range(30):  # Fill 20 cells with valid random numbers
#             # If the chosen number is not valid or the cell is already filled, choose new random numbers
#             while not Solver.valid(self._board, num, (row, col)) or self._board[row][col] != 0:
#                 row = random.randrange(9)
#                 col = random.randrange(9)
#                 num = random.randrange(1, 10)
#             self._board[row][col] = num  # Place the valid random number at the chosen cell
#
#         copy_grid = copy.deepcopy(self._board)  # Create a deep copy of the grid
#         if not Solver.solve(copy_grid):  # If the puzzle cannot be solved generate new grid
#             self._board = self.generate()
#
#         return self._board
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
#             # Find best indexes for the column
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


class Game:
    def __init__(self):
        # self._solver = Solver()
        self._game_board = Game.generate()
        self._initial_board = tuple(map(tuple, self._game_board))
        self._mouse_active = False
        self._key_active = False
        self._info = ''
        self._mistakes = 0
        self._hints = 0
        self._selected_col = 0
        self._selected_row = 0
        self._location = [0, 0]

    @staticmethod
    def generate():
        board = [[0 for i in range(9)] for j in range(9)]
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)

        for i in range(30):  # Fill 20 cells with valid random numbers
            # If the chosen number is not valid or the cell is already filled, choose new random numbers
            while not Game.valid(board, num, (row, col)) or board[row][col] != 0:
                row = random.randrange(9)
                col = random.randrange(9)
                num = random.randrange(1, 10)
            board[row][col] = num  # Place the valid random number at the chosen cell

        copy_grid = copy.deepcopy(board)  # Create a deep copy of the grid
        if not Game.solve(copy_grid):  # If the puzzle cannot be solved generate new grid
            board = Game.generate()

        return board

    @staticmethod
    def valid(board, num, position):
        # Check if the number is already in the same row or column
        for i in range(9):
            if num == board[position[0]][i]:
                return False
        for i in range(9):
            if num == board[i][position[1]]:
                return False
        # Check if the number is already in the same 3x3 sub-grid
        for i in range((position[0] // 3) * 3, (position[0] // 3) * 3 + 3):
            for j in range((position[1] // 3) * 3, (position[1] // 3) * 3 + 3):
                if num == board[i][j]:
                    return False
        return True

    @staticmethod
    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j  # Return the location of the empty cell
        return False  # Return False if no empty cell is found

    @staticmethod
    def solve(board):
        if not Game.find_empty(board):
            return True
        else:
            position = Game.find_empty(board)
            for i in range(1, 10):
                if Game.valid(board, i, position):
                    board[position[0]][position[1]] = i  # Place the number at the empty cell
                    if Game.solve(board):  # Recursively solve the puzzle
                        return True
                    # If the puzzle cannot be solved, backtrack by removing the number from the empty cell
                    board[position[0]][position[1]] = 0
        return False  # If the puzzle cannot be solved, return False

    @staticmethod
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

    @staticmethod
    def find_best_indexes(board):
        scores = []

        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    score = Game.calculate_score(board, row, col)
                    scores.append((score, row, col))

        scores.sort(key=lambda x: x[0])  # Sort the scores based on the first element (score) in ascending order

        best_indexes = [(row, col) for _, row, col in scores]

        # Find best indexes for the row
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    score = Game.calculate_score(board, row, col)
                    if score == scores[0][0]:
                        best_indexes.append((row, col))

            # Find best indexes for the column
        for col in range(9):
            for row in range(9):
                if board[row][col] == 0:
                    score = Game.calculate_score(board, row, col)
                    if score == scores[0][0]:
                        best_indexes.append((row, col))

        return best_indexes

    @property
    def game_board(self):
        return self._game_board

    @property
    def mouse_active(self):
        return self._mouse_active

    @mouse_active.setter
    def mouse_active(self, mouse_active):
        self._mouse_active = mouse_active

    @property
    def key_active(self):
        return self._key_active

    @property
    def mistakes(self):
        return self._mistakes

    @property
    def hints(self):
        return self._hints

    @hints.setter
    def hints(self, hints):
        self._hints = hints

    def draw_game(self):    # IS USED IN MAIN
        increment = MARGIN
        for i in range(SECTION + 1):
            # draws the horizontal lines of the board
            pygame.draw.line(SCREEN, COL_BLACK, (MARGIN, increment), (WINDOW_SIZE - MARGIN, increment), 3)
            # draws the vertical lines of the board
            pygame.draw.line(SCREEN, COL_BLACK, (increment, MARGIN), (increment, WINDOW_SIZE - MARGIN), 3)
            # updates the value of the increment for the next iteration
            increment += SECTION_SIZE

        increment = MARGIN
        for i in range(SQUARE_NUM + 1):
            # draws the thin horizontal lines that separate the squares
            pygame.draw.line(SCREEN, COL_BLACK, (MARGIN, increment), (WINDOW_SIZE - MARGIN, increment))
            # draws the thin vertical lines that separate the squares
            pygame.draw.line(SCREEN, COL_BLACK, (increment, MARGIN), (increment, WINDOW_SIZE - MARGIN))
            # updates the value of the increment for the next iteration
            increment += SQUARE_SIZE

        increment_x = increment_y = MARGIN + SQUARE_SIZE // 2

        for row in range(9):
            for col in range(9):
                # if a box has a value that is not 0, render the value as text
                if self._game_board[row][col] != 0 and self._game_board[row][col] != self._initial_board[row][col]:
                    text = FONT.render(str(self._game_board[row][col]), True, COL_BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = (increment_x, increment_y)
                    SCREEN.blit(text, text_rect)
                elif self._initial_board[row][col] != 0:
                    text = FONT.render(str(self._game_board[row][col]), True, (0, 0, 255))
                    text_rect = text.get_rect()
                    text_rect.center = (increment_x, increment_y)
                    SCREEN.blit(text, text_rect)

                increment_x += SQUARE_SIZE
            increment_x = MARGIN + SQUARE_SIZE // 2
            increment_y += SQUARE_SIZE
        text = FONT.render("Press space-bar to solve", True, COL_BLACK)
        text2 = FONT.render("Press back-slash to show hint", True, COL_BLACK)
        SCREEN.blit(text, (MARGIN + 115, WINDOW_SIZE * 0.0155))
        SCREEN.blit(text2, (MARGIN - 27, WINDOW_SIZE * 0.06))

    def find_location(self, mouse_x, mouse_y):  # IS USED IN MAIN
        # Calculate the column of the square that the mouse is currently over.
        self._selected_col = int((mouse_x - MARGIN) // SQUARE_SIZE)
        # Calculate the row of the square that the mouse is currently over.
        self._selected_row = int((mouse_y - MARGIN) // SQUARE_SIZE)
        # Calculate the pixel location of the square that the mouse is currently over.
        self._location = (MARGIN + (self._selected_col * int(SQUARE_SIZE)),
                          MARGIN + (self._selected_row * int(SQUARE_SIZE)))
        # If the mouse is inside the game board and the square the mouse is over is empty,
        # set the mouse_active flag to true.
        if (mouse_x > MARGIN) and (mouse_x < WINDOW_SIZE - MARGIN) and (mouse_y > MARGIN) and \
                (mouse_y < WINDOW_SIZE - MARGIN) and self._game_board[self._selected_row][self._selected_col] == 0:
            self._info = ''
            self.mouse_active = True
        else:   # If the mouse is outside the game board or the square the mouse is over
            # is not empty, set the mouse_active flag to false.
            del self._selected_row
            del self._selected_col
            del self._location
            self.mouse_active = False
            self._key_active = False

    def draw_sel_box(self):     # IS USED IN MAIN
        pygame.draw.rect(SCREEN, SELECT_COL_LIGHT_GREEN, (self._location[0], self._location[1],
                                                          SQUARE_SIZE, SQUARE_SIZE), 4)

    def detect_keys(self, info, hint=False):    # IS USED IN MAIN
        if hint:
            board_copy = copy.deepcopy(self._game_board)
            self._selected_row, self._selected_col = Game.find_best_indexes(board_copy)[0]
            for i in range(1, 10):
                self._info = str(i)
                self._finalize_key(True)

        if info.unicode in NUMBERS:
            self._key_active = True
            self._info = info.unicode
        # Check if the pressed key is the Enter key and there is a number stored in the info attribute
        elif info.key == 13 and self._info in NUMBERS:
            self._finalize_key()
        else:
            self._key_active = False
            # self._info = ''

    def draw_num(self):     # IS USED IN MAIN
        text = FONT.render(self._info, True, COL_BLACK)
        text_rect = text.get_rect()
        text_rect.center = (self._location[0] + SQUARE_SIZE // 2, self._location[1] + SQUARE_SIZE // 2)
        SCREEN.blit(text, text_rect)

    def _finalize_key(self, hint=False):
        board_copy = copy.deepcopy(self._game_board)

        board_copy[self._selected_row][self._selected_col] = int(self._info)
        if Game.valid(self._game_board, int(self._info), (self._selected_row, self._selected_col)) \
                and Game.solve(board_copy):
            self._game_board[self._selected_row][self._selected_col] = int(self._info)
        elif not hint:
            self._mistakes += 1
        self.mouse_active = False
        self._key_active = False
        self._info = ''

    def draw_mistakes(self):
        text = LOWER_FONT.render("Mistakes " + str(self._mistakes), True, COL_BLACK)
        SCREEN.blit(text, (MARGIN, WINDOW_SIZE * 0.925))

    def draw_hints(self):
        text = LOWER_FONT.render("Hints: " + str(self._hints), True, COL_BLACK)
        SCREEN.blit(text, (MARGIN + 239, WINDOW_SIZE * 0.925))


class Screen:
    def __init__(self):
        self._size_x = WINDOW_SIZE * 0.4  # set the width of the button to 40% of the screen size
        # set the horizontal position of the button to the center
        self._button_x = WINDOW_SIZE // 2 - self._size_x // 2
        # set the height of the button to 10% of the screen siz
        self._size_y = WINDOW_SIZE * 0.1
        # set the vertical position of the button to the middle of the screen
        self._button_y = WINDOW_SIZE * 0.6 - self._size_y // 2
        # set the font size and type for the main text
        self._main_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.5))
        # set the font size and type for the small text
        self._small_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.1))
        # set the font size and type for the button text
        self._button_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.12), 1.5)
        self._button_active = False  # Initializes the state of the button as inactive
        # self.mouse_x = 0      THE BEGINNING VARIANT!!!
        # self.mouse_y = 0      THE BEGINNING VARIANT!!!
        self._mouse = [0, 0]  # Initializes the position of the mouse

    @property
    def button_active(self):
        return self._button_active

    def _button(self):
        # self.mouse_x = pygame.mouse.get_pos()[0]      THE BEGINNING VARIANT!!!
        # self.mouse_y = pygame.mouse.get_pos()[1]      THE BEGINNING VARIANT!!!
        self._mouse = pygame.mouse.get_pos()  # get the current mouse position and store it in the variable 'mouse'

        # if (self.button_x + self.size_x) > self.mouse_x > self.button_x and \  THE BEGINNING VARIANT!!!
        #         (self.button_y + self.size_y) > self.mouse_y > self.button_y:  THE BEGINNING VARIANT!!!
        if (self._button_x + self._size_x) > self._mouse[0] > self._button_x and \
                (self._button_y + self._size_y) > self._mouse[1] > self._button_y:
            # pygame.draw.rect(SCREEN, S_BUTTON_COL, (self.button_x, self.button_y, self.size_x, self.size_y))
            # THE BEGINNING VARIANT!!!
            # if the mouse is over the button, draw the button with a different color and set it as active
            pygame.draw.rect(SCREEN, S_BUTTON_COL_DARK_BLUE,
                             (int(self._button_x), int(self._button_y), int(self._size_x), int(self._size_y)))
            self._button_active = True
        else:
            # pygame.draw.rect(SCREEN, BUTTON_COL, (self.button_x, self.button_y, self.size_x, self.size_y))
            # THE BEGINNING VARIANT!!!
            # if the mouse is not over the button, draw the button with the default color and set it as inactive
            pygame.draw.rect(SCREEN, BUTTON_COL_LIGHT_BLUE,
                             (int(self._button_x), int(self._button_y), int(self._size_x), int(self._size_y)))
            self._button_active = False


class HomeScreen(Screen):
    def __init__(self):
        super().__init__()

    def draw_home(self):    # IS USED IN MAIN
        # Render the main title "Sudoku" using the main_text font.
        text = self._main_text.render("Sudoku", True, COL_BLACK)
        # Get a rectangle representing the size of the text surface.
        text_rect = text.get_rect()
        # Center the text on top of the screen.
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.45)
        # Blit the text surface onto the screen.
        SCREEN.blit(text, text_rect)
        # Render the small text "Created by Fed IP-23" using the small_text font.
        text = self._small_text.render("Created by Fedorieieva IP-23", True, COL_BLACK)
        # Blit the text surface onto the screen at a specific position.
        SCREEN.blit(text, (WINDOW_SIZE * 0.025, WINDOW_SIZE * 0.925))

        self._button()       # Call the button method to draw the button.
        # Render the text "Generate Board!" using the button_text font.
        text = self._button_text.render("Generate Board!", True, BACKGROUND_COL_WIGHT)
        # Get a rectangle representing the size of the text surface.
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.6)      # Center the text on the button.
        SCREEN.blit(text, text_rect)        # Blit the text surface onto the screen.


class EndScreen(Screen):
    def __init__(self):
        super().__init__()
        self._button_x = WINDOW_SIZE // 2    # Sets the horizontal position of the button
        # Defines the font for the main text
        self._main_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.4))
        # Defines the font for the button text
        self._button_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.075), 1.5)

    def draw_over(self, mistakes, time):        # IS USED IN MAIN
        text = self._main_text.render("GAME OVER!", True, COL_BLACK)     # Renders the "GAME OVER!" message
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.35)     # Sets the position of the "GAME OVER!" message
        SCREEN.blit(text, text_rect)
        # Creates a message with the end game statistics
        compound = "You finished with " + str(mistakes) + " mistakes and in the time " + \
                   str(time[0]).zfill(2) + ":" + str(time[1]).zfill(2)
        text = FONT.render(compound, True, COL_BLACK)       # Renders the message
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE // 2)       # Sets the position of the message
        SCREEN.blit(text, text_rect)

        self._button()       # Draws the "Generate New Game" button
        # Renders the button text
        text = self._button_text.render("   " * 19 + "Generate New Game!", True, BACKGROUND_COL_WIGHT)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.6)      # Sets the position of the button text
        SCREEN.blit(text, text_rect)
