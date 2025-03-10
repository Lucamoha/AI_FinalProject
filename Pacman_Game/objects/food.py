import pygame as pg

from constants import *

class Food:
    def __init__(self, row, col, size=BLOCK_SIZE, color=WHITE):
        self.size = size
        self.color = color

        # Tọa độ của thức ăn 
        self.x = col * SIZE_WALL + MARGIN["LEFT"] + SIZE_WALL // 2
        self.y = row * SIZE_WALL + MARGIN["TOP"] + SIZE_WALL // 2

        self.rect = pg.Rect(self.x - self.size // 2, self.y - self.size // 2, self.size, self.size) # Ranh giới va chạm của thưc ăn

    # Vẽ thức ăn
    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.size)

    # Kiểm tra xem thức ăn đã bị ăn chưa
    def check_food(self, player_rect): 
        return self.rect.colliderect(player_rect)
