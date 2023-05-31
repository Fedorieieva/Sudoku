from config import*


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
