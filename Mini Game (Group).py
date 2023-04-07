import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

# Level 1: Emma Lee
# Level 2: Gisele Chan
# Level 3: Grace Ryu

import time

pygame.init()

WIDTH = 530
HEIGHT = 280
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

game = 0

# Intro
game_name = "Welcome to MOVING GEOMETRY!"
intro_text = "Move (arrow keys) to the light green area on the other side. Avoid anything red!"
start_text = "Press ENTER to start the game."
intro_font = pygame.font.SysFont('Calibri', 15)
game_name_surf = intro_font.render(game_name, True, (0, 0, 0))
intro_surf = intro_font.render(intro_text, True, (0, 0, 0))
start_surf = intro_font.render(start_text, True, (0, 0, 0))
game_name_rect = game_name_surf.get_rect(center=(WIDTH/2, HEIGHT/2 - 50))
intro_rect = intro_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
start_rect = start_surf.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))

square_side1 = 50
obstacle1_x = 0
obstacle2_x = WIDTH - square_side1
obstacle_speed = 5

player1_x = 0
player1_y = HEIGHT - square_side1
player1_speed = 5

game_font = pygame.font.SysFont('Calibri', 32)  # "Try Again" and "Success!" Text

# Level 2
block_1_x = 110
block_2_x = 200
block_3_x = 280
block_4_x = 370
block_y1 = 0
block_y2 = 220
player_block = 60
speed = 8
player_x = 0
player_y = HEIGHT - player_block
player_speed = 7
key_held = False
font = pygame.font.SysFont('Calibri', 32)
messagelist = ['try again', 'Success!']

# Level 3
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

# Colours
start = (182,215,168)
goal = (182,215,168)
block = (234,153,153)
heart = (224,102,102) 
line = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Border rect
border_rect1 = pygame.Rect(0, 170, 15, HEIGHT - 170)
border_rect2 =  pygame.Rect(15, 260, 140 - 15, HEIGHT - 260)
border_rect3 =  pygame.Rect(140, 220, 200, HEIGHT - 220)
border_rect4 =  pygame.Rect(340, 55, 15, HEIGHT - 55)
border_rect5 =  pygame.Rect(355, 100, 40, HEIGHT - 100)
border_rect6 =  pygame.Rect(395, 150, 65, HEIGHT - 150)
border_rect7 =  pygame.Rect(0, 0, 55, 170)
border_rect8 =  pygame.Rect(55, 0, 45, 220)
border_rect9 =  pygame.Rect(100, 0, 290, 20)
border_rect10 =  pygame.Rect(390, 0, 35, 70)
border_rect11 =  pygame.Rect(425, 0, 35, 120)
border_rect_list = [border_rect1, border_rect2, border_rect3, border_rect4, border_rect5, border_rect6,  border_rect7,  border_rect8,  border_rect9,  border_rect10,  border_rect11]

# ---------------------------
# Level 1
def show_intro():
    global game
    screen.fill((207,226,243))
    screen.blit(game_name_surf, game_name_rect)
    screen.blit(intro_surf, intro_rect)
    screen.blit(start_surf, start_rect)
    pygame.display.flip()

def restart_round1():
    global obstacle1_x, obstacle2_x, player1_x, player1_y
    obstacle1_x = 0
    obstacle2_x = WIDTH - square_side1
    player1_x = 0
    player1_y = HEIGHT - square_side1

# game_2
def restart_round2():
    # Move the player to the starting position
    global player_x, player_y
    player_x = 0
    player_y = HEIGHT - player_block
    
    # Reset the velocities of the moving blocks
    global moving_block_velocities
    import random
    moving_block_velocities = [random.randint(-5, 5) for _ in range(4)]

def collision():
    global game
    for block_pos in [(110, block_y1), (200, block_y2), (280, block_y1), (370, block_y2)]:
            block_rect = pygame.Rect(block_pos[0], block_pos[1], 60, 60)
            if player_rect.colliderect(block_rect):
                # Reset the player's block position (back to the starting block)
                restart_round2()
                # Show "try again" message 
                message = font.render(messagelist[0], True, (255, 0, 0))
                message_rect = message.get_rect(center=(WIDTH/2, HEIGHT/2))
                screen.blit(message, message_rect)
                pygame.display.flip()
                # for 2 seconds
                time.sleep(2)

    # collision with goal block
    goal_rect = pygame.Rect(WIDTH- player_block, 0, player_block, player_block)
    if player_rect.colliderect(goal_rect):
        # Reset the player's block position (back to the starting block)
        restart_round2()
        # Show "Success!" message for 2 seconds
        message = font.render(messagelist[1], True, (0, 255, 0))
        message_rect = message.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(message, message_rect)
        pygame.display.flip()
        # for 2 seconds
        time.sleep(2)
        game = 3

# game_3
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
    
    for border_rect in border_rect_list:
        if player_rect.colliderect(border_rect):
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
            elif event.key == pygame.K_RETURN:
                waiting = False
                game = 1
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                key_held = False

    # keyboard movement (move player if an arrow key is being held down)
    if game == 0:
        show_intro()
    
    elif game == 1:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player1_x > 0:
                player1_x -= player1_speed
        elif keys[pygame.K_RIGHT]:
            if player1_x < WIDTH - square_side1:
                player1_x += player1_speed
        elif keys[pygame.K_UP]:
            if player1_y > 0:
                player1_y -= player1_speed
        elif keys[pygame.K_DOWN]:
            if player1_y < HEIGHT - square_side1:
                player1_y += player1_speed

        # GAME STATE UPDATES    
        obstacle1_x += obstacle_speed # OBSTACLE1 MOVEMENT
        obstacle2_x -= obstacle_speed # OBSTACLE2 MOVEMENT

        if (obstacle1_x + square_side > WIDTH) or (obstacle1_x < 0): # OBSTACLE1 MOVEMENT
            obstacle_speed = - obstacle_speed
        elif (obstacle2_x + square_side > WIDTH) or (obstacle2_x < 0): # OBSTACLE2 MOVEMENT
            obstacle_speed = - obstacle_speed

        # COLLISION DETECTION
        player1_rect = pygame.Rect(player1_x, player1_y, square_side1, square_side1)
        obstacle1_rect = pygame.Rect(obstacle1_x, 77, square_side1, square_side1)
        obstacle2_rect = pygame.Rect(obstacle2_x, 155, square_side1, square_side1)

        if player1_rect.colliderect(obstacle1_rect) or player1_rect.colliderect(obstacle2_rect):
            restart_round1()
            # "TRY AGAIN" MESSAGE
            message = game_font.render("TRY AGAIN", True, (255, 0, 0))
            message_rect = message.get_rect(center=(WIDTH/2, HEIGHT/2))
            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 2000:
                screen.blit(message, message_rect)
                pygame.display.flip()
        else:
            # "SUCCESS" MESSAGE
            goal_rect = pygame.Rect(WIDTH-square_side, 0, square_side, square_side)
            if player1_rect.colliderect(goal_rect):
                message = game_font.render("SUCCESS", True, (0, 255, 0))
                message_rect = message.get_rect(center=(WIDTH/2, HEIGHT/2))
                start_time = pygame.time.get_ticks()
                while pygame.time.get_ticks() - start_time < 2000:
                    screen.blit(message, message_rect)
                    pygame.display.flip()
                game = 2

        # DRAWING
        screen.fill((207,226,243))

        level_font = pygame.font.SysFont ('Calibri', 20, True, False) # "LEVEL 1" text
        level_text = level_font.render("LEVEL 1", True, (0,0,0))
        screen.blit (level_text, [400,250])

        pygame.draw.rect(screen, ((182,215,168)), (0, HEIGHT - square_side1, square_side1, square_side1), 0) # STARTING POINT
        pygame.draw.rect(screen, ((0,0,0)), (0, HEIGHT - square_side1, square_side1, square_side1), 1)
        area_font = pygame.font.SysFont ('Calibri', 10, True, False) # "START"/"GOAL" text
        start_text = area_font.render("START", True, (0,0,0)) # "START" text
        screen.blit (start_text, [9,250])
        
        pygame.draw.rect(screen, ((182,215,168)), (WIDTH - square_side1, 0, square_side1, square_side1), 0) # GOAL
        pygame.draw.rect(screen, ((0,0,0)), (WIDTH - square_side1, 0, square_side1, square_side1), 1)
        goal_text = area_font.render("GOAL", True, (0,0,0)) # "GOAL" text
        screen.blit (goal_text, [492,20])

        pygame.draw.rect(screen, ((234,153,153)), (obstacle1_x, 77, square_side1, square_side1), 0) # OBSTACLE 1
        pygame.draw.rect(screen, ((0,0,0)), (obstacle1_x, 77, square_side1, square_side1), 1)

        pygame.draw.rect(screen, ((234,153,153)), (obstacle2_x, 155, square_side1, square_side1), 0) # OBSTACLE 2
        pygame.draw.rect(screen, ((0,0,0)), (obstacle2_x, 155, square_side1, square_side1), 1)

        pygame.draw.rect(screen, ((50,205,50)), (player1_x, player1_y, square_side1, square_side1), 0) # PLAYER
        pygame.draw.rect(screen, ((0,0,0)), (player1_x, player1_y, square_side1, square_side1), 1)

    elif game == 2:
        if key_held:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT]:
                player_x += player_speed
            elif keys[pygame.K_UP]:
                player_y -= player_speed
            elif keys[pygame.K_DOWN]:
                player_y += player_speed

        player_rect = pygame.Rect(player_x, player_y, player_block, player_block)
        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > WIDTH:
            player_rect.right = WIDTH
        if player_rect.top < 0:
            player_rect.top = 0
        if player_rect.bottom > HEIGHT:
            player_rect.bottom = HEIGHT

        # since we're keeping the player's block inside the screen, need to update the location of player x and y
        player_x = player_rect.x
        player_y = player_rect.y
        collision()

        # GAME STATE UPDATES
        # block movement (bouncing up and down)
        block_y1 += speed
        if (block_y1 + 60 > HEIGHT) or (block_y1 < 0):
            speed = - speed
        block_y1 = max(0, min(block_y1, HEIGHT - 60))

        block_y2 -= speed
        if (block_y2 + 60 > HEIGHT) or (block_y2 < 0):
            speed = - speed
            block_y2 = max(0, min(block_y2, HEIGHT - 60)) 

        # DRAWING
        screen.fill((207,226,243))  # always the first drawing command
        line = (0,0,0)
        start = (182, 215, 168)
        goal = (182, 215, 168)
        block = (234, 153, 153)
        player = (50,205,50)

        # start
        pygame.draw.rect(screen, start, [0, 200, 80, 80], 0)
        pygame.draw.rect(screen, line, [0, 200, 80, 80], 1)
        # blocks (1)
        pygame.draw.rect(screen, block, [block_1_x,block_y1,60,60],0)
        pygame.draw.rect(screen, line, [block_1_x,block_y1,60,60],1)
        # block (2)
        pygame.draw.rect(screen, block, [block_2_x,block_y2,60,60],0)
        pygame.draw.rect(screen, line, [block_2_x,block_y2,60,60],1)
        # block (3)
        pygame.draw.rect (screen,block, [block_3_x,block_y1,60,60],0)
        pygame.draw.rect (screen,line, [block_3_x,block_y1,60,60],1)
        # block (4)
        pygame.draw.rect (screen,block, [block_4_x,block_y2,60,60],0)
        pygame.draw.rect (screen,line, [block_4_x,block_y2,60,60],1)
        # player's block 
        pygame.draw.rect(screen, player, [player_x, player_y, player_block, player_block], 0)
        pygame.draw.rect (screen, line, [player_x, player_y, player_block, player_block],2)
        # goal
        pygame.draw.rect(screen, goal, [450, 0, 80, 80], 0)
        pygame.draw.rect(screen, line, [450,0,80, 80], 1)

    elif game == 3:
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

        player_rect = pygame.Rect(start_x, start_y, 22, 22)
        # GAME STATE UPDATES
        # All game math and comparisons happen here
        circle_y += circle_speed
        square_y += square_speed

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
            pygame.draw.rect(screen, start, [0, 100, 70, 70], 0)
            pygame.draw.rect(screen, line, [0, 100, 70, 70], 1)
            goal_rect = pygame.draw.rect(screen, goal, [460, 100, 70, 70], 0)
            pygame.draw.rect(screen, line, [460, 100, 70, 70], 1)
            font=pygame.font.SysFont ('Calibri', 25, True, False)
            text=font.render("Game Over", True, black)
            screen.blit (text, [230, 120])

        if player_rect.colliderect(goal_rect):
            pygame.draw.rect(screen, start, [0, 100, 70, 70], 0)
            pygame.draw.rect(screen, line, [0, 100, 70, 70], 1)
            goal_rect = pygame.draw.rect(screen, goal, [460, 100, 70, 70], 0)
            pygame.draw.rect(screen, line, [460, 100, 70, 70], 1)
            font=pygame.font.SysFont ('Calibri', 21, True, False)
            text=font.render('Congratulations! You finally finished the game!', True, black)
            screen.blit (text, [60, 120])
            end_game()

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
