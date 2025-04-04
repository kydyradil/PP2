import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False


k_elize = "k_elize.mp3"
simph = "simph.mp3"
piano = "piano.mp3"

current = k_elize

pygame.mixer.music.load(current)
pygame.mixer.music.play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(current)
                    pygame.mixer.music.play()
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
            elif event.key == pygame.K_d:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()

                if current == k_elize:
                    current = simph
                elif current == simph:
                    current = piano
                else:
                    current = k_elize

                pygame.mixer.music.load(current)
                pygame.mixer.music.play()
            elif event.key == pygame.K_a:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()

                if current == k_elize:
                    current = piano
                elif current == simph:
                    current = k_elize
                else:
                    current = simph

                pygame.mixer.music.load(current)
                pygame.mixer.music.play()
