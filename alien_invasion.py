import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from game_states import GameState
from button import Button
from scoreboard import ScoreBoard


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #游戏启动后处于活动状态
        self.active = False
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        #设置窗口标题
        pygame.display.set_caption("Alien Invasion litingzhang")

        #创建一个用于存储游戏统计信息的实例, 并创建记分
        self.stats = GameState(self)
        self.score_board = ScoreBoard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        
        self._create_stars()

        self._create_fleet()

        #创建按钮
        self.play_button = Button(self, "Play")

    def _create_stars(self):
        new_star = Star(self)

        self.stars.add(new_star)


    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = new_alien.x
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        #设置外星人的间距
        alien = Alien(self)
        #alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size

        #current_x = alien_width
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

        #self.aliens.add(alien)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_event(self):
        """响应键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                """
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                """
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.active:
            self.stats.reset_stats()
            self.score_board.prep_score()

            self.score_board.prep_ships()

            self.active = True

            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            #self.stars.empty()

            #创建一个新的外星人舰队，将飞船放置在屏幕的底部中间
            self.ship.center_ship()

            #还原游戏设置
            self.settings.initialize_dynamic_settings()
        



    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.stars.draw(self.screen)

        #显示得分
        self.score_board.show_score()

        if not self.active :
            self.play_button.draw_button()

        pygame.display.flip()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_bullet_alien_collision(self):
        #检查是否有子弹击中了外星人
    
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, self.settings.bullet_collision_dispear, True)

        if collisions :
            self.stats.score += self.settings.alien_score
            self.score_board.prep_score()
            self.score_board.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()


    def _update_bullets(self):

        self._check_bullet_alien_collision()

        #更新子弹的位置
        self.bullets.update()

        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _change_fleet_direction(self):
        #让整个舰队向下移动，同时修改左右移动的方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1  # 反转方向



    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _ship_hit(self):
        if self.stats.ship_left > 0 :
            #ship_left 减1
            self.stats.ship_left -= 1
            self.score_board.prep_ships()

            print(f"ship_left: {self.stats.ship_left}")

            #清空外星人列表、子弹列表、星星列表
            self.aliens.empty()
            self.bullets.empty()
            self.stars.empty()

            #将飞船放在屏幕的底部中央
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self.active = False



        



    def _update_aliens(self):
        #检查是否有外星人到达屏幕边缘
        self._check_fleet_edges()

        self.aliens.update()

        #检测外星人和飞船是否发生碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!!!")
            self._ship_hit()

        #检测是否有外星人到达了屏幕下边缘
        self._check_aliens_bottom()

    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #像飞船撞到了外人一样进行处理
                self._ship_hit()
                break



    def _update_stars(self):
        if pygame.sprite.spritecollideany(self.ship, self.stars):
            print("ship get star")
            self.stars.empty()
            self.settings.bullet_collision_dispear = False



    def run_game(self):
        while True:
            self._check_event()

            if self.active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_stars()

            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    #创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
