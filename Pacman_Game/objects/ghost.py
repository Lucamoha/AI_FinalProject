import pygame as pg
import random
from constants import *

class Ghost:
    def __init__(self, row, col, preRow: int = 0, preCol: int = 0):
        self.row = row
        self.col = col
        self.direction = RIGHT

        self.x = col * SIZE_WALL + MARGIN["LEFT"]
        self.y = row * SIZE_WALL + MARGIN["TOP"]
        self.count_ghost = random.randint(0, len(IMAGE_GHOST_PATH) - 1)

        self.preRow = preRow
        self.preCol = preCol


    def draw(self, screen):
        image = pg.image.load(IMAGE_GHOST_PATH[self.count_ghost]).convert_alpha()
        image = pg.transform.scale(image, (SIZE_WALL, SIZE_WALL))
        screen.blit(image, (self.x, self.y))

    def set_RC(self, newRow, newCol):
        self.preRow = self.row
        self.preCol = self.col
        for i in range(len(MOVES)):
            if self.row + MOVES[i][0] == newRow and self.col + MOVES[i][1] == newCol:
                self.direction = i
                break
        self.row = newRow
        self.col = newCol
   
    def set_rect(self):
        self.x = self.col * SIZE_WALL + MARGIN["LEFT"]
        self.y = self.row * SIZE_WALL + MARGIN["TOP"]
    
    def get_rect(self):
        return pg.Rect(self.x, self.y, SIZE_WALL, SIZE_WALL)
    
    def get_pre_RC(self):
        return self.preRow, self.preCol
    
    def move(self):
        '''Di chuyển từng bước theo hướng'''
        if self.reached_target():
            return
        if self.direction == RIGHT:
            self.x += SIZE_WALL // 10
        elif self.direction == LEFT:
            self.x -= SIZE_WALL // 10
        elif self.direction == UP:
            self.y -= SIZE_WALL // 10
        elif self.direction == DOWN:
            self.y += SIZE_WALL // 10
        
    def get_RC(self):
        return self.row, self.col

    def reached_target(self):
        return self.x == self.col * SIZE_WALL + MARGIN["LEFT"] and \
               self.y == self.row * SIZE_WALL + MARGIN["TOP"]
