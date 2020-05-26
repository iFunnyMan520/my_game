from characters.user.user_character import *
from characters.user.enemy_characters import *
from functions.functions import *



scores = 0


def create_enemy_array(array):
    enemy_img_1 = pygame.image.load(r'images/Enemy1.png')
    enemy_img_2 = pygame.image.load(r'images/Enemy2.gif')
    enemy_img_3 = pygame.image.load(r'images/Enemy3.png')
    array.append(Enemy(display, enemy_img_1, 200, 0, 90, 90, 1))
    array.append(Enemy(display, enemy_img_2, 400, 0, 100, 100, 2))
    array.append(Enemy(display, enemy_img_3, 600, 0, 110, 110, 3))


def run_game():
    global cooldown_user, scores
    game = True
    user = User(display, user_img, user_x, user_y)

    create_enemy_array(enemies)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(bg, (0, 0))

        write_text(f'Score: {scores}', 20, 50)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause()
        if not cooldown_user:
            if keys[pygame.K_SPACE]:
                pygame.mixer.Sound.play(bullet_sound)
                user_bullets.append(Bullet(user.x + user.width / 2, user.y,
                                           bullet_user_img))
                cooldown_user = 20
        else:
            cooldown_user -= 1

        for bullet in user_bullets:
            if not bullet.user_bullet_move():
                user_bullets.remove(bullet)

        user.move(keys)
        user.show()
        if enemies_move(enemies, user_bullets):
            scores += 1

        if crush(enemies, user):
            enemies.clear()
            enemies_bullets.clear()
            user_bullets.clear()
            pygame.mixer.Sound.play(endgame_sound)
            write_text(f'Max score: {scores}', 350, 450)
            scores = 0
            game = False

        pygame.display.update()

        fps.tick(60)

    return game_over()


while run_game():
    pass
pygame.quit()
quit()



