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
player_x = 260
player_y = 410

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
    text = (0, 0, 0)
    player = (182,215,168)
    heart= (224,102,102) 

    # start
    player_block = pygame.draw.rect(screen, player, [player_x, player_y, 25, 25], 0)
    player_block = pygame.draw.rect(screen, line, [player_x, player_y, 25, 25], 2)
    # line
    line_1 = pygame.draw.line(screen, line, [200, 35], [200, 435], 3)
    line_2 = pygame.draw.line(screen, line, [200, 35], [380, 35], 3)
    line_3 = pygame.draw.line(screen, line, [430, 35], [430, 435], 3)
    line_4 = pygame.draw.line(screen, line, [200, 435], [250, 435], 3)
    line_5 = pygame.draw.line(screen, line, [430, 435], [295, 435], 3)
    line_6 = pygame.draw.line(screen, line, [335, 400], [335, 435], 3)
    line_7 = pygame.draw.line(screen, line, [250, 400], [250, 435], 3)
    line_8 = pygame.draw.line(screen, line, [250, 400], [295, 400], 3)
    line_9 = pygame.draw.line(screen, line, [295, 400], [295, 365], 3)
    line_10 = pygame.draw.line(screen, line, [295, 365], [370, 365], 3)
    line_11 = pygame.draw.line(screen, line, [370, 400], [370, 330], 3)
    line_12 = pygame.draw.line(screen, line, [380, 35], [380, 65], 3)
    line_13 = pygame.draw.line(screen, line, [430, 100], [340, 100], 3)
    line_14 = pygame.draw.line(screen, line, [340, 70], [340, 135], 3)
    line_15 = pygame.draw.line(screen, line, [295, 35], [295, 100], 3)
    line_16 = pygame.draw.line(screen, line, [295, 70], [245, 70], 3)
    line_17 = pygame.draw.line(screen, line, [380, 135], [240, 135], 3)
    line_18 = pygame.draw.line(screen, line, [240, 100], [240, 170], 3)
    line_19 = pygame.draw.line(screen, line, [200, 205], [365, 205], 3)
    line_20 = pygame.draw.line(screen, line, [285, 165], [285, 205], 3)
    line_21 = pygame.draw.line(screen, line, [325, 135], [325, 165], 3)
    line_22 = pygame.draw.line(screen, line, [430, 285], [245, 285], 3)
    line_23 = pygame.draw.line(screen, line, [430, 360], [410, 360], 3)
    line_24 = pygame.draw.line(screen, line, [410, 360], [410, 400], 3)
    line_25 = pygame.draw.line(screen, line, [370, 400], [370, 325], 3)
    line_26 = pygame.draw.line(screen, line, [390, 325], [370, 325], 3)
    line_27 = pygame.draw.line(screen, line, [245, 285], [245, 365], 3)
    line_28 = pygame.draw.line(screen, line, [245, 325], [330, 325], 3)
    line_28 = pygame.draw.line(screen, line, [365, 170], [365, 205], 3)
    line_29 = pygame.draw.line(screen, line, [365, 170], [390, 170], 3)
    line_30 = pygame.draw.line(screen, line, [390, 170], [390, 245], 3)
    line_31 = pygame.draw.line(screen, line, [390, 245], [245, 245], 3)

    # heart
    pygame.draw.circle(screen, heart, (465, 420), 8, 0)
    pygame.draw.circle(screen, heart, (477, 420), 8, 0)
    pygame.draw.polygon(screen, heart, [[465, 425], [477, 425], [471, 435]], 0)

    pygame.draw.circle(screen, heart, (500, 420), 8, 0)
    pygame.draw.circle(screen, heart, (512, 420), 8, 0)
    pygame.draw.polygon(screen, heart, [[500, 425], [512, 425], [506, 435]], 0)

    pygame.draw.circle(screen, heart, (535, 420), 8, 0)
    pygame.draw.circle(screen, heart, (547, 420), 8, 0)
    pygame.draw.polygon(screen, heart, [[535, 425], [547, 425], [541, 435]], 0)

    # font
    font=pygame.font.SysFont ('Calibri', 20, True, False)
    text=font.render("START", True, line)
    screen.blit (text, [250, 450])

    font=pygame.font.SysFont ('Calibri', 20, True, False)
    text=font.render("FINISH", True, line)
    screen.blit (text, [380, 10])
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
