import pygame as pg

from constants import *

class Food:
    def __init__(self, row, col, size=SIZE_WALL, color=WHITE):
        self.size = size
        self.color = color

        # Tọa độ của thức ăn
        self.row = row
        self.col = col
        self.x = col * SIZE_WALL + MARGIN["LEFT"]
        self.y = row * SIZE_WALL + MARGIN["TOP"]

        self.rect = pg.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size) # Ranh giới va chạm của thưc ăn

    # Vẽ thức ăn
    def draw(self, screen):
        image = pg.Surface([self.size // 2, self.size // 2])
        image.fill(WHITE)
        image.set_colorkey(WHITE)
        pg.draw.ellipse(image, YELLOW, [0, 0, self.size // 2, self.size // 2])
        screen.blit(image, (self.x + self.size // 4, self.y + self.size // 4))

    # Kiểm tra xem thức ăn đã bị ăn chưa
    def check_food(self, player_rect): 
        return self.rect.colliderect(player_rect)
    
    def getPos(self):
        return self.row, self.col
