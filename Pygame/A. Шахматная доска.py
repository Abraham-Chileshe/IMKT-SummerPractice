import pygame as pygm

class Chess:
    def __init__(self, length: int, cnt_cells: int):
        self.length = length
        self.cell_len = length // cnt_cells
        self.cell_begin_coords = []
        
        x, y = 0, 0

        for i in range(cnt_cells):
            self.cell_begin_coords.append([])
            for _ in range(cnt_cells):
                self.cell_begin_coords[i].append((x, y))
                x += self.cell_len
            x = 0
            y += self.cell_len

    #Drawing the chess Chess
    def draw(self, screen: pygm.Surface, colors: tuple[pygm.Color | tuple[int, int, int], pygm.Color | tuple[int, int, int]] = ((0, 0, 0), (255, 255, 255))) -> None:
        for index_side, side in enumerate(self.cell_begin_coords):
            for index_cell, coord in enumerate(side):
                x, y = coord
                color = colors[(index_side + index_cell) % 2]
                pygm.draw.rect(screen, color, (x, y, self.cell_len, self.cell_len), 0)
               

if __name__=='__main__':
    len_side, count_squares = map(int, input("Enter Window size _ cell number: ").split())
    screen = pygm.display.set_mode((len_side, len_side))
    pygm.init()
    Chess = Chess(len_side, count_squares)

    running = True
    while running:
        for event in pygm.event.get():
            if event.type == pygm.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the screen with white color
        Chess.draw(screen)  # Draw the Chess on the screen
        pygm.display.flip()  # Update the display

    pygm.quit()
