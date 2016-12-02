import threading
from time import sleep
import pygame
import re
from subprocess import *

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
DEFAULT = (80,168,227)
CENTER = (160,120)
GREEN = (92, 184, 92)
ORANGE = (236, 151, 31)
RED = (201, 48, 44)

SIGNAL_LEVEL =  ["iwconfig", "wlan0"]
FREQUENCY =     ["iwconfig", "wlan0", "|", "grep", "-o" , "'[0-9]\.[0-9]*\sGHz'"]

class signalStrength(threading.Thread):
    def __init__(self,surface,running):
        threading.Thread.__init__(self)
        self.surface = surface
        self.running = running

    def run(self):
        last_result = 1
        while self.running:
            last_result = signal_strength(self.surface,last_result)
            sleep(0.1)


def show_bars(surface,number=5):
    surface.fill(DEFAULT)
    font_big = pygame.font.Font(None, 50)
    text_surface = font_big.render("Pakjes", True, WHITE)
    text_surface1 = font_big.render("Zoeker", True, WHITE)
    rect = text_surface.get_rect(center=(80, 80))
    rect1 = text_surface1.get_rect(center=(80, 160))
    surface.blit(text_surface, rect)
    surface.blit(text_surface1,rect1)
    color = RED
    if number == 2:
        color = RED
    elif number == 3:
        color = ORANGE
    elif number == 4:
        color = ORANGE
    elif number == 5:
        color = GREEN

    if number >= 1:
        rect = pygame.Rect(200, 185,  80,30)
        surface.fill(color,rect)
    if number >= 2:
        rect = pygame.Rect(200, 145, 80, 30)
        surface.fill(color, rect)
    if number >= 3:
        rect = pygame.Rect(200, 105, 80, 30)
        surface.fill(color, rect)
    if number >= 4:
        rect = pygame.Rect(200, 65, 80, 30)
        surface.fill(color, rect)
    if number >= 5:
        rect = pygame.Rect(200, 25, 80, 30)
        surface.fill(color, rect)
    pygame.display.update()


def signal_strength(surface,previous):
    result = 0.0

    # iwconfig wlan0 | grep -o '[0-9]\.[0-9]*\sGHz'
    # Signal level=[0-9]*\/[0-9]*
    for i in range(100):
        iwconfig = Popen(SIGNAL_LEVEL, stdout=PIPE)
        # freq = Popen(FREQUENCY, stdout=PIPE)
        iwconfig_string = ""
        signal_string = iwconfig.stdout.readline()
        while signal_string != '':
            iwconfig_string = iwconfig_string + signal_string
            signal_string = iwconfig.stdout.readline()

        signal_level = ""
        quality = 0
        m = re.search('Signal level=[0-9]*\/[0-9]*', iwconfig_string)
        if m:
            signal_level = m.group(0)
            # print(signal_level)
            m1 = re.search('[0-9]+',signal_level)
            if m1:
                # print(m1.group(0))
                quality = int(m1.group(0))

        # print(quality)
        if (quality <= 0):
            dBm = -100
        elif (quality >= 100):
            dBm = -50
        else:
            dBm = (quality / 2) - 100

        result = float(result) + (float(quality) / 100)
    bars = int(result/20)
    # print(result)
    # print(bars)
    if surface is not None:

        if (bars != previous):
            show_bars(surface,bars)

    return bars

# while True:
#     print(signal_strength(None,1))
#     sleep(0.1)