import copy
from solver import solve, generate, valid
from config import*


class Game:
    def __init__(self):
        self.board = generate()     # creates a board by calling the `generate` function
        self.initial_board = tuple(map(tuple, self.board))
        self.mouse_active = False   # sets `mouse_active` to False
        self.key_active = False     # sets `key_active` to False
        self.info = ''      # initializes an empty string for `info`
        self.mistakes = 0   # sets the number of mistakes to 0
        self.hints = 0
        self.s_col = 0      # initializes the selected column to 0
        self.s_row = 0      # initializes the selected row to 0
        self.location = [0, 0]   # initializes the location of the selected box to 0

    def draw_game(self):
        increment = MARGIN      # sets the increment to the `MARGIN`
        for i in range(SECTION + 1):
            # draws the horizontal lines of the board
            pygame.draw.line(SCREEN, COL_BLACK, (MARGIN, increment), (WINDOW_SIZE - MARGIN, increment), 3)
            # draws the vertical lines of the board
            pygame.draw.line(SCREEN, COL_BLACK, (increment, MARGIN), (increment, WINDOW_SIZE - MARGIN), 3)
            # updates the value of the increment for the next iteration
            increment += SECTION_SIZE

        increment = MARGIN      # resets the increment to the `MARGIN` value
        for i in range(SQUARE_NUM + 1):
            # draws the thin horizontal lines that separate the squares
            pygame.draw.line(SCREEN, COL_BLACK, (MARGIN, increment), (WINDOW_SIZE - MARGIN, increment))
            # draws the thin vertical lines that separate the squares
            pygame.draw.line(SCREEN, COL_BLACK, (increment, MARGIN), (increment, WINDOW_SIZE - MARGIN))
            # updates the value of the increment for the next iteration
            increment += SQUARE_SIZE

        increment_x = increment_y = MARGIN + SQUARE_SIZE // 2  # initializes the increment_x and increment_y values

        for row in range(len(self.board)):      # loops over the rows of the board
            for col in range(len(self.board[0])):   # loops over the columns of the board
                # if a box has a value that is not 0, render the value as text
                if self.board[row][col] != 0 and self.board[row][col] != self.initial_board[row][col]:
                    text = FONT.render(str(self.board[row][col]), True, COL_BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = (increment_x, increment_y)
                    SCREEN.blit(text, text_rect)
                elif self.initial_board[row][col] != 0:
                    text = FONT.render(str(self.board[row][col]), True, (0, 0, 255))
                    text_rect = text.get_rect()
                    text_rect.center = (increment_x, increment_y)
                    SCREEN.blit(text, text_rect)

                increment_x += SQUARE_SIZE  # updates the value of the increment_x for the next iteration
            increment_x = MARGIN + SQUARE_SIZE // 2  # resets the value of increment_x to the original value
            increment_y += SQUARE_SIZE      # updates the value of increment_y for the next iteration
        # increment_y = MARGIN + SQUARE_SIZE // 2 THE BEGINNING VARIANT!!!
        # renders the "Press space-bar to solve" text
        text = FONT.render("Press space-bar to solve", True, COL_BLACK)
        text2 = FONT.render("Select section & press back-slash to show hint", True, COL_BLACK)
        SCREEN.blit(text, (MARGIN + 115, WINDOW_SIZE * 0.0155))
        SCREEN.blit(text2, (MARGIN - 27, WINDOW_SIZE * 0.06))

    # This method takes in the mouse x and y coordinates and finds the corresponding row and column
    # on the game board, as well as the pixel coordinates of the corresponding square on the game board.
    def find_location(self, mouse_x, mouse_y):
        # Calculate the column of the square that the mouse is currently over.
        self.s_col = int((mouse_x - MARGIN) // SQUARE_SIZE)
        # Calculate the row of the square that the mouse is currently over.
        self.s_row = int((mouse_y - MARGIN) // SQUARE_SIZE)
        # Calculate the pixel location of the square that the mouse is currently over.
        self.location = (MARGIN + (self.s_col * int(SQUARE_SIZE)), MARGIN + (self.s_row * int(SQUARE_SIZE)))
        # If the mouse is inside the game board and the square the mouse is over is empty,
        # set the mouse_active flag to true.
        if (mouse_x > MARGIN) and (mouse_x < WINDOW_SIZE - MARGIN) and (mouse_y > MARGIN) and \
                (mouse_y < WINDOW_SIZE - MARGIN) and self.board[self.s_row][self.s_col] == 0:
            self.info = ''  # Reset the info message.
            self.mouse_active = True
        else:   # If the mouse is outside the game board or the square the mouse is over
            # is not empty, set the mouse_active flag to false.
            del self.s_row  # Delete the previously calculated row, column and location.
            del self.s_col
            del self.location
            self.mouse_active = False   # Set the mouse_active flag to false.
            self.key_active = False     # Set the key_active flag to false.

    # This method draws a selection box around the square that the mouse is currently over.
    def draw_sel_box(self):
        pygame.draw.rect(SCREEN, SELECT_COL_LIGHT_GREEN, (self.location[0], self.location[1],
                                                          SQUARE_SIZE, SQUARE_SIZE), 4)

    def detect_keys(self, info, hint=False):
        # Check if the pressed key is a number from 1 to 9
        if hint:
            for i in range(1, 10):
                self.info = str(i)
                self.finalize_key(True)

        if info.unicode in NUMBERS:
            # If it is, set the key_active flag to True and store the number in the info attribute
            self.key_active = True
            self.info = info.unicode
        # Check if the pressed key is the Enter key and there is a number stored in the info attribute
        elif info.key == 13 and self.info in NUMBERS:
            # If it is, call the finalize_key method
            # self.finalize_key(info) THE BEGINNING VARIANT!!!
            self.finalize_key()
        else:
            # Otherwise, set the key_active flag to False and clear the info attribute
            self.key_active = False
            self.info = ''

    def draw_num(self):
        # Create a text surface for the stored number with blue text
        text = FONT.render(self.info, True, COL_BLACK)  # color blue when in box, then changes to black
        # Get the rect for the text surface and center it in the box
        text_rect = text.get_rect()
        text_rect.center = (self.location[0] + SQUARE_SIZE // 2, self.location[1] + SQUARE_SIZE // 2)
        # Draw the text surface on the screen at the center of the box
        SCREEN.blit(text, text_rect)

    # def finalize_key(self, event): THE BEGINNING VARIANT!!!
    def finalize_key(self, hint=False):
        new = copy.deepcopy(self.board)     # create a copy of the current board
        # set the value of the clicked square to the input number
        new[self.s_row][self.s_col] = int(self.info)
        # if the move is valid and the board can be solved:
        if valid(self.board, int(self.info), (self.s_row, self.s_col)) and solve(new):
            self.board[self.s_row][self.s_col] = int(self.info)     # update the board with the new value
        elif not hint:    # if the user did not request a hint:
            self.mistakes += 1      # increase the mistakes count
        self.mouse_active = False  # deactivate mouse
        self.key_active = False  # deactivate keyboard
        self.info = ''      # reset input information

    def draw_mistakes_hints(self):
        # create a text object with the number of mistakes
        for i in range(2):
            if i == 0:
                text = LOWER_FONT.render("Mistakes " + str(self.mistakes), True, COL_BLACK)
            else:
                text = LOWER_FONT.render("Hints " + str(self.hints), True, COL_BLACK)
            text_rect = text.get_rect()     # get the rectangle of the text object
            #  center the rectangle at the bottom of the screen
            text_rect.center = (WINDOW_SIZE // 7.5, WINDOW_SIZE - (MARGIN // 2))
            if i == 0:
                SCREEN.blit(text, (MARGIN, WINDOW_SIZE * 0.925))    # draw the text at the bottom of the screen
            else:
                SCREEN.blit(text, (MARGIN + 245, WINDOW_SIZE * 0.925))


class Screen:
    def __init__(self):
        self.size_x = WINDOW_SIZE * 0.4  # set the width of the button to 40% of the screen size
        # set the horizontal position of the button to the center
        self.button_x = WINDOW_SIZE // 2 - self.size_x // 2
        # set the height of the button to 10% of the screen siz
        self.size_y = WINDOW_SIZE * 0.1
        # set the vertical position of the button to the middle of the screen
        self.button_y = WINDOW_SIZE * 0.6 - self.size_y // 2
        # set the font size and type for the main text
        self.main_text = pygame.font.SysFont("Calibri", int(self.size_x * 0.5))
        # set the font size and type for the small text
        self.small_text = pygame.font.SysFont("Calibri", int(self.size_x * 0.1))
        # set the font size and type for the button text
        self.button_text = pygame.font.SysFont("Calibri", int(self.size_x * 0.12), 1.5)
        self.active = False  # Initializes the state of the button as inactive
        # self.mouse_x = 0      THE BEGINNING VARIANT!!!
        # self.mouse_y = 0      THE BEGINNING VARIANT!!!
        self.mouse = [0, 0]  # Initializes the position of the mouse

    def button(self):
        # self.mouse_x = pygame.mouse.get_pos()[0]      THE BEGINNING VARIANT!!!
        # self.mouse_y = pygame.mouse.get_pos()[1]      THE BEGINNING VARIANT!!!
        self.mouse = pygame.mouse.get_pos()  # get the current mouse position and store it in the variable 'mouse'

        # if (self.button_x + self.size_x) > self.mouse_x > self.button_x and \  THE BEGINNING VARIANT!!!
        #         (self.button_y + self.size_y) > self.mouse_y > self.button_y:  THE BEGINNING VARIANT!!!
        if (self.button_x + self.size_x) > self.mouse[0] > self.button_x and \
                (self.button_y + self.size_y) > self.mouse[1] > self.button_y:
            # pygame.draw.rect(SCREEN, S_BUTTON_COL, (self.button_x, self.button_y, self.size_x, self.size_y))
            # THE BEGINNING VARIANT!!!
            # if the mouse is over the button, draw the button with a different color and set it as active
            pygame.draw.rect(SCREEN, S_BUTTON_COL_DARK_BLUE,
                             (int(self.button_x), int(self.button_y), int(self.size_x), int(self.size_y)))
            self.active = True
        else:
            # pygame.draw.rect(SCREEN, BUTTON_COL, (self.button_x, self.button_y, self.size_x, self.size_y))
            # THE BEGINNING VARIANT!!!
            # if the mouse is not over the button, draw the button with the default color and set it as inactive
            pygame.draw.rect(SCREEN, BUTTON_COL_LIGHT_BLUE,
                             (int(self.button_x), int(self.button_y), int(self.size_x), int(self.size_y)))
            self.active = False


class HomeScreen(Screen):
    # def __init__(self):
    #     super().__init__()

    def draw_home(self):
        # Render the main title "Sudoku" using the main_text font.
        text = self.main_text.render("Sudoku", True, COL_BLACK)
        # Get a rectangle representing the size of the text surface.
        text_rect = text.get_rect()
        # Center the text on top of the screen.
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.45)
        # Blit the text surface onto the screen.
        SCREEN.blit(text, text_rect)
        # Render the small text "Created by Fed IP-23" using the small_text font.
        text = self.small_text.render("Created by Fedorieieva IP-23", True, COL_BLACK)
        # Blit the text surface onto the screen at a specific position.
        SCREEN.blit(text, (WINDOW_SIZE * 0.025, WINDOW_SIZE * 0.925))

        self.button()       # Call the button method to draw the button.
        # Render the text "Generate Board!" using the button_text font.
        text = self.button_text.render("Generate Board!", True, BACKGROUND_COL_WIGHT)
        # Get a rectangle representing the size of the text surface.
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.6)      # Center the text on the button.
        SCREEN.blit(text, text_rect)        # Blit the text surface onto the screen.


class EndScreen(Screen):
    def __init__(self):
        super().__init__()
        self.button_x = WINDOW_SIZE // 2    # Sets the horizontal position of the button
        # Defines the font for the main text
        self.main_text = pygame.font.SysFont("Calibri", int(self.size_x * 0.4))
        # Defines the font for the button text
        self.button_text = pygame.font.SysFont("Calibri", int(self.size_x * 0.075), 1.5)

    def draw_over(self, mistakes, time):
        text = self.main_text.render("GAME OVER!", True, COL_BLACK)     # Renders the "GAME OVER!" message
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

        self.button()       # Draws the "Generate New Game" button
        # Renders the button text
        text = self.button_text.render("    " * 14 + "Generate New Game!", True, BACKGROUND_COL_WIGHT)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.6)      # Sets the position of the button text
        SCREEN.blit(text, text_rect)
