import pygame as pg
from constants import *

class Player:
    def __init__(self, row: int, col: int):
        self.image_list = IMAGE_PLAYER
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()

        self.rect.top = row * SIZE_WALL + MARGIN["TOP"]  # Tọa độ Y
        self.rect.left = col * SIZE_WALL + MARGIN["LEFT"]  # Tọa độ X

        self.row = row
        self.col = col
        self.direction = RIGHT  # Hướng mặc định

    def set_RC(self, row: int, col: int):
        '''Cập nhật vị trí theo ô lưới'''
        for i in range(len(MOVES)):
            if self.row + MOVES[i][0] == row and self.col + MOVES[i][1] == col:
                self.direction = i
                break
        self.row = row
        self.col = col
    
    def set_rect(self):
        self.rect.top = self.row * SIZE_WALL + MARGIN["TOP"]
        self.rect.left = self.col * SIZE_WALL + MARGIN["LEFT"]

    def get_RC(self):
        return self.row, self.col

    def draw(self, screen: pg.Surface, counter: int):
        '''Vẽ nhân vật theo hướng hiện tại'''
        if self.direction == RIGHT: 
            screen.blit(self.image_list[counter % 4], (self.rect.left, self.rect.top))
        elif self.direction == LEFT:
            screen.blit(pg.transform.rotate(self.image_list[counter % 4], 180), (self.rect.left, self.rect.top))
        elif self.direction == UP:
            screen.blit(pg.transform.rotate(self.image_list[counter % 4], 90), (self.rect.left, self.rect.top))
        elif self.direction == DOWN:
            screen.blit(pg.transform.rotate(self.image_list[counter % 4], 270), (self.rect.left, self.rect.top))

    def move(self):
        '''Di chuyển từng bước theo hướng'''
        if self.direction == RIGHT:
            self.rect.left += SIZE_WALL // 10  # Di chuyển từng phần nhỏ
        elif self.direction == LEFT:
            self.rect.left -= SIZE_WALL // 10
        elif self.direction == UP:
            self.rect.top -= SIZE_WALL // 10
        elif self.direction == DOWN:
            self.rect.top += SIZE_WALL // 10

    def reached_target(self):
        '''Kiểm tra nếu Pacman đến đúng vị trí ô lưới'''
        return self.rect.left == self.col * SIZE_WALL + MARGIN["LEFT"] and \
               self.rect.top == self.row * SIZE_WALL + MARGIN["TOP"]