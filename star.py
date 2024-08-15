import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        self.screen_rect = ai_game.screen.get_rect()

        #设置星星开始的位置
        self.rect.x = self.screen_rect.width - self.rect.width
        self.rect.y = self.screen_rect.height - self.rect.height


