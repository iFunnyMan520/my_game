import pygame

pygame.init()

display_width = 820
display_height = 1000
bg = pygame.image.load(r'images/Background.jpg')


user_img = pygame.image.load(r'images/User.gif')
user_x = display_width / 2
user_y = display_height - 200
user_height = 100
user_width = 100
user_bullets = []
bullet_user_img = pygame.image.load(r'images/Rocket user.png')

cooldown_user = 0
cooldown_enemies = 0

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Eagle Force')


enemies = []
enemies_bullets = []
bullet_enemies_img = pygame.image.load(r'images/Rocket enemies.png')

fps = pygame.time.Clock()

bullet_sound = pygame.mixer.Sound(r'sounds/bullet.wav')
game_sound = pygame.mixer.Sound(r'sounds/game.wav')
endgame_sound = pygame.mixer.Sound(r'sounds/endgame.wav')
enemies_kill_sound = pygame.mixer.Sound(r'sounds/enemies_kill.wav')
