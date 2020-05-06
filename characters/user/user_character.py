from game_field.field import *


class User:

    def __init__(self, _display, img, x, y):
        self._display = _display
        self._image = img
        self.x = x
        self.y = y

    def show(self):
        self._display.blit(self._image, (self.x, self.y))

    def move(self, key):
        if key[pygame.K_LEFT]:
            self.x -= 10
        if key[pygame.K_RIGHT]:
            self.x += 10
        if self.x < 0:
            self.x = display_width
        if self.x > display_width:
            self.x = 0

    def fire(self):
        pass

    def crash(self):
        pass
