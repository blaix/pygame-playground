SPEED = 1
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

character_right = 'images/bob-right.png'
character_left = 'images/bob-left.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
character = pygame.image.load(character_right).convert_alpha()
grass = pygame.image.load('images/grass.png')
font = pygame.font.SysFont("Verdana", 16)

x, y = 0, 0
move_x, move_y = 0, 0
fullscreen = 0

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                if fullscreen:
                    fullscreen = 0
                else:
                    fullscreen = FULLSCREEN
                screen = pygame.display.set_mode(SCREEN_SIZE, fullscreen, 32)
            if event.key == K_LEFT:
                character = pygame.image.load(character_left).convert_alpha()
                move_x = -SPEED
            elif event.key == K_RIGHT:
                character = pygame.image.load(character_right).convert_alpha()
                move_x = +SPEED
            elif event.key == K_UP:
                move_y = -SPEED
            elif event.key == K_DOWN:
                move_y = +SPEED
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP or event.key == K_DOWN:
                move_y = 0

    x += move_x
    y += move_y
    
    for bg_y in range(0, SCREEN_HEIGHT, 10):
        for bg_x in range(0, SCREEN_WIDTH, 10):
            screen.blit(grass, (bg_x, bg_y))
            
    screen.blit(font.render("Hit 'f' to enter/exit fullscreen mode.", True, (250, 250, 250)), (5, 5))
    screen.blit(character, (x, y))
    
    pygame.display.update()
