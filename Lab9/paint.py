import pygame
import math

"""
Paint-like application where you can draw different shapes with color options.

Control the drawing with the following keys:
- Y, B, W, D, G to change colors (Yellow, Blue, White, Red, Green respectively).
- Click LMB to assign borders for figures.
- S to draw a square.
- T to draw a right triangle.
- E to draw an equilateral triangle.
- R to draw a rhombus.
- Press 'Esc' to exit the application.
"""

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Shapes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Default color
current_color = RED

# Clock
clock = pygame.time.Clock()

# Function to draw a square
def draw_square(screen, color, position, size):
    rect = pygame.Rect(position[0], position[1], size, size)
    pygame.draw.rect(screen, color, rect)

# Function to draw a right triangle
def draw_right_triangle(screen, color, position, base, height):
    p1 = position
    p2 = (position[0] + base, position[1])  # Bottom right
    p3 = (position[0], position[1] - height)  # Top left
    points = [p1, p2, p3]
    pygame.draw.polygon(screen, color, points)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(screen, color, position, size):
    height = math.sqrt(3) * size / 2
    p1 = position  # Bottom left corner
    p2 = (position[0] + size, position[1])  # Bottom right corner
    p3 = (position[0] + size / 2, position[1] - height)  # Top point
    points = [p1, p2, p3]
    pygame.draw.polygon(screen, color, points)

# Function to draw a rhombus
def draw_rhombus(screen, color, position, size):
    half_diag = size / math.sqrt(2)
    p1 = (position[0], position[1] - half_diag)  # Top
    p2 = (position[0] + half_diag, position[1])  # Right
    p3 = (position[0], position[1] + half_diag)  # Bottom
    p4 = (position[0] - half_diag, position[1])  # Left
    points = [p1, p2, p3, p4]
    pygame.draw.polygon(screen, color, points)

# Main function to run the game
def main():
    global current_color
    running = True
    mode = "square"  # Default shape mode

    while running:
        screen.fill(BLACK)  # Clear screen before drawing

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Press 'S' to draw a square
                    mode = "square"
                elif event.key == pygame.K_t:  # Press 'T' to draw a right triangle
                    mode = "right_triangle"
                elif event.key == pygame.K_e:  # Press 'E' to draw an equilateral triangle
                    mode = "equilateral_triangle"
                elif event.key == pygame.K_r:  # Press 'R' to draw a rhombus
                    mode = "rhombus"
                elif event.key == pygame.K_y:  # Press 'Y' to change to yellow
                    current_color = YELLOW
                elif event.key == pygame.K_b:  # Press 'B' to change to blue
                    current_color = BLUE
                elif event.key == pygame.K_w:  # Press 'W' to change to white
                    current_color = WHITE
                elif event.key == pygame.K_d:  # Press 'D' to change to red
                    current_color = RED
                elif event.key == pygame.K_g:  # Press 'G' to change to green
                    current_color = GREEN

        # Draw shapes based on the selected mode
        position = (200, 200)  # Starting position for drawing
        size = 100  # Size for the shapes

        if mode == "square":
            draw_square(screen, current_color, position, size)
        elif mode == "right_triangle":
            draw_right_triangle(screen, current_color, position, size, size)
        elif mode == "equilateral_triangle":
            draw_equilateral_triangle(screen, current_color, position, size)
        elif mode == "rhombus":
            draw_rhombus(screen, current_color, position, size)

        pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit the frame rate to 60 FPS

    pygame.quit()

# Run the program
main()
