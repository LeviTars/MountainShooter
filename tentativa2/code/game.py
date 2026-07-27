import pygame
from code.menu import Menu
from code.const import WIN_HEIGHT, WIN_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        

        running = True
        while running:

            menu = Menu(self.window)
            menu.run()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
