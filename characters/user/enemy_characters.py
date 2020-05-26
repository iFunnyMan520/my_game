from game_field.field import *
import random


class Enemy:

    def __init__(self, display_enemy, image_enemy, x, y, width, height, level):
        self._display = display_enemy
        self._img = image_enemy
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.level = level

    def move(self):
        if self.y < display_width:
            self._display.blit(self._img, (self.x, self.y))
            if self.level == 1:
                self.y += 6
            elif self.level == 2:
                self.y += 7
            elif self.level == 3:
                self.y += 8
        else:
            self.y = 0
            self.x = random.randint(1, 8) * 100

    def destroy(self, bullets):
        for bullet in bullets:
            if self.y + self.height > bullet.y:
                if self.x <= (
                        bullet.x + bullet.width / 2) <= self.x + self.width:
                    pygame.mixer.Sound.play(enemies_kill_sound)
                    self.y = 0
                    self.x = random.randint(1, 8) * 100
                    bullets.remove(bullet)
                    return True
        return False



