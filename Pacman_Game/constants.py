import pygame as pg

# DEFINE COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# DEFINE MAP
SIZE_WALL: int = 30
DEFINE_WIDTH: int = 6
BLOCK_SIZE: int = SIZE_WALL // 2
MOVES = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# Entity
EMPTY = 0
WALL = 1
FOOD = 2
GHOST = 3

# Direction 
RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

# Setup screen
WIDTH: int = 1200
HEIGHT: int = 600
FPS: int = 60

MARGIN = {
    "TOP": 0, # "TOP": Xác định khoảng cách từ mép trên của cửa sổ đến khu vực chơi.
    "LEFT": 0  # "LEFT" Xác định khoảng cách từ mép trái của cửa sổ đến khu vực chơi.
}

# IMAGE
IMAGE_GHOST_PATH = ["assets/ghost_images/blue.png", "assets/ghost_images/dead.png", "assets/ghost_images/orange.png", "assets/ghost_images/pink.png", "assets/ghost_images/powerup.png", "assets/ghost_images/red.png"]
IMAGE_PLAYER_PATH = ["assets/player_images/1.png", "assets/player_images/2.png", "assets/player_images/3.png", "assets/player_images/4.png"]
IMAGE_GHOST = []
IMAGE_PLAYER = []
for image_path in IMAGE_PLAYER_PATH:
    IMAGE_PLAYER.append(pg.transform.scale(pg.image.load(image_path), (SIZE_WALL, SIZE_WALL)))
