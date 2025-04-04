import pygame
import math

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

# Clock
clock = pygame.time.Clock()

# Function to draw a square
def draw_square(screen, color, position, size):
    # A square has 4 sides, all equal
    rect = pygame.Rect(position[0], position[1], size, size)
    pygame.draw.rect(screen, color, rect)

# Function to draw a right triangle
def draw_right_triangle(screen, color, position, base, height):
    # Define the points of the right triangle
    p1 = position
    p2 = (position[0] + base, position[1])  # Bottom right
    p3 = (position[0], position[1] - height)  # Top left
    points = [p1, p2, p3]
    pygame.draw.polygon(screen, color, points)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(screen, color, position, size):
    # Calculate the height of an equilateral triangle using Pythagorean theorem
    height = math.sqrt(3) * size / 2
    p1 = position  # Bottom left corner
    p2 = (position[0] + size, position[1])  # Bottom right corner
    p3 = (position[0] + size / 2, position[1] - height)  # Top point
    points = [p1, p2, p3]
    pygame.draw.polygon(screen, color, points)

# Function to draw a rhombus
def draw_rhombus(screen, color, position, size):
    # Rhombus vertices are determined by half-width and half-height of the diagonal
    half_diag = size / math.sqrt(2)
    p1 = (position[0], position[1] - half_diag)  # Top
    p2 = (position[0] + half_diag, position[1])  # Right
    p3 = (position[0], position[1] + half_diag)  # Bottom
    p4 = (position[0] - half_diag, position[1])  # Left
    points = [p1, p2, p3, p4]
    pygame.draw.polygon(screen, color, points)

# Main function to run the game
def main():
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

        # Draw shapes based on the selected mode
        position = (200, 200)  # Starting position for drawing
        size = 100  # Size for the shapes

        if mode == "square":
            draw_square(screen, RED, position, size)
        elif mode == "right_triangle":
            draw_right_triangle(screen, GREEN, position, size, size)
        elif mode == "equilateral_triangle":
            draw_equilateral_triangle(screen, WHITE, position, size)
        elif mode == "rhombus":
            draw_rhombus(screen, RED, position, size)

        pygame.display.flip()  # Update the display

        clock.tick(60)  # Limit the frame rate to 60 FPS

    pygame.quit()

# Run the program
main()
