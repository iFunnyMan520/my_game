from characters.user.user_character import *
from characters.user.enemy_characters import *
from functions.functions import *


pygame.init()


def create_enemy_array(array):
    enemy_img_1 = pygame.image.load(r'images/Enemy1.png')
    enemy_img_2 = pygame.image.load(r'images/Enemy2.gif')
    enemy_img_3 = pygame.image.load(r'images/Enemy3.png')
    array.append(Enemy(display, enemy_img_1, 200, 0, 90, 90, 1))
    array.append(Enemy(display, enemy_img_2, 400, 0, 100, 100, 2))
    array.append(Enemy(display, enemy_img_3, 600, 0, 110, 110, 3))


def run_game():
    game = True
    user = User(display, user_img, user_x, user_y)

    cooldown_user = 0
    cooldown_enemies = 0

    create_enemy_array(enemies)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(bg, (0, 0))

        write_text('Score: %s' % scores, 20, 50)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()
        if not cooldown_user:
            if keys[pygame.K_SPACE]:
                user_bullets.append(Bullet(user.x + user.width / 2, user.y))
                cooldown_user = 20
        else:
            cooldown_user -= 1

        for bullet in user_bullets:
            if not bullet.user_bullet_move():
                user_bullets.remove(bullet)

        user.move(keys)
        for enemy in enemies:
            enemy.move()
            enemy.show()
            if not cooldown_enemies:
                enemies_bullets.append(Bullet(enemy.x + enemy.width / 2, enemy.y +
                                       enemy.height))
                cooldown_enemies = 30
            else:
                cooldown_enemies -= 1
            for bullet in enemies_bullets:
                if not bullet.enemies_bullet_move():
                    enemies_bullets.remove(bullet)

            if crush(enemy, user):
                game = False

        user.show()

        pygame.display.update()

        fps.tick(60)

    return game_over()


while run_game():
    pass
pygame.quit()
quit()

