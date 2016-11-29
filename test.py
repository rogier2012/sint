import pygame
from pygame.locals import *
import os
from time import sleep

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
DEFAULT = (80,168,227)
CENTER = (160,120)

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(True)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 20)
page = 1

while True:
    # Scan touchscreen events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
        elif(event.type is MOUSEBUTTONUP):
            if (page == 0):
                lcd.fill(WHITE)

                pygame.display.update()
                page = 1
            elif (page == 1 ):
                lcd.fill(DEFAULT)
                text_surface = font_big.render('Hello World', True, WHITE)
                rect = text_surface.get_rect(center=CENTER)
                lcd.blit(text_surface, rect)
                pygame.display.update()
                page = 2
            elif (page == 2):
                lcd.fill(DEFAULT)
                text_surface = font_small.render("Text hello Hello", True, WHITE)
                rect = text_surface.get_rect(center=CENTER)
                lcd.blit(text_surface, rect)
                pygame.display.update()
                page = 3
            elif (page == 3):
                lcd.fill(DEFAULT)
                text_surface = font_small.render("Text hello Hello", True, WHITE)
                rect = text_surface.get_rect(center=CENTER)
                lcd.blit(text_surface, rect)
                pygame.display.update()
                page = 3
    sleep(0.1)