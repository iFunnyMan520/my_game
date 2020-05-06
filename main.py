from characters.user.user_character import *
from characters.user.enemy_characters import *
from functions.functions import *

pygame.init()
bg = pygame.image.load(r'images/Background.jpg')
user_img = pygame.image.load(r'images/User.gif')


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

    enemies = []
    create_enemy_array(enemies)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(bg, (0, 0))

        key_move = pygame.key.get_pressed()
        if key_move[pygame.K_ESCAPE]:
            pause()

        user.move(key_move)
        for enemy in enemies:
            enemy.move()
            enemy.show()


        user.show()

        pygame.display.update()

        fps.tick(60)


run_game()

