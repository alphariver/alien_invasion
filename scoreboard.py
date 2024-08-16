import pygame.font

class ScoreBoard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #显示得分时的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #准备初始化得分图像
        self.prep_score()

        #准备最高分的图像
        self.prep_high_score()

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, 
                                                self.text_color, self.settings.bg_color)

        #将最高分放在屏幕顶部的左边
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = self.screen_rect.top + 20  # 20 pixels above the top edge of the screen.




    def prep_score(self):
        round_score = round(self.stats.score, -1)
        score_str = f"{round_score:,}"
        self.score_image = self.font.render(score_str, True, 
                                            self.text_color, self.settings.bg_color)
        
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()