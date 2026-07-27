import pygame

pygame.init()
window = pygame.display.set_mode(size=(600,480))


running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()