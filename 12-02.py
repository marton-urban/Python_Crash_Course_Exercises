import sys
import pygame


class GameCharacter:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Game Character")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                pygame.display.set_mode((1200, 700)).fill((255, 255, 255))
                pygame.display.flip()


if __name__ == '__main__':
    GameCharacter().run_game()
