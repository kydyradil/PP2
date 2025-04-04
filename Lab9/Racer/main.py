# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialization
pygame.init()

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables
FPS = 60
FramePerSec = pygame.time.Clock()
SPEED = 5
SCORE = 0
COIN = 0
COIN_SPEEDUP_INTERVAL = 5  # Increase speed every 5 collected coins

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading and scaling images
street = pygame.image.load("street.png")
street = pygame.transform.scale(street, (400, 600))

player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (40, 80))

enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (40, 80))

coin_img = pygame.image.load("coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Loading sounds
crashsound = pygame.mixer.Sound("crashsound.wav")
jingle = pygame.mixer.Sound("jingle.mp3")

# Classes
class Enemy(pygame.sprite.Sprite):
    # Enemy class, moves downward on the screen
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    # Player class controlled with arrow keys
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    # Coin class with random weight
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.weight = random.randint(1, 3)  # Coin weight from 1 to 3
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        # Respawn coin with new weight
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.weight = random.randint(1, 3)

# Creating objects
player = Player()
enemy = Enemy()
coin1 = Coin()
coin2 = Coin()

# Groups
enemies = pygame.sprite.Group()
enemies.add(enemy)

coins = pygame.sprite.Group()
coins.add(coin1)
coins.add(coin2)

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, coin1, coin2)

# Timer to increase speed over time
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(street, (0, 0))

    # Show score and collected coins
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_text = font_small.render(f"Coins: {COIN}", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    # Move and draw all entities
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Collision with enemy
    if pygame.sprite.spritecollideany(player, enemies):
        crashsound.play()
        time.sleep(1)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision with coins
    for coin in coins:
        if coin.rect.colliderect(player.rect):
            jingle.play()
            COIN += coin.weight  # Add coin weight
            coin.respawn()

            # Increase speed after collecting N coins
            if COIN % COIN_SPEEDUP_INTERVAL == 0:
                SPEED += 1
            break

    pygame.display.update()
    FramePerSec.tick(FPS)
