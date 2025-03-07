import pygame

from constants import *


class Wall:
    def __init__(self, row, col):
        self.image = pygame.Surface([SIZE_WALL, SIZE_WALL])
        pygame.draw.rect(self.image, BLUE, (0, 0, SIZE_WALL, SIZE_WALL), 1)

        self.rect = self.image.get_rect()
        self.rect.top = row * SIZE_WALL + MARGIN["TOP"] # Tọa độ Y
        self.rect.left = col * SIZE_WALL + MARGIN["LEFT"] # Tọa độ X

    def draw(self, screen):
        screen.blit(self.image, (self.rect.left, self.rect.top))
