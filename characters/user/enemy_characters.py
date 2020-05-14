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

    def show(self):
        self._display.blit(self._img, (self.x, self.y))

    def move(self):

        if self.y >= display_width:
            self.y = 0
            self.x = random.randint(1, 8) * 100
        else:
            if self.level == 1:
                self.y += 6
            elif self.level == 2:
                self.y += 7
            elif self.level == 3:
                self.y += 8

    def destroy(self):
        pass



