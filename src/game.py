import sys
import pygame
from pygame.locals import QUIT

# constants
FPS = 60
WIDTH = 1920
HEIGHT = 1080

# initialization
pygame.init()
clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Turukuun Pliis')

def start():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.fill((50, 50, 150))
        pygame.display.update()
        clock.tick(FPS)
