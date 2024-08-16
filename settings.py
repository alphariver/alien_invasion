class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船设置
        self.ship_speed = 6
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 18.0
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullet_collision_dispear = True

        #外星人设置
        #self.alien_speed = 1.0
        #1代表向右，-1代表向左移动
        self.fleet_direction = 1
        self.fleet_drop_speed = 20
        self.score_scale = 2

        #以什么速度加快游戏节奏
        self.speed_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed = 1.0
        #记分设置
        self.alien_score = 1

    def increase_speed(self):
        self.alien_speed *= self.speed_scale

        self.alien_score = int (self.alien_score * self.score_scale)
        print(self.alien_score)