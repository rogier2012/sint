import pygame
from pygame.locals import *
import os
from time import sleep
import matplotlib as plt
from subprocess import *


result = 0.0
for i in range(100):
    res = Popen(["cat", "/proc/net/wireless"],stdout=PIPE )
    corr = ""
    line = res.stdout.readline()
    while line != '':
            # print(line)
            if "wlan0" in line:
                corr = line
            line = res.stdout.readline()
    # print(corr[18:-30])

    quality = int(corr[20:-53])
    if (quality <= 0):
        dBm = -100
    elif (quality >= 100):
        dBm = -50
    else:
        dBm = (quality / 2) - 100

    result = float(result) + (float(dBm) / 100)

print(result)