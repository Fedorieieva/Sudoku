import pygame


minutes = 0     # the initial value of minutes on the timer is set to 0
seconds = 0     # the initial value of seconds on the timer is set to 0
start_time = 0

WINDOW_SIZE = 700      # the size of the game window is set to 700x700 pixels
MARGIN = 75     # the margin size around the grid is set to 75 pixels

SQUARE_NUM = 9                  # the size of the grid (number of squares) is set to 9x9
SECTION = SQUARE_NUM // 3       # the size of a section of the grid is set to 3x3

SECTION_SIZE = (WINDOW_SIZE - MARGIN * 2) / SECTION      # the size of a section in pixels
SQUARE_SIZE = (WINDOW_SIZE - MARGIN * 2) / SQUARE_NUM    # the size of a square in pixels
# the list of numbers that can be used in the grid
NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

COL_BLACK = (0, 0, 0)                   # the default color for text
SELECT_COL_LIGHT_GREEN = (102, 205, 170)        # the color used for highlighting selected squares
BUTTON_COL_LIGHT_BLUE = (30, 144, 255)        # the color used for buttons
S_BUTTON_COL_DARK_BLUE = (24, 116, 205)        # the color used for selected buttons

BACKGROUND_COL_WIGHT = (255, 255, 255)    # the color used for the background

FONT_SIZE = int((WINDOW_SIZE - MARGIN * 2) * 0.06)     # the font size for the numbers on the grid
LOWER_FONT_SIZE = int(FONT_SIZE * 0.75)     # the font size for the text below the grid

CLOCK = pygame.time.Clock()     # a pygame clock object is created to keep track of time

pygame.init()       # pygame is initialized

SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))       # the game window is created with the specified size
# ICON = pygame.image.load('imgs/logo.png')
#
# pygame.display.set_icon(ICON)
pygame.display.set_caption("Sudoku Fedorieieva")        # the game window caption is set to "Sudoku"

FONT = pygame.font.SysFont("calibri", FONT_SIZE)        # a font object is created for the numbers
LOWER_FONT = pygame.font.SysFont("calibri", LOWER_FONT_SIZE)     # a font object is created for the text below the grid
