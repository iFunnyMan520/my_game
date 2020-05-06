import pygame


display_width = 800
display_height = 1000


user_x = display_width / 2
user_y = display_height - 200
user_height = 100
user_width = 100


display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Eagle Force')


fps = pygame.time.Clock()
