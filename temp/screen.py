from config import*


class Screen:
    def __init__(self):
        self._size_x = WINDOW_SIZE * 0.4
        self._button_x = WINDOW_SIZE // 2 - self._size_x // 2
        self._size_y = WINDOW_SIZE * 0.1
        self._button_y = WINDOW_SIZE * 0.6 - self._size_y // 2
        self._button2_y = WINDOW_SIZE * 0.75 - self._size_y // 2  # Lower the button2 position
        self._main_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.5))
        self._small_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.1))
        self._button_text = pygame.font.SysFont("Calibri", int(self._size_x * 0.12), 1.5)
        self._button_active = False
        self._button2_active = False
        self._mouse = [0, 0]

    @property
    def button_active(self):
        return self._button_active

    @property
    def button2_active(self):
        return self._button2_active

    def _button(self):
        self._mouse = pygame.mouse.get_pos()

        if (self._button_x + self._size_x) > self._mouse[0] > self._button_x and \
                (self._button_y + self._size_y) > self._mouse[1] > self._button_y:
            pygame.draw.rect(SCREEN, S_BUTTON_COL_DARK_BLUE,
                             (int(self._button_x), int(self._button_y), int(self._size_x), int(self._size_y)))
            self._button_active = True
        else:
            pygame.draw.rect(SCREEN, BUTTON_COL_LIGHT_BLUE,
                             (int(self._button_x), int(self._button_y), int(self._size_x), int(self._size_y)))
            self._button_active = False

    def _button2(self):
        self._mouse = pygame.mouse.get_pos()
        if (self._button_x + self._size_x) > self._mouse[0] > self._button_x and \
                (self._button2_y + self._size_y) > self._mouse[1] > self._button2_y:
            pygame.draw.rect(SCREEN, S_BUTTON_COL_DARK_BLUE,
                             (int(self._button_x), int(self._button2_y), int(self._size_x), int(self._size_y)))
            self._button2_active = True
        else:
            pygame.draw.rect(SCREEN, BUTTON_COL_LIGHT_BLUE,
                             (int(self._button_x), int(self._button2_y), int(self._size_x), int(self._size_y)))
            self._button2_active = False



class HomeScreen(Screen):
    def __init__(self):
        super().__init__()

    def draw_home(self):
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
        self._button2()
        # Render the text "Generate Board!" using the button_text font.
        text = self._button_text.render("Generate Board!", True, BACKGROUND_COL_WIGHT)
        text2 = self._button_text.render("Continue Board!", True, BACKGROUND_COL_WIGHT)
        # Get a rectangle representing the size of the text surface.
        text_rect = text.get_rect()
        text_rect2 = text2.get_rect()
        text_rect2.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.75)
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.6)      # Center the text on the button.
        SCREEN.blit(text, text_rect)        # Blit the text surface onto the screen.
        SCREEN.blit(text2, text_rect2)


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

        self._button()
        # Renders the button text
        text = self._button_text.render("   " * 19 + "Generate New Game!", True, BACKGROUND_COL_WIGHT)
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE * 0.6)      # Sets the position of the button text
        SCREEN.blit(text, text_rect)
