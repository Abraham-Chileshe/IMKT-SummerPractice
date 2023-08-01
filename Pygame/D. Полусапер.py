import pygame as pg
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (150, 150, 150)

# Board dimensions
ROWS = 10
COLS = 10
CELL_SIZE = 40

# Minesweeper board class
class MinesweeperBoard:
    def __init__(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.mines = set()

    def place_mines(self, num_mines):
        self.mines = set(random.sample(range(ROWS * COLS), num_mines))
        for mine in self.mines:
            row, col = mine // COLS, mine % COLS
            self.board[row][col] = -1

        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != -1:
                    for i in range(max(0, row - 1), min(ROWS, row + 2)):
                        for j in range(max(0, col - 1), min(COLS, col + 2)):
                            if self.board[i][j] == -1:
                                self.board[row][col] += 1

    def reveal_cell(self, row, col):
        if (row, col) in self.mines:
            return False
        if self.board[row][col] == 0:
            self.board[row][col] = -2
            for i in range(max(0, row - 1), min(ROWS, row + 2)):
                for j in range(max(0, col - 1), min(COLS, col + 2)):
                    if self.board[i][j] == 0:
                        self.reveal_cell(i, j)
        return True

    def is_mine(self, row, col):
        return (row, col) in self.mines

    def get_cell_value(self, row, col):
        return self.board[row][col]

# Chessboard class
class Board:
    def __init__(self):
        self.cells = [[BLACK if (row + col) % 2 == 0 else BLACK for col in range(COLS)] for row in range(ROWS)]

    def draw(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                cell_rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pg.draw.rect(screen, self.cells[row][col], cell_rect)

# Pygame setup
pg.init()
screen = pg.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE))
pg.display.set_caption("Minesweeper")
clock = pg.time.Clock()

# Create the Minesweeper board and place mines
minesweeper_board = MinesweeperBoard()
minesweeper_board.place_mines(15)

board_pattern = Board()

running = True
revealed_cells = set()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                row, col = event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE
                if (row, col) not in revealed_cells:
                    if minesweeper_board.reveal_cell(row, col):
                        revealed_cells.add((row, col))
                        if minesweeper_board.is_mine(row, col):
                            running = False

    # Draw the board
    screen.fill(WHITE)
    board_pattern.draw(screen)

    for row in range(ROWS):
        for col in range(COLS):
            cell_rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if (row, col) in revealed_cells:
                cell_value = minesweeper_board.get_cell_value(row, col)
                if cell_value == 0:
                    pg.draw.rect(screen, GREY, cell_rect)
                elif cell_value == -1:
                    pg.draw.rect(screen, RED, cell_rect)
                else:
                    pg.draw.rect(screen, GREY, cell_rect)
                    font = pg.font.Font(None, CELL_SIZE // 2)
                    cell_text = font.render(str(cell_value), True, BLACK)
                    text_rect = cell_text.get_rect(center=cell_rect.center)
                    screen.blit(cell_text, text_rect)

            # Draw the grey border for each cell
            pg.draw.rect(screen, GREY, cell_rect, 1)

    pg.display.flip()
    clock.tick(30)

pg.quit()
