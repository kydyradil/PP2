import pygame
import random

# initialization 
pygame.init()

# window of player
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# uses for colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# shape of player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 100
player_speed = 5

# shape of enemy
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = -50
enemy_speed = 3

# coin
coin_size = 20
coins = []
coin_weights = [1, 2, 3]  # Разные веса монет
collected_coins = 0
speed_increase_threshold = 5  # Увеличение скорости врага после N монет

# shrift
font = pygame.font.Font(None, 36)

# main cycle 
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # events 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # control player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # motion of enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -50
        enemy_x = random.randint(0, WIDTH - enemy_size)
    
    # generate coins
    if random.randint(1, 100) > 98:
        coins.append([random.randint(0, WIDTH - coin_size), -20, random.choice(coin_weights)])
    
    # motion of coins
    for coin in coins[:]:
        coin[1] += 3
        if coin[1] > HEIGHT:
            coins.remove(coin)
    
    # checking for coins
    for coin in coins[:]:
        if player_x < coin[0] < player_x + player_size and player_y < coin[1] < player_y + player_size:
            collected_coins += coin[2]  # Добавляем вес монеты
            coins.remove(coin)
            
            # improve speed of enemy
            if collected_coins % speed_increase_threshold == 0:
                enemy_speed += 1
    
    # objects
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, (0, 0, 255), (enemy_x, enemy_y, enemy_size, enemy_size))
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0] + coin_size // 2, coin[1] + coin_size // 2), coin_size // 2)
    
    # uses for score
    score_text = font.render(f"Coins: {collected_coins}", True, (0, 0, 0))
    screen.blit(score_text, (WIDTH - 150, 20))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()

мой вариант 
# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turbo Drift")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Player attributes
car_size = 55
car_x = WIDTH // 2 - car_size // 2
car_y = HEIGHT - 120
car_speed = 6

# Opponent attributes
rival_size = 55
rival_x = random.randint(0, WIDTH - rival_size)
rival_y = -60
rival_speed = 4

# Coin attributes
coin_size = 25
coins = []
coin_values = [1, 3, 5]  # Different point values
score = 0
speed_threshold = 6  # Speed boost after collecting N coins

# Font setup
font = pygame.font.Font(None, 38)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_size:
        car_x += car_speed
    
    # Opponent movement
    rival_y += rival_speed
    if rival_y > HEIGHT:
        rival_y = -60
        rival_x = random.randint(0, WIDTH - rival_size)
    
    # Random coin generation with varied rates
    if random.randint(1, 150) > 145:  # Slightly adjusted probability
        coins.append([random.randint(0, WIDTH - coin_size), -25, random.choice(coin_values)])
    
    # Coin movement
    for coin in coins[:]:
        coin[1] += 5  # Faster movement
        if coin[1] > HEIGHT:
            coins.remove(coin)
    
    # Coin collection check
    for coin in coins[:]:
        if car_x < coin[0] < car_x + car_size and car_y < coin[1] < car_y + car_size:
            score += coin[2]  # Add coin value to score
            coins.remove(coin)
            
            # Increase opponent speed at certain thresholds
            if score % speed_threshold == 0:
                rival_speed += 1
    
    # Draw objects
    pygame.draw.rect(screen, GREEN, (car_x, car_y, car_size, car_size))
    pygame.draw.rect(screen, PURPLE, (rival_x, rival_y, rival_size, rival_size))
    for coin in coins:
        pygame.draw.circle(screen, ORANGE, (coin[0] + coin_size // 2, coin[1] + coin_size // 2), coin_size // 2)
    
    # Display score
    score_display = font.render(f"Coins: {score}", True, (0, 0, 0))
    screen.blit(score_display, (WIDTH - 160, 20))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()

