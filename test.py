import pygame
from pygame.locals import *
import os
from time import sleep

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 50)


while True:
    # Scan touchscreen events
    page = 0
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            print pos
        elif(event.type is MOUSEBUTTONUP):
            if (page == 0):
                lcd.fill(WHITE)
                pygame.display.update()
                page = 1
            elif (page ==1 ):
                lcd.fill(BLACK)
                pygame.display.update()
                page = 0
    sleep(0.1)