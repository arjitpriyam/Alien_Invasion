import pygame

from pygame.sprite import Group
import time
from settings import Settings
import game_functions as gf
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from background import Background
from database import Database

class alien_invasion():

    def run_game(self,username):
        pygame.init()
        ai_settings = Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        play_button = Button(ai_settings, screen, "Play")
        stats = GameStats(ai_settings,username)
        sb = Scoreboard(ai_settings, screen, stats)
        bg_color = (230, 230, 230)
        db=Database()
        ship = Ship(ai_settings, screen)
        bg=Background(ai_settings,screen)
        bullet= Bullet(ai_settings, screen, ship)
        bullets = Group()
        aliens = Group()
        gf.create_fleet(ai_settings, screen, ship, aliens)
        while True:
            gf.check_events(ai_settings, screen, stats,sb, play_button, ship, aliens, bullet,bullets,db,username)
            if stats.game_active:
                ship.update(bullet)
                bullet.update(ai_settings, screen, ship,bullets)
                bullets.update(ai_settings, screen, ship,bullets)
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets,db,username)
                gf.update_aliens(ai_settings, screen, stats, sb, ship , aliens, bullets,db,username)
        #for bullet in bullets:
        #if bullet.rect.bottom <= 0:
        #    bullets.remove(bullet)
        #print(len(bullets))
            gf.update_screen(ai_settings, screen,stats,sb, ship, bullets,aliens,play_button,bg)

#al=alien_invasion()
#al.run_game()
