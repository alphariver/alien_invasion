import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        #加载飞船图像并获取矩形
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        #使飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性中存储一个浮点数
        self.x = float(self.rect.x)

        #移动标志
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #根据self.x更新rect对象
        self.rect.x = self.x


    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

    