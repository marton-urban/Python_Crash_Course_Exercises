import pygame


class Popeye:
    def __init__(self, popeye_game):
        self.screen = popeye_game.screen
        self.screen_rect = popeye_game.screen.get_rect()

        self.image = pygame.image.load('files/popeye.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
