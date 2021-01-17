import sys
import pygame
from popeye import Popeye


class PopeyeGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Popeye")

        self.popeye = Popeye(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.popeye.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    PopeyeGame().run_game()
