import sys
import pygame

class PygameBlueWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption('Pygame Blue Window')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 255))
            pygame.display.flip()


if __name__ == '__main__':
    PygameBlueWindow().run_game()
