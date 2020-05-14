import pygame


display_width = 820
display_height = 1000
bg = pygame.image.load(r'images/Background.jpg')


user_img = pygame.image.load(r'images/User.gif')
user_x = display_width / 2
user_y = display_height - 200
user_height = 100
user_width = 100
user_bullets = []


display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Eagle Force')


enemies = []
enemies_bullets = []

fps = pygame.time.Clock()

scores = 0
