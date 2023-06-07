import time
from config import*
from game import Game
from screen import HomeScreen, EndScreen


class Main:
    def __init__(self):
        self.__minutes = 0
        self.__seconds = 0
        self.__start_time = 0

    @staticmethod
    def __write_to_file(board, mistakes=0, hint=0, timer=(), filename='sudoku_file_manager', mode='a'):
        with open(filename, mode) as file:
            if filename is 'sudoku_continue':
                for row in board:
                    file.write(' '.join(map(str, row)) + '\n')
                file.write(str(mistakes) + "\n" + str(hint))
                file.write(str(timer[0]) + ":" + str(timer[1]))
            else:
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

    def __read_continue_file(self):
        matrix = []
        mistake = None
        with open('sudoku_continue', 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.isdigit():
                    mistake = int(line)
                elif ':' in line:
                    time_parts = line.split(':')
                    self.__minutes = int(time_parts[0])
                    self.__seconds = int(time_parts[1])
                else:
                    row = [int(num) for num in line.split()]
                    matrix.append(row)

        return matrix, mistake

    def __timer(self, stop=False):
        if stop:
            second = int((pygame.time.get_ticks() - self.__start_time) / 1000)
            self.__minutes = second // 60
            self.__seconds = second - self.__minutes * 60
            if self.__seconds == 60:
                self.__seconds = 0
            compound = "Timer: " + str(self.__minutes).zfill(2) + ":" + str(self.__seconds).zfill(2)
            text = LOWER_FONT.render(compound, True, COL_BLACK)
            SCREEN.blit(text, (WINDOW_SIZE - MARGIN - WINDOW_SIZE * 0.17, WINDOW_SIZE * 0.925))
        else:
            return self.__minutes, self.__seconds

    def game(self):
        screen = "HOME"
        run, playing = True, True
        sudoku = Game()
        home = HomeScreen()
        end = EndScreen()
        self.__write_to_file(sudoku.game_board)
        time_played = 0, 0

        while playing:
            if screen == "END":
                time.sleep(3)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if end.button_active:
                            self.__start_time += pygame.time.get_ticks()
                            sudoku = Game()
                            self.__write_to_file(sudoku.game_board)
                            screen = "PLAY"
                if run:
                    time.sleep(3)
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                end.draw_over(sudoku.mistakes, time_played)
                run = False

            if screen == "PLAY":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__write_to_file(sudoku.game_board, sudoku.mistakes, sudoku.hints, time_played, 'sudoku_continue', 'w')
                        playing = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        sudoku.find_location(mouse_x, mouse_y)
                    if event.type == pygame.KEYDOWN:
                        if sudoku.mouse_active:
                            sudoku.detect_keys(event)
                        if event.key == pygame.K_SPACE:
                            sudoku.solve(sudoku.game_board)
                        if event.key == pygame.K_BACKSLASH:
                            sudoku.hints = (sudoku.hints + 1)
                            sudoku.detect_keys(event, True)
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                self.__timer(True)
                sudoku.draw_game()
                sudoku.draw_mistakes()
                sudoku.draw_hints()

                if not sudoku.find_empty(sudoku.game_board):
                    time_played = self.__timer(False)
                    self.__write_to_file(sudoku.game_board, sudoku.mistakes, sudoku.hints, time_played)
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
                            self.__start_time = pygame.time.get_ticks()
                            screen = "PLAY"
                        if home.button2_active:
                            sudoku = Game()
                            sudoku.game_board, sudoku.mistakes = self.__read_continue_file()
                            screen = "PLAY"
                SCREEN.fill(BACKGROUND_COL_WIGHT)
                home.draw_home()

            pygame.display.update()
            CLOCK.tick(30)


Main().game()
