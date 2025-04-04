import pygame

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    else:
        color = (255, 255, 255)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = "blue"
    points = []

    running = True
    while running:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or (event.key == pygame.K_w and ctrl_held) or (event.key == pygame.K_F4 and alt_held):
                    running = False
                elif event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            elif event.type == pygame.MOUSEMOTION:
                position = event.pos
                if mode != 'eraser':
                    points.append(position)
                    points = points[-256:]
                else:
                    # Просто рисуем чёрным, но не сохраняем в points
                    if len(points) > 0:
                        drawLineBetween(screen, 0, points[-1], position, radius, mode)
                    points.append(position)
                    points = points[-1:]

        screen.fill((0, 0, 0))

        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
