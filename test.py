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

def begin_screen():
    lcd.fill(DEFAULT)
    text_surface = font_big.render('Hello World', True, WHITE)
    rect = text_surface.get_rect(center=CENTER)
    lcd.blit(text_surface, rect)
    pygame.display.update()


pygame.init()
pygame.mouse.set_visible(False)
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()

font_big = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 20)
page = 1
running = True
while running:
    # Scan touchscreen events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            running = False
        elif(event.type is MOUSEBUTTONUP):
            if (page == 1 ):
                begin_screen()
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
                page = 4
            elif (page == 4):
                lcd.fill(DEFAULT)
                text_surface = font_big.render("Quit?", True, WHITE)
                rect = text_surface.get_rect(center=(160,80))
                lcd.blit(text_surface, rect)
                text_surface = font_big.render("Yes", True, WHITE)
                rect = text_surface.get_rect(center=(80,160))
                lcd.blit(text_surface, rect)
                text_surface = font_big.render("No", True, WHITE)
                rect = text_surface.get_rect(center=(240,160))
                lcd.blit(text_surface, rect)
                pygame.display.update()
                page = 5
            elif (page == 5):
                pos = pygame.mouse.get_pos()
                if pos[0] > 160:
                    begin_screen()
                    page = 2
                else:
                    pygame.display.quit()
                    pygame.quit()
                    running = False

    sleep(0.1)


