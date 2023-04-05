# GRACE
"""
COMPOUND SHAPES
- Quick tip (mouse click)
- Multiple shapes, same location variables
- Movement
- Advanced: Make a function out of it
"""

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 530
HEIGHT = 280
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_1x = 147.5
circle_2x = 207.5
circle_3x = 267.5
circle_y = 206
circle_radius = 12.5
circle_speed = 3

square_1x = 105
square_2x = 165
square_3x = 225
square_y = 20
square_speed = 3

start_x = 25
start_y = 180
square_side = 2
start_speed = 3

key_held = False
key_pressed = ""

health = 3

# colour
start = (182,215,168)
goal = (182,215,168)
block = (234,153,153)
heart = (224,102,102) 
line = (0,0,0)
red = (255, 66, 72)
green = (73, 175, 2)

# boarder ract
boarder_rect1 = pygame.Rect(0, 170, 15, HEIGHT - 170)
boarder_rect2 =  pygame.Rect(15, 260, 140 - 15, HEIGHT - 260)
boarder_rect3 =  pygame.Rect(140, 220, 200, HEIGHT - 220)
boarder_rect4 =  pygame.Rect(340, 55, 15, HEIGHT - 55)
boarder_rect5 =  pygame.Rect(355, 100, 40, HEIGHT - 100)
boarder_rect6 =  pygame.Rect(395, 150, 65, HEIGHT - 150)
boarder_rect7 =  pygame.Rect(0, 0, 55, 170)
boarder_rect8 =  pygame.Rect(55, 0, 45, 220)
boarder_rect9 =  pygame.Rect(100, 0, 290, 20)
boarder_rect10 =  pygame.Rect(390, 0, 35, 70)
boarder_rect11 =  pygame.Rect(425, 0, 35, 120)
boarder_rect_list = [boarder_rect1, boarder_rect2, boarder_rect3, boarder_rect4, boarder_rect5, boarder_rect6,  boarder_rect7,  boarder_rect8,  boarder_rect9,  boarder_rect10,  boarder_rect11]

# ---------------------------
def heart1():
    pygame.draw.circle(screen, heart, (410, 240), 8, 0)
    pygame.draw.circle(screen, heart, (422, 240), 8, 0)
    pygame.draw.polygon(screen, heart, [[410, 245], [422, 245], [416, 255]], 0)

def heart2():
    pygame.draw.circle(screen, heart, (445, 240), 8, 0)
    pygame.draw.circle(screen, heart, (457, 240), 8, 0)
    pygame.draw.polygon(screen, heart, [[445, 245], [457, 245], [451, 255]], 0)

def heart3():
    pygame.draw.circle(screen, heart, (480, 240), 8, 0)
    pygame.draw.circle(screen, heart, (492, 240), 8, 0)
    pygame.draw.polygon(screen, heart, [[480, 245], [492, 245], [486, 255]], 0)

def back_to_start():
    global start_x, start_y, health
    start_x = 25
    start_y = 180
    health -= 1

def collision_check():
    global  start_x, start_y, player_rect

    for square_pos in [(square_1x, square_y), (square_2x, square_y), (square_3x, square_y)]:
        square_rect = pygame.Rect(square_pos[0], square_pos[1], 25, 25)
        if player_rect.colliderect(square_rect):
            back_to_start()
    
    for circle_pos in [(circle_1x, circle_y), (circle_2x, circle_y), (circle_3x, circle_y)]:
        circle_rect = pygame.Rect(circle_pos[0], circle_pos[1], circle_radius, circle_radius)
        if player_rect.colliderect(circle_rect):
            back_to_start()
    
    rectangle_rect = pygame.Rect(285, 40, 25, 150)
    if player_rect.colliderect(rectangle_rect):
        back_to_start()
    
    for boarder_rect in boarder_rect_list:
        if player_rect.colliderect(boarder_rect):
            if key_pressed == "left":
                start_x += start_speed*2
            elif key_pressed == "right":
                start_x -= start_speed*2
            elif key_pressed == "up":
                start_y += start_speed*2
            elif key_pressed == "down":
                start_y -= start_speed*2

def end_game():
    global start_speed, square_speed, circle_speed
    start_speed = 0
    square_speed = 0
    circle_speed = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or  event.key == pygame.K_DOWN:
                key_held = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                key_held = False

    # keyboard movement (move player if an arrow key is being held down)
    if key_held:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            key_pressed = "left"
            start_x -= start_speed
        elif keys[pygame.K_RIGHT]:
            key_pressed = "right"
            start_x += start_speed
        elif keys[pygame.K_UP]:
            key_pressed = "up"
            start_y -= start_speed
        elif keys[pygame.K_DOWN]:
            key_pressed = "down"
            start_y += start_speed

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    circle_y += circle_speed
    square_y += square_speed
    player_rect = pygame.Rect(start_x, start_y, 22, 22)

    collision_check()

    # DRAWING
    screen.fill("#cfe2f3")  # always the first drawing command

    # start
    pygame.draw.rect(screen, start, [0, 100, 70, 70], 0)
    pygame.draw.rect(screen, line, [0, 100, 70, 70], 1)

    # goal
    goal_rect = pygame.draw.rect(screen, goal, [460, 100, 70, 70], 0)
    pygame.draw.rect(screen, line, [460, 100, 70, 70], 1)

    # start block
    start_block = pygame.draw.rect(screen, start, [start_x, start_y, 22, 22], 0)
    start_block = pygame.draw.rect(screen, line, [start_x, start_y, 22, 22], 1)

    # line
    line_1 = pygame.draw.line(screen, line, [15, 170], [15, 260], 1)
    line_2 = pygame.draw.line(screen, line, [55, 170], [55, 220], 1)
    line_3 = pygame.draw.line(screen, line, [15, 260], [140, 260], 1)
    line_4 = pygame.draw.line(screen, line, [55, 220], [100, 220], 1)
    line_5 = pygame.draw.line(screen, line, [100, 220], [100, 20], 1)
    line_6 = pygame.draw.line(screen, line, [100, 20], [390, 20], 1)
    line_7 = pygame.draw.line(screen, line, [390, 20], [390, 70], 1)
    line_8 = pygame.draw.line(screen, line, [390, 70], [425, 70], 1)
    line_9 = pygame.draw.line(screen, line, [425, 70], [425, 120], 1)
    line_10 = pygame.draw.line(screen, line, [425, 120], [460, 120], 1)
    line_11 = pygame.draw.line(screen, line, [140, 260], [140, 220], 1)
    line_12 = pygame.draw.line(screen, line, [140, 220], [340, 220], 1)
    line_13 = pygame.draw.line(screen, line, [340, 220], [340, 55], 1)
    line_14 = pygame.draw.line(screen, line, [340, 55], [355, 55], 1)
    line_15 = pygame.draw.line(screen, line, [355, 55], [355, 100], 1)
    line_16 = pygame.draw.line(screen, line, [355, 100], [395, 100], 1)
    line_17 = pygame.draw.line(screen, line, [395, 100], [395, 150], 1)
    line_18 = pygame.draw.line(screen, line, [395, 150], [460, 150], 1)

    # deadly blocks (squares)
    if square_y < 22 and square_y > 195:
        square_speed = -square_speed
    pygame.draw.rect(screen, block, [square_1x, square_y, 25, 25], 0)

    if square_y < 22 or square_y > 195:
        square_speed = -square_speed
    pygame.draw.rect(screen, line, [square_1x, square_y, 25, 25], 1)

    if square_y < 22 or square_y > 195:
        square_speed = +square_speed
    pygame.draw.rect(screen, block, [square_2x, square_y, 25, 25], 0)

    if square_y < 22 or square_y > 195:
        square_speed = +square_speed
    pygame.draw.rect(screen, line, [square_2x, square_y, 25, 25], 1)

    if square_y < 22 or square_y > 195:
        square_speed = +square_speed
    pygame.draw.rect(screen, block, [square_3x, square_y, 25, 25], 0)

    if square_y < 22 or square_y > 195:
        square_speed = +square_speed
    pygame.draw.rect(screen, line, [square_3x, square_y, 25, 25], 1)

    # # deadly blocks (circles)
    if circle_y < 35 or circle_y > 206:
        circle_speed = -circle_speed
    pygame.draw.circle(screen, block, (circle_1x, circle_y), circle_radius, 0)

    if circle_y < 35 or circle_y > 206:
        circle_speed = +circle_speed
    pygame.draw.circle(screen, line, (circle_1x, circle_y), circle_radius, 1)

    if circle_y < 35 or circle_y > 208:
        circle_speed = -circle_speed
    pygame.draw.circle(screen, block, (circle_2x, circle_y), circle_radius, 0)

    if circle_y < 35 or circle_y > 208:
        circle_speed = +circle_speed
    pygame.draw.circle(screen, line, (circle_2x, circle_y), circle_radius, 1)

    if circle_y < 35 or circle_y > 208:
        circle_speed = -circle_speed
    pygame.draw.circle(screen, block, (circle_3x, circle_y), circle_radius, 0)

    if circle_y < 35 or circle_y > 208:
        circle_speed = +circle_speed
    pygame.draw.circle(screen, line, (circle_3x, circle_y), circle_radius, 1)

    # deadly blocks (rectangle)
    pygame.draw.rect(screen, block, [285, 40, 25, 150], 0)
    pygame.draw.rect(screen, line, [285, 40, 25, 150], 1)

    # font
    font=pygame.font.SysFont ('Calibri', 20, True, False)
    text=font.render("LEVEL 3", True, line)
    screen.blit (text, [430,25])

    font=pygame.font.SysFont ('Calibri', 18, True, False)
    text=font.render("START", True, line)
    screen.blit (text, [12,125])
 
    font=pygame.font.SysFont ('Calibri', 18, True, False)
    text=font.render("GOAL", True, line)
    screen.blit (text, [475,125])

    # endings + draw heart
    if health == 3:
        heart1()
        heart2()
        heart3()
    elif health == 2:
        heart1()
        heart2()
    elif health == 1:
        heart1()
    elif health == 0:
        font=pygame.font.SysFont ('Calibri', 25, True, False)
        text=font.render("Try Again", True, red)
        screen.blit (text, [230, 110])
    
    if player_rect.colliderect(goal_rect):
        font=pygame.font.SysFont ('Calibri', 25, True, False)
        text=font.render('Success!', True, green)
        screen.blit (text, [195, 110])
        end_game()

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
