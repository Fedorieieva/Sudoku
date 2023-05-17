# по сожливості додати кілька рівнів складності
# перевірити гетери та сетери для атрибутів
# FILE_MANAGER  !!!

import time
from solver import solve, find_empty
from config import*
from classes import Game, HomeScreen, EndScreen


def timer(stop=False):
    global minutes, seconds     # access the global variables minutes and seconds
    # calculate the time elapsed since the start of the game in seconds
    if stop:
        second = int((pygame.time.get_ticks() - start_time) / 1000)
        # second = int((pygame.time.get_ticks()) / 1000)
        minutes = second // 60
        # calculate the seconds by subtracting the minutes (converted back to seconds) from the total seconds
        seconds = second - minutes * 60
        if seconds == 60:  # if the seconds have reached 60, reset to 0
            seconds = 0
        # create a string to display the time in the format "Timer: MM:SS"
        compound = "Timer: " + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
        # create a text object to display the time on the screen
        text = LOWER_FONT.render(compound, True, COL_BLACK)
        # blit the text object onto the bottom right corner of the screen
        SCREEN.blit(text, (WINDOW_SIZE - MARGIN - WINDOW_SIZE * 0.17, WINDOW_SIZE * 0.925))
    else:
        return minutes, seconds


class Main:
    @staticmethod
    def game():
        global start_time
        screen = "HOME"
        run, playing = True, True
        sudoku = Game()
        home = HomeScreen()
        end = EndScreen()

        while playing:
            if screen == "END":
                time_played = timer(False)
                time.sleep(3)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if end.button_active:
                            start_time += pygame.time.get_ticks()
                            sudoku = Game()
                            screen = "PLAY"
                if run:
                    time.sleep(3)
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                end.draw_over(sudoku.mistakes, time_played)
                run = False

            if screen == "PLAY":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        sudoku.find_location(mouse_x, mouse_y)
                    if event.type == pygame.KEYDOWN:
                        if sudoku.mouse_active:
                            sudoku.detect_keys(event)
                        if event.key == pygame.K_SPACE:
                            solve(sudoku.game_board)
                        if event.key == pygame.K_BACKSLASH:  # HINT !!!!!!
                            sudoku.hints = (sudoku.hints + 1)
                            sudoku.detect_keys(event, True)
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                timer(True)
                sudoku.draw_game()
                sudoku.draw_mistakes_hints()

                if not find_empty(sudoku.game_board):
                    screen = "END"
                    sudoku.mouse_active = False

                if sudoku.mouse_active:
                    sudoku.draw_sel_box()

                if sudoku.key_active:
                    sudoku.draw_num()

            if screen == "HOME":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if home.button_active:
                            start_time = pygame.time.get_ticks()
                            screen = "PLAY"
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                home.draw_home()

            pygame.display.update()
            CLOCK.tick(30)


Main.game()
