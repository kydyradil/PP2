import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Clock and speed
clock = pygame.time.Clock()
initial_speed = 10

# Font
font = pygame.font.SysFont("Arial", 24)

# Snake initialization
snake = [(5, 5)]
direction = (1, 0)

# Food generation function with weight and timer
def generate_food():
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake:
            weight = random.randint(1, 3)  # Food weight between 1 and 3
            timer = random.randint(5, 10)  # Food disappears after 5-10 seconds
            return pos, weight, time.time(), timer  # Return food position, weight, start time, and timer

# Initial food generation
food, food_weight, food_start_time, food_timer = generate_food()

score = 0
level = 1
speed = initial_speed

# Load the sound for eating food
eat_sound = pygame.mixer.Sound("eat.wav")

# Game loop
running = True
while running:
    clock.tick(speed)

    # Check if food should disappear
    if time.time() - food_start_time > food_timer:
        food, food_weight, food_start_time, food_timer = generate_food()  # Regenerate food if time is up

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Control snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Move snake
    head = snake[-1]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # Check for wall collision
    if new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
        print("Game Over: Hit wall!")
        running = False
        continue

    # Check for self collision
    if new_head in snake:
        print("Game Over: Hit yourself!")
        running = False
        continue

    snake.append(new_head)

    # Check for food
    if new_head == food:
        score += food_weight  # Add food weight to score
        eat_sound.play()  # Play sound when food is eaten

        # Regenerate food with new weight and timer
        food, food_weight, food_start_time, food_timer = generate_food()

        # Level up every 4 points
        if score % 4 == 0:
            level += 1
            speed += 2  # Increase speed

    else:
        snake.pop(0)

    # Drawing
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw score and level
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
