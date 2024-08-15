class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 12.0
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)

        #外星人设置
        self.alien_speed = 1.0
        #1代表向右，-1代表向左移动
        self.fleet_direction = 1
        self.fleet_drop_speed = 20