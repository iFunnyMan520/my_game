from game_field.field import *
from characters.user.enemy_characters import *


def enemies_move(array, bullets_arr):
    global cooldown_enemies
    for arr in array:
        arr.move()
        if arr.destroy(bullets_arr):
            return True
        if not cooldown_enemies:
            enemies_bullets.append(Bullet(arr.x + arr.width / 2, arr.y +
                                   arr.height, bullet_enemies_img))
            cooldown_enemies = 30
        else:
            cooldown_enemies -= 1
        for bullet in enemies_bullets:
            if not bullet.enemies_bullet_move():
                enemies_bullets.remove(bullet)


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


def crush(enemies_arr, user):
    for enemy in enemies_arr:
        if user.y < enemy.y + enemy.height:
            if user.x <= (enemy.x + enemy.width / 2) <= user.x + user_width:
                enemy.y = display_height
                return True

    for bullet in enemies_bullets:
        if user.y < bullet.y + bullet.height:
            if user.x <= (bullet.x + bullet.width / 2) <= user.x + user_width:
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


def count_scores():
    pass


class Bullet:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self._img = img
        self.speed = 8
        self.height = 40
        self.width = 40

    def user_bullet_move(self):
        self.y -= 5
        if self.y >= 0:
            display.blit(self._img, (self.x - self.width / 2, self.y))
            return True
        else:
            return False

    def enemies_bullet_move(self):
        self.y += 4
        if self.y <= display_height:
            display.blit(self._img, (self.x - self.width / 2, self.y))
            return True
        else:
            return False
