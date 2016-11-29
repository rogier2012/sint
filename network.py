import pygame
from pygame.locals import *
import os
from time import sleep
import matplotlib as plt
from subprocess import call


res = call(["cat", "/proc/net/wireless"])
print(res)