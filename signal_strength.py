import threading
from time import sleep
import pygame
from subprocess import *

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
DEFAULT = (80,168,227)
CENTER = (160,120)
GREEN = (92, 184, 92)
ORANGE = (236, 151, 31)
RED = (201, 48, 44)

class signalStrength(threading.Thread):
    def __init__(self,surface,running):
        threading.Thread.__init__(self)
        self.surface = surface
        self.running = running

    def run(self):
        last_result = 1
        while self.running:
            last_result = signal_strength(self.surface,last_result)
            sleep(0.5)


def show_bars(surface,number=5):
    surface.fill(DEFAULT)

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
        signal = Popen("iwconfig wlan0 | grep -o \'Signal level=[0-9]*\/[0-9]*\'", stdout=PIPE)
        freq = Popen("iwconfig wlan0 | grep -o \'[0-9]\.[0-9]*\sGHz\'", stdout=PIPE)
        corr = ""
        signal_string = signal.stdout.readline()
        quality = signal_string[13:15]
        # print(corr[18:-30])

        # quality = int(corr[20:-53])
        if (quality <= 0):
            dBm = -100
        elif (quality >= 100):
            dBm = -50
        else:
            dBm = (quality / 2) - 100

        result = float(result) + (float(quality) / 100)
    bars = int(result/20)
    if surface is not None:

        if (bars != previous):
            show_bars(surface,bars)

    return bars

# while True:
    # print(signal_strength(None,1))
    # sleep(0.1)