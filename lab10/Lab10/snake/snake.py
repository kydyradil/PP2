import pygame
import random
import psycopg2
from config import load_config


level = 1
score = 0
coor_head = []
coor_body = []
coor_apple = []
value = 0
GAatS = True # Generate Apple at the Start (or use the one saved in user profile)
direc = "r"
next_dir = "r"
invincible = False # A variable for giving the player a chance to leave the newly-formed walls upon level progression
cheated = False # A variable for score-cheating

config = load_config()

def check_user(username):
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM users WHERE username = '{username}';")
            rows = cur.fetchall()
            if len(rows) == 0:
                cur.execute(f"INSERT INTO users(username, level, score, GAatS, direction) VALUES('{username}', 1, 0, True, 'r') RETURNING *")
                cur.execute(f"INSERT INTO coords(username, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, ax, ay) VALUES('{username}', 100, 100, 30, 100, 40, 100, 50, 100, 60, 100, 70, 100, 80, 100, 90, 100, 100, 100, 0, 0) RETURNING *")
        conn.commit()

def load_data(username):
    global level
    global score
    global coor_head
    global coor_body
    global coor_apple
    global value
    global GAatS
    global direc
    global next_dir
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
            row = cur.fetchone()
            level, score = row[1], row[2]
            GAatS = row[3]
            direc = row[4]
            next_dir = row[4]
            cur.execute(f"SELECT * FROM coords WHERE username = '{username}'")
            row = cur.fetchone()
            coor_head = [row[1], row[2]]
            coor_body = [[row[3], row[4]], [row[5], row[6]], [row[7], row[8]], 
                         [row[9], row[10]], [row[11], row[12]], [row[13], row[14]], 
                         [row[15], row[16]], [row[17], row[18]]]
            coor_apple = [row[19], row[20]]
            value = row[21]


def save_data(username):
    global level
    global score
    global coor_head
    global coor_body
    global coor_apple
    global value
    global direc
    c1, c, ca = coor_head, coor_body, coor_apple
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users SET (level, score, GAatS, direction) = ({level}, {score}, False, '{direc}') WHERE username = '{username}';")
            cur.execute(f"UPDATE coords SET (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9, ax, ay, av) = ({c1[0]}, {c1[1]}, {c[0][0]}, {c[0][1]}, {c[1][0]}, {c[1][1]}, {c[2][0]}, {c[2][1]}, {c[3][0]}, {c[3][1]}, {c[4][0]}, {c[4][1]}, {c[5][0]}, {c[5][1]}, {c[6][0]}, {c[6][1]}, {c[7][0]}, {c[7][1]}, {ca[0]}, {ca[1]}, {value}) WHERE username = '{username}';")
        conn.commit()

user = input("Enter your username: ")
check_user(user)
load_data(user)


'''
level, score = 1, 0
coor_head = [100, 100]
coor_body = [
    [30,100],
    [40,100],
    [50,100],
    [60,100],
    [70,100],
    [80,100],
    [90,100],
    [100,100]
]
'''
pygame.init()

#game variables
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
done = False

COLOR_BODY = (255, 255, 255)
COLOR_HEAD = (128,128,128)
COLOR_WALLS = (255, 216, 110)

record = 0 # a variable for keeping the count of the score collected and progressing in levels

#three walls variants
walls = []

#apple
eaten = False
COLOR = {1: (0, 255, 0), 2: (0, 0, 255), 3: (255, 0, 0)} # the apple's color now depends on its weight
def generate_apple():
    #appearance close to the walls and on top of the snake excluded
    global eaten 
    global width
    global height
    global coor_apple
    global value
    finished = True
    while True:
        apple_width, apple_height = random.randrange(1,width//10)*10, random.randrange(1,height//10)*10
        if apple_width in [0, 800, coor_body[0], coor_head[0]]: 
            finished = False
        elif apple_height in [0, 600, coor_body[1], coor_head[1]]: 
            finished = False
        else:
            for i in walls:
                if apple_width in range(i[0], i[2]):
                    finished = False
                elif apple_height in range(i[1], i[3]):
                    finished = False
        if finished: 
            break
        else:
            finished = True     
    coor_apple = [apple_width, apple_height]
    value = random.randint(1, 3) # randomly assigned weight of the apple
    eaten = False


if GAatS: generate_apple()

APPLE = pygame.USEREVENT + 1 # a gimmick event to be used in the timer below
timer = pygame.time.set_timer(APPLE, int(48000 / (value + level))) # apple's disappearance timer
INV = pygame.USEREVENT + 2 # invincibility event
PAUSE = False

def score_update(font, size, color):
    global score
    score_font = pygame.font.SysFont(font,size)
    score_render = score_font.render("Score: "+str(score),True,color)
    score_rect = score_render.get_rect()
    #level update included
    level_render = score_font.render("Level: "+str(level),True,color)
    level_rect = pygame.Rect(width - size * 5 - 1, 0, width - 1, size)


    screen.blit(score_render,score_rect)
    screen.blit(level_render, level_rect)

    pygame.display.update()

def game_over_message(font, size, color):
    global score
    global done
    game_over_font = pygame.font.SysFont(font,size)
    game_over_surface1 = game_over_font.render("Game Over, your final score: "+str(score)+";",True,color)
    game_over_surface2 = game_over_font.render("You reached level "+str(level),True,color)
    game_over_rect1, game_over_rect2 = pygame.Rect(100,100,200,200), pygame.Rect(100,200,400,400)
    screen.blit(game_over_surface1,game_over_rect1)
    screen.blit(game_over_surface2,game_over_rect2)
    pygame.display.update()
    pygame.time.delay(3000)
    done = True

while not done:
    pressed = pygame.key.get_pressed()
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    walls = []


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if PAUSE and event.key == pygame.K_s and ctrl_held:
                save_data(user)
            if event.key == pygame.K_g and ctrl_held: # A cheat for auto-eating apples
                cheated = True
            if event.key == pygame.K_SPACE:
                if PAUSE: 
                    PAUSE = False
                else: 
                    PAUSE = True
            if event.key == pygame.K_RIGHT:
                next_dir = "r"
            if event.key == pygame.K_LEFT:
                next_dir = "l"
            if event.key == pygame.K_UP:
                next_dir = "u"
            if event.key == pygame.K_DOWN:
                next_dir = "d"
        if event.type == APPLE:
            eaten = True
        if event.type == INV:
            if invincible:
                invincible = False
                COLOR_BODY = (255, 255, 255)
                COLOR_HEAD = (128,128,128)
            else:
                invincible = True
                COLOR_BODY = (66, 233, 245)
                COLOR_HEAD = (0, 167, 179)
    
    if PAUSE: continue

    for seg in coor_body[:-1]:
        if coor_head[0] == seg[0] and coor_head[1] == seg[1]:
            game_over_message("times new roman",44,(255,0,0))
    
    #additional check for the walls
    if not invincible:
        if coor_head[0] == 0 or coor_head[0] == 800 or coor_head[1] == 0 or coor_head[1] == 600:
            game_over_message("times new roman",44,(255,0,0))
        for i in walls:
            if coor_head[0] in range(i[0], i[2]) and coor_head[1] in range (i[1], i[3]):
                game_over_message("times new roman",44,(255,0,0))
                break

    screen.fill((0,0,0))
    #logic
    if next_dir == "r" and direc != "l":
        direc = "r"
    if next_dir == "l" and direc != "r":
        direc = "l"
    if next_dir == "u" and direc != "d":
        direc = "u"
    if next_dir == "d" and direc != "u":
        direc = "d"



    if direc == "r":
        coor_head[0] += 10
    if direc == "l":
        coor_head[0] -= 10
    if direc == "u":
        coor_head[1] -= 10
    if direc == "d":
        coor_head[1] += 10

    new_coor = [coor_head[0],coor_head[1]]
    coor_body.append(new_coor)
    coor_body.pop(0)

    if (coor_head[0] == coor_apple[0] and coor_head[1] == coor_apple[1]) or cheated:
        eaten = True
        score += value * 10
        if score - record >= 50: 
            level += 1
            record = score
            pygame.event.post(pygame.event.Event(INV))
            inv_timer = pygame.time.set_timer(INV, 2222, loops=1)
        cheated = False
    
    if eaten:
        generate_apple()
        timer = pygame.time.set_timer(APPLE, int(48000 / (value + level)))
        

    # drawing section
    if not eaten:
        pygame.draw.rect(screen,COLOR[value],pygame.Rect(coor_apple[0],coor_apple[1],10,10))

    for i in walls:
        pygame.draw.rect(screen, COLOR_WALLS, pygame.Rect(i[0], i[1], i[2] - i[0], i[3] - i[1]))

    for el in coor_body:
        pygame.draw.rect(screen,COLOR_BODY,pygame.Rect(el[0],el[1],10,10))
    
    pygame.draw.rect(screen,COLOR_HEAD,pygame.Rect(coor_head[0],coor_head[1],10,10))

    score_update("times new roman",20,(128,128,128))

    #tweaked the delay so that the game's speed increases along with the progression in levels
    pygame.time.delay(int(150 / level))

    pygame.display.flip()

pygame.quit()
