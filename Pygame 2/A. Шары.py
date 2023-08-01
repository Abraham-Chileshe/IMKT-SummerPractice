import pygame as pygm
from random import *

RED = (255, 0, 0)

class Border(pygm.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2):
        super().__init__(asprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygm.Surface([1, y2 - y1])
            self.rect = pygm.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygm.Surface([x2 - x1, 1])
            self.rect = pygm.Rect(x1, y1, x2 - x1, 1)

class Ball(pygm.sprite.Sprite):

    def __init__(self, radius: int, x: int, y: int):
        super().__init__(asprites)
        self.radius = radius
        self.image = pygm.Surface((2 * radius, 2 * radius), pygm.SRCALPHA, 32)
        pygm.draw.circle(self.image, RED, (radius, radius), radius)
        self.rect = pygm.Rect(x, y, 2 * radius - 5, 2 * radius - 5)
        self.x = x
        self.y = y
        self.vx = speed_var[randint(0, 19)]
        self.vy = speed_var[randint(0, 19)]

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        x1 = horizontal_borders.copy()
        x1.remove(list(x1)[0])
        x2 = horizontal_borders.copy()
        x2.remove(list(x2)[1])
        y1 = vertical_borders.copy()
        y1.remove(list(y1)[0])
        y2 = vertical_borders.copy()
        y2.remove(list(y2)[1])

        if pygm.sprite.spritecollide(self, x1, 0) and self.vy > 0:  
            self.vy = -self.vy
            self.y += 20

        if pygm.sprite.spritecollide(self, x2, 0) and self.vy < 0: 
            self.vy = -self.vy
            self.y -= 20

        if pygm.sprite.spritecollide(self, y1, 0) and self.vx > 0: 
            self.vx = -self.vx
            self.x -= 20

        if pygm.sprite.spritecollide(self, y2, 0) and self.vx < 0:  # Left
            self.vx = -self.vx
            self.x += 20

        rest_balls = asprites.copy()
        rest_balls.remove(self)

        if pygm.sprite.spritecollide(self, rest_balls, 0):
            self.vy = -self.vy
            self.vx = -self.vx

pygm.init()

width, height = map(int, input('\nScreenwidth _ Scrieenheight:').split())
screen = pygm.display.set_mode((width, height))
pygm.display.set_caption("Шары")

asprites = pygm.sprite.Group()
horizontal_borders = pygm.sprite.Group()
vertical_borders = pygm.sprite.Group()
sprite = pygm.sprite.Sprite()

clock = pygm.time.Clock()

ball_speed = int(input('Ball_speed: '))

speed_var = [i for i in range(-10, 11) if i != 0]

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)

asprites.empty()
for _ in range(int(input('Number of balls: '))):
    Ball(20, randint(25, width - 25), randint(25, height - 25))

running = True
while running:
    pos = pygm.mouse.get_pos()
    for event in pygm.event.get():
        if event.type == pygm.QUIT:
            running = False
        if event.type == pygm.MOUSEBUTTONDOWN:
            Ball(20, *pos)
    screen.fill((0, 0, 0))
    asprites.draw(screen)
    asprites.update()
    pygm.display.flip()
    clock.tick(ball_speed)

pygm.quit()
