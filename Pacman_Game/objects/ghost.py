import pygame as pg
import random
from constants import *

class Ghost:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        
        self.x = col * SIZE_WALL + MARGIN["LEFT"]
        self.y = row * SIZE_WALL + MARGIN["TOP"]
        self.count_ghost = random.randint(0, len(IMAGE_GHOST_PATH) - 1)

    def draw(self, screen):
        image = pg.image.load(IMAGE_GHOST_PATH[self.count_ghost]).convert_alpha()
        image = pg.transform.scale(image, (SIZE_WALL, SIZE_WALL))
        screen.blit(image, (self.x, self.y))

    def set_RC(self, newRow, newCol):
        self.row = newRow
        self.col = newCol
        self.x = self.col * SIZE_WALL + MARGIN["LEFT"]
        self.y = self.row * SIZE_WALL + MARGIN["TOP"]
        
    def get_RC(self):
        return self.row, self.col
