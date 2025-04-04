import pygame

pygame.init()


screen = pygame.display.set_mode((500, 500))
ball_x = 25
ball_y = 25
ball_radius = 25
ball_speed = 20
ball_color = (255, 0, 0)
background_color = (255, 255, 255)
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y >= ball_radius + ball_speed:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y <= 500 - ball_radius - ball_speed:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x >= ball_radius + ball_speed:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x <= 500 - ball_radius - ball_speed:
        ball_x += ball_speed

    screen.fill(background_color)
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)
