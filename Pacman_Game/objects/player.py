import pygame as pg

from constants import *

class Player:
    def __init__(self, row : int, col : int, score : int):
        self.image_list = IMAGE_PLAYER
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()

        self.rect.top = row * SIZE_WALL + MARGIN["TOP"] # Tọa độ Y
        self.rect.left = col * SIZE_WALL + MARGIN["LEFT"] # Tọa độ X

        self.row = row
        self.col = col

        self.score = score

    def set_RC(self, row : int , col : int):
        self.row = row
        self.col = col
        self.rect.top = row * SIZE_WALL + MARGIN["TOP"]
        self.rect.left = col * SIZE_WALL + MARGIN["LEFT"]

    def get_RC(self):
        return [self.row, self.col]

    def draw(self, screen : pg.Surface, direction : int, counter : int):
        '''Vẽ nhân vật lên giao diện theo hướng chỉ định'''
        if direction == RIGHT: 
            screen.blit(self.image_list[counter // 5], (self.rect.left, self.rect.top))
        elif direction == LEFT:
            screen.blit(pg.transform.rotate(self.image_list[counter // 5], 180), (self.rect.left, self.rect.top))
        elif direction == UP:
            screen.blit(pg.transform.rotate(self.image_list[counter // 5], 90), (self.rect.left, self.rect.top))
        elif direction == DOWN:
            screen.blit(pg.transform.rotate(self.image_list[counter // 5], 270), (self.rect.left, self.rect.top))

    def move(self, dx : int, dy : int):
        '''Di chuyển nhân vật một đoạn dx, dy (pixel)'''
        self.rect.top += dx
        self.rect.left += dy

    def touch_New_RC(self, row : int, col : int):
        '''Kiểm tra vị trí hiện tại có trùng vị trí row, col đang xét'''
        return self.rect.top == row * SIZE_WALL and self.rect.left == col * SIZE_WALL
