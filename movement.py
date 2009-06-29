character_image_filename = 'images/bob.png'
speed = 2
screen_width = 640
screen_height = 480

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
character = pygame.image.load(character_image_filename).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -speed
            elif event.key == K_RIGHT:
                move_x = +speed
            elif event.key == K_UP:
                move_y = -speed
            elif event.key == K_DOWN:
                move_y = +speed
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP or event.key == K_DOWN:
                move_y = 0

    x += move_x
    y += move_y
    
    screen.fill((0, 0, 0))
    screen.blit(character, (x, y))
    
    pygame.display.update()
