import pygame
from pygame.locals import *
import os
from time import sleep
import matplotlib as plt
from subprocess import call


res = call(["cat", "/proc/net/wireless"])
for x in res:
    print(x)
quality = 0
if (quality <= 0):
    dBm = -100
elif (quality >= 100):
    dBm = -50
else:
    dBm = (quality / 2) - 100