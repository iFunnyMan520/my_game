from game_field.field import *


def text(message, x, y, font_color=(0, 0, 0),
         font='/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf',
         font_size=30):
    font_type = pygame.font.Font(font, font_size)
    pause_text = font_type.render(message, True, font_color)
    display.blit(pause_text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        text('Paused. Press enter to continue', 200, 400)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False

        pygame.display.update()



"""def crush(enemy, user):
    if user.y < enemy.y:
        if enemy.x < (user.x + user_width) / 2 < enemy.width:
            return True
    return False


def game_over():
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        text('Game over. Press enter to play again or ESC to escape', 100, 400)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            return True
        if key[pygame.K_ESCAPE]:
            return False

        pygame.display.update()"""

