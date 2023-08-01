import pygame as pygm

background_color= (0, 0, 0)
drawing_color = (255, 255, 255)

size_screen = tuple(map(int, input("screenwidth _ screenheight: ").split()))
screen = pygm.display.set_mode(size_screen)
screen2 = pygm.display.set_mode(size_screen)
list_surface = []

pygm.init()

drawing = False
x1, y1 = 0,0
width, height = 0, 0

running = True

while running:
    for event in pygm.event.get():
        match event.type:

            case pygm.QUIT:
                running = False

            case pygm.MOUSEBUTTONDOWN:
                drawing = True
                screen2.fill(background_color)
                x1, y1 = event.pos

            case pygm.MOUSEMOTION:
                width, height = event.pos[0] - x1, event.pos[1] - y1
                if drawing:
                    screen2.fill(background_color)
                    screen2.blit(screen, (0, 0))
                    coordinates = (min(x1, x1 + width), min(y1, y1 + height))
                    pygm.draw.rect(screen2, drawing_color, (coordinates, (abs(width), abs(height))), 1)

            case pygm.MOUSEBUTTONUP:
                drawing = False

                coordinates = (min(x1, x1 + width), min(y1, y1 + height))
                list_surface.append((coordinates, (abs(width), abs(height))))
                screen.fill(background_color)
                for entity in list_surface:
                    pygm.draw.rect(screen, drawing_color, entity, 1)

            case pygm.KEYDOWN:
                if not (event.key == pygm.K_z and pygm.key.get_mods() & pygm.KMOD_CTRL):
                    continue
                list_surface.pop(-1)
                screen.fill(background_color)
                for entity in list_surface:
                    pygm.draw.rect(screen, drawing_color, entity, 1)

    if drawing:
        screen.blit(screen2, (0, 0))
        for entity in list_surface:
            pygm.draw.rect(screen, drawing_color, entity, 1)
    pygm.display.flip()


pygm.quit()
