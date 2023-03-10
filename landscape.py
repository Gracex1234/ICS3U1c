"""
COMPOUND SHAPES
- Quick tip (mouse click)
- Multiple shapes, same location variables
- Movement
- Advanced: Make a function out of it
"""

import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

star_list=[]
for i in range(50):
  x=random.randrange(0,700)
  y=random.randrange(0,400)
  star_list.append([x,y])
# ---------------------------
# Initialize global variables

smoke_1x = 350
smoke_1y = 120
smoke_1radius = 7
smoke_2x = 361
smoke_2y = 123
smoke_2radius = 7
smoke_3x = 358
smoke_3y = 114
smoke_3radius = 5
smoke_4x = 397
smoke_4y = 83
smoke_4radius = 5
smoke_5x = 388
smoke_5y = 87
smoke_5radius = 6
smoke_6x = 397
smoke_6y = 93
smoke_6radius = 7
smoke_7x = 368
smoke_7y = 57
smoke_7radius = 5
smoke_8x = 361
smoke_8y = 63
smoke_8radius = 5
smoke_9x = 368
smoke_9y = 64
smoke_9radius = 5
smoke_10x = 413
smoke_10y = 48
smoke_10radius = 4
smoke_11x = 408
smoke_11y = 50
smoke_11radius = 4
smoke_12x = 412
smoke_12y = 53
smoke_12radius = 4
smoke_x_speed = 0.5

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
    screen.fill("#000000")  # always the first drawing command

    wall = (240, 240, 240)
    top_wall = (214, 214, 214)
    bottom = (160, 134, 121)
    bottom_2 = (139, 108, 92)
    ground = (221, 225, 131)
    building_1 = (210, 247, 255)
    door_1 = (207, 114, 113)
    window = (0,0,0)
    house = (253, 223, 134)
    door_2 = (209, 136, 111)
    roof = (250, 70, 78)
    chimney = (201, 128, 84)
    building_2 = (227, 100, 94)
    door_3 = (228, 190, 158)
    bush = (121, 199, 161)
    flower = (255,255,255)
    smoke = (255,255,255) 
    body = (255,255,255) 
    eyes = (0,0,0)
    lip = (255, 0, 0)
    button = (0,0,0)
    outside_door = (0,0,0)
    window_2 = (255,255,255) 
    window_change = (253, 223, 139)
    snow = (255, 255, 255)
         
    # bottom
    pygame.draw.rect(screen, bottom, [0, 300, 640, 80], 0)
    pygame.draw.rect(screen, bottom_2, [0, 300, 640, 15], 0)
    # wall
    pygame.draw.rect(screen, wall, [0, 0, 180, 300], 0)
    pygame.draw.rect(screen, wall, [460, 0, 180, 300], 0)
    pygame.draw.rect(screen, wall, [0, 0, 640, 40], 0)
    pygame.draw.rect(screen, top_wall, [0, 0, 640, 25], 0)
    # ground
    pygame.draw.rect(screen, ground, [180, 250, 280, 50], 0)
        
    # building_1
    pygame.draw.rect(screen, building_1, [180, 100, 80, 150], 0)
    # window_1
    pygame.draw.rect(screen, window, [185, 115, 15, 20], 0)
    pygame.draw.rect(screen, window, [235, 115, 15, 20], 0)
    pygame.draw.rect(screen, window, [185, 150, 15, 20], 0)
    pygame.draw.rect(screen, window, [235, 150, 15, 20], 0)
    pygame.draw.rect(screen, window, [185, 185, 15, 20], 0)
    pygame.draw.rect(screen, window, [235, 185, 15, 20], 0)
    # door_1
    pygame.draw.rect(screen, door_1, [210, 215, 20, 35], 0)

    # house
    pygame.draw.rect(screen, house, [270, 190, 100, 60], 0)
    # door_2
    pygame.draw.rect(screen, door_2, [310, 220, 20, 30], 0)
    # window_2
    pygame.draw.rect(screen, window, [285, 220, 15, 20], 0)
    pygame.draw.rect(screen, window, [340, 220, 15, 20], 0)
    # chimney
    pygame.draw.rect(screen, chimney, [340, 150, 13, 30], 0)
    # roof
    pygame.draw.polygon(screen, roof, [[320,150], [270,190], [370, 190]], 0)

    # building_2
    pygame.draw.rect(screen, building_2, [380, 140, 80, 110], 0) 
    # window_3
    pygame.draw.rect(screen, window, [390, 150, 15, 20], 0)
    pygame.draw.rect(screen, window, [390, 180, 15, 20], 0)
    pygame.draw.rect(screen, window, [390, 210, 15, 20], 0)
    pygame.draw.rect(screen, window, [420, 150, 15, 20], 0)
    pygame.draw.rect(screen, window, [420, 180, 15, 20], 0)
    pygame.draw.rect(screen, window, [450, 150, 10, 20], 0)
    pygame.draw.rect(screen, window, [450, 180, 10, 20], 0)
    pygame.draw.rect(screen, window, [450, 210, 10, 20], 0)
    # door_3
    pygame.draw.rect(screen, door_3, [418, 210, 20, 40], 0)
    # bush    
    pygame.draw.circle(screen, bush, [260, 236], 7, 0)
    pygame.draw.circle(screen, bush, [257, 246], 7, 0)
    pygame.draw.circle(screen, bush, [267, 245], 7, 0)
    pygame.draw.circle(screen, bush, [375, 236], 7, 0)
    pygame.draw.circle(screen, bush, [370, 247], 7, 0)
    pygame.draw.circle(screen, bush, [381.5, 245], 7, 0)
    # flower
    pygame.draw.circle(screen, flower, [258, 235], 2, 0)
    pygame.draw.circle(screen, flower, [260, 246], 2, 0)
    pygame.draw.circle(screen, flower, [267, 243], 2, 0)
    # flower_2
    pygame.draw.circle(screen, flower, [376, 236], 2, 0)
    pygame.draw.circle(screen, flower, [370, 244], 2, 0)
    pygame.draw.circle(screen, flower, [383, 243], 2, 0) 

    # GAME STATE UPDATES
    smoke_1x += smoke_x_speed
    smoke_2x += smoke_x_speed
    smoke_3x += smoke_x_speed
    smoke_4x += smoke_x_speed
    smoke_5x += smoke_x_speed
    smoke_6x += smoke_x_speed
    smoke_7x += smoke_x_speed
    smoke_8x += smoke_x_speed
    smoke_9x += smoke_x_speed
    smoke_10x += smoke_x_speed
    smoke_11x += smoke_x_speed
    smoke_12x += smoke_x_speed
        
    # BOUNCE
    if smoke_1x > 460 or smoke_1x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_1x, smoke_1y), smoke_1radius)

    if smoke_2x > 460 or smoke_2x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_2x, smoke_2y), smoke_2radius)

    if smoke_3x > 460 or smoke_3x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_3x, smoke_3y), smoke_3radius)

    if smoke_4x > 460 or smoke_4x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_4x, smoke_4y), smoke_4radius)

    if smoke_5x > 460 or smoke_5x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_5x, smoke_5y), smoke_5radius)

    if smoke_6x > 460 or smoke_6x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_6x, smoke_6y), smoke_6radius)

    if smoke_7x > 460 or smoke_7x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_7x, smoke_7y), smoke_7radius)

    if smoke_8x > 460 or smoke_8x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_8x, smoke_8y), smoke_8radius)

    if smoke_9x > 460 or smoke_9x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_9x, smoke_9y), smoke_9radius)

    if smoke_10x > 460 or smoke_10x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_10x, smoke_10y), smoke_10radius)

    if smoke_11x > 460 or smoke_11x < 320:
        smoke_x_speed = -smoke_x_speed
    pygame.draw.circle(screen, smoke, (smoke_11x, smoke_11y), smoke_11radius)

    if smoke_12x > 460 or smoke_12x < 320:
        smoke_x_speed = -smoke_x_speed            
    pygame.draw.circle(screen, smoke, (smoke_12x, smoke_12y), smoke_12radius)

    # outside_door_1
    pygame.draw.rect(screen, outside_door, [85, 40, 95, 260], 0)
    # outside_window_1
    pygame.draw.rect(screen, window_2, [100, 40, 5, 260], 0)
    pygame.draw.rect(screen, window_2, [120, 60, 45, 70], 0)
    pygame.draw.rect(screen, window_2, [120, 150, 45, 35], 0)
    pygame.draw.rect(screen, window_2, [120, 200, 45, 80], 0)
    pygame.draw.circle(screen, body, [92.5, 195], 2.5, 0)    

    # outside_door_2
    pygame.draw.rect(screen, outside_door, [460, 40, 95, 260], 0)
    # outside_window_2
    pygame.draw.rect(screen, window_2, [535, 40, 5, 260], 0)
    pygame.draw.rect(screen, window_2, [475, 60, 45, 70], 0)
    pygame.draw.rect(screen, window_2, [475, 150, 45, 35], 0)
    pygame.draw.rect(screen, window_2, [475, 200, 45, 80], 0)
    pygame.draw.circle(screen, body, [547.5, 195], 2.5, 0) 
    
    # snowman
    pygame.draw.circle(screen, body, [320, 220], 8, 0) 
    pygame.draw.circle(screen, body, [320, 230], 10, 0)    
    pygame.draw.circle(screen, body, [320, 245], 12, 0)    
    # snowman_eyes
    pygame.draw.rect(screen, eyes, [315, 215, 3, 3], 0)
    pygame.draw.rect(screen, eyes, [322, 215, 3, 3], 0)
    # snowman_lip
    pygame.draw.rect(screen, lip, [318, 220, 4, 4], 0)
    # snowman_button
    pygame.draw.circle(screen, button, [320, 230], 2, 0)    
    pygame.draw.circle(screen, button, [320, 240], 2, 0)    
    pygame.draw.circle(screen, button, [320, 250], 2, 0)    

    pygame.draw.circle(screen, body, [215, 230], 2, 0)
    pygame.draw.circle(screen, window, [423, 228], 2, 0)
 
    for item in star_list:
     item[1]+=1
     pygame.draw.circle(screen,snow,item,2)
     if item[1]>500:
       item[1]=random.randrange(-20,-5)
       item[0]=random.randrange(700) 
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()
