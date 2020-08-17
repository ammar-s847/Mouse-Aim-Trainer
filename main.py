import pygame
import time
import math
import random
from sys import exit as sysExit

# Initialization
pygame.mixer.pre_init(44100, 16, 2, 2048)
pygame.init()

WinX, WinY = 450, 450
window = pygame.display.set_mode((WinX, WinY))
pygame.display.set_caption("Mouse Aim Trainer")
run = True
clock = pygame.time.Clock()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 128, 0)

# Classes


# Variables


# Functions


# PyGame Loop
while run:
    # Event Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

if not run:
    pygame.quit()
    sysExit()