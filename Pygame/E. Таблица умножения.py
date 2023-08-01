import pygame as pg
import random
from math import cos, sin, radians

class Table:
    def __init__(self, len_screen: int, count_nums: int, start_multip: float = 2.0, step_mul: float = 0.001):
        self.len_screen = len_screen
        self.radius = len_screen // 2 - len_screen // 15
        self.step_mul = step_mul
        self.step_rad = 360 // count_nums
        # Ensure count_nums <= 360, otherwise raise an error

        self.cur_multip = float(start_multip)
        self.list_nums = []

    def draw(self, screen: pg.Surface,
             color: pg.Color | tuple[int, int, int] = (0, 191, 255),
             bgc: pg.Color | tuple[int, int, int] = (0, 0, 0),
             width: int = 1) -> None:
        """
        Draw the multiplication table.

        :param screen: The screen where the table will be drawn.
        :type screen: pg.Surface
        :param color: The color of the table.
        :type color: pg.Color | tuple[int, int, int]
        :param bgc: The background color.
        :type bgc: pg.Color | tuple[int, int, int]
        :param width: The width of the circle border.
        :type width: int
        """

        for rad in range(0, 360, self.step_rad):
            pg.draw.circle(screen, color, (self.len_screen // 2, self.len_screen // 2), self.radius, width)
            start_pos = (int(cos(radians(rad)) * self.radius) + self.len_screen // 2,
                         int(sin(radians(rad)) * self.radius) + self.len_screen // 2)
            end_pos = (int(cos(radians(rad * self.cur_multip)) * self.radius) + self.len_screen // 2,
                       int(sin(radians(rad * self.cur_multip)) * self.radius) + self.len_screen // 2)
            pg.draw.line(screen, color, start_pos, end_pos)

    def draw_stat(self, screen: pg.Surface, color: pg.Color | tuple[int, int, int] = (0, 191, 255)) -> None:
        """
        Draw the current multiplier.

        :param screen: The screen where the text will be displayed.
        :type screen: pg.Surface
        :param color: The color of the text.
        :type color: pg.Color | tuple[int, int, int]
        """
        font = pg.font.Font(None, self.len_screen // 25)
        cur_multiplier_text = font.render(f'{self.cur_multip:.3f}', 1, color)
        text_x = 10
        text_y = 10
        screen.blit(cur_multiplier_text, (text_x, text_y))

# Test Inputs
len_side, count_nums, start_multip, step = 600, 360, 1.0, 0.01
fps, lim_fps = 30, 100

screen = pg.display.set_mode((len_side, len_side))
pg.init()

table = Table(len_side, count_nums, start_multip, step)

delta_s, delta_h = 0.1, 0.1
s, h = float(random.randint(0, 100 - 1)), float(random.randint(0, 256 - 1))

sub_color = pg.Color(100, 100, 100)
sub_color.hsva = (h, s, 100, 100)

running = True
drawing = True
clock = pg.time.Clock()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()

            if keys[pg.K_SPACE]:
                drawing = not drawing
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                fps = fps % lim_fps + 1
            else:
                fps = fps % lim_fps + 10

    if not drawing:
        continue

    screen.fill((0, 0, 0))
    table.draw(screen, sub_color)
    sub_color = (h, s, 100, 100)

    font = pg.font.Font(None, len_side // 25)
    cur_fps_text = font.render(f'{fps}', 1, (255, 255, 255))
    text_x = len_side - cur_fps_text.get_width() - 10
    text_y = 10
    screen.blit(cur_fps_text, (text_x, text_y))

    table.draw_stat(screen, (255, 255, 255))
    table.cur_multip += table.step_mul
    pg.display.flip()

    s += delta_s * random.randint(1, 2)
    h += delta_h * random.randint(1, 2)

    if not (0 + delta_s * 2 <= s <= 100 - delta_s * 2):
        delta_s = -delta_s

    if not (0 + delta_h * 2 <= h <= 256 - delta_h * 2):
        delta_h = -delta_h

    clock.tick(fps)

pg.quit()
