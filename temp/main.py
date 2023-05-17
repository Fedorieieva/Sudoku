# по сожливості додати кілька рівнів складності

import time
from solver import Solver
from config import*
from classes import Game, HomeScreen, EndScreen


class Main:
    def __init__(self):
        self._solver = Solver()
        self._minutes = 0
        self._seconds = 0
        self._start_time = 0

    @staticmethod
    def _write_to_file(board, mistakes=0, hint=0, timer=()):
        with open("sudoku_file_manager", 'a') as file:
            if sum(sum(row) for row in board) < 405:
                file.write("SUDOKU GAME:\n")
                file.write("\tPUZZLE TO SOLVE:\n\n")
                for row in board:
                    file.write('\t' * 2 + ' '.join(map(str, row)) + '\n')
            else:
                file.write("\n\tSOLVED PUZZLE:\n\n")
                for row in board:
                    file.write('\t' * 2 + ' '.join(map(str, row)) + '\n')
                file.write("\nMistakes: " + str(mistakes) + "\t\tHints: " + str(hint))
                file.write("\nIn time " + str(timer[0]) + ":" + str(timer[1]) + "\n" * 3)

    def _timer(self, stop=False):
        if stop:
            second = int((pygame.time.get_ticks() - self._start_time) / 1000)
            self._minutes = second // 60
            # calculate the seconds by subtracting the minutes (converted back to seconds) from the total seconds
            self._seconds = second - self._minutes * 60
            if self._seconds == 60:  # if the seconds have reached 60, reset to 0
                self._seconds = 0
            # create a string to display the time in the format "Timer: MM:SS"
            compound = "Timer: " + str(self._minutes).zfill(2) + ":" + str(self._seconds).zfill(2)
            # create a text object to display the time on the screen
            text = LOWER_FONT.render(compound, True, COL_BLACK)
            # blit the text object onto the bottom right corner of the screen
            SCREEN.blit(text, (WINDOW_SIZE - MARGIN - WINDOW_SIZE * 0.17, WINDOW_SIZE * 0.925))
        else:
            return self._minutes, self._seconds

    def game(self):
        screen = "HOME"
        run, playing = True, True
        sudoku = Game()
        home = HomeScreen()
        end = EndScreen()
        self._write_to_file(sudoku.game_board)
        time_played = 0, 0

        while playing:
            if screen == "END":
                time.sleep(3)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if end.button_active:
                            self._start_time += pygame.time.get_ticks()
                            sudoku = Game()
                            self._write_to_file(sudoku.game_board)
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
                            self._solver.solve(sudoku.game_board)
                        if event.key == pygame.K_BACKSLASH:  # HINT !!!!!!
                            sudoku.hints = (sudoku.hints + 1)
                            sudoku.detect_keys(event, True)
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                self._timer(True)
                sudoku.draw_game()
                sudoku.draw_mistakes_hints()

                if not self._solver.find_empty(sudoku.game_board):
                    time_played = self._timer(False)
                    self._write_to_file(sudoku.game_board, sudoku.mistakes, sudoku.hints, time_played)
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
                            self._start_time = pygame.time.get_ticks()
                            screen = "PLAY"
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                home.draw_home()

            pygame.display.update()
            CLOCK.tick(30)


Main().game()
