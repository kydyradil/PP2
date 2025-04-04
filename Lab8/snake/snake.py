import pygame
import random

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

# Food generation function
def generate_food():
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake:
            return pos

food = generate_food()
score = 0
level = 1
speed = initial_speed

# Load the sound for eating food
eat_sound = pygame.mixer.Sound("eat.wav")  

# Game loop
running = True
while running:
    clock.tick(speed)
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
        score += 1
        food = generate_food()

        # Play the sound when snake eats food
        eat_sound.play()

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

