import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        #设置窗口标题
        pygame.display.set_caption("Alien Invasion litingzhang")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #更新窗口
            pygame.display.flip()


if __name__ == "__main__":
    #创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
