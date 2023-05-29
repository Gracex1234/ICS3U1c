import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x = 400
cloud_y = 300


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill("#cfe2f3")  # always the first drawing command

    line = (0, 0, 0)

    # line
    line_1 = pygame.draw.line(screen, line, [200, 35], [200, 435], 2)
    line_2 = pygame.draw.line(screen, line, [200, 35], [430, 35], 2)
    line_3 = pygame.draw.line(screen, line, [430, 35], [430, 435], 2)
    line_4 = pygame.draw.line(screen, line, [200, 435], [430, 435], 2)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
