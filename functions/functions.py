from game_field.field import *


def write_text(message, x, y, font_color=(0, 0, 0),
         font='/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf',
         font_size=30):
    font_type = pygame.font.Font(font, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        write_text('Paused. Press enter to continue', 200, 400)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


def crush(enemy, user):
    if user.y < enemy.y + enemy.height:
        if user.x <= (enemy.x + enemy.width / 2) <= user.x + user_width:
            return True
    return False


def game_over():
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        write_text('Game over. Press enter to play again or ESC to escape',
                  10, 400)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            return True
        if key[pygame.K_ESCAPE]:
            return False

        pygame.display.update()


def count():
    pass


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8

    def user_bullet_move(self):
        self.y -= 5
        if self.y >= 0:
            pygame.draw.circle(display, (255, 0, 0), (int(self.x),
                                                      int(self.y)), 10)
            return True
        else:
            return False

    def enemies_bullet_move(self):
        self.y += 4
        if self.y <= display_height:
            pygame.draw.circle(display, (255, 0, 0), (int(self.x),
                                                      int(self.y)), 10)
            return True
        else:
            return False
