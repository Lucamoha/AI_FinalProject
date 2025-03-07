import os
import pygame as pg

sprites = {}

def load_sprites(folder_name : str):
    path = os.path.join("assets", folder_name)

    if not os.path.exists(path):
        print(f"Thư mục {path} không tồn tại")
        return
    
    for file in os.listdir(path):
        try:
            sprite_name = os.path.splitext(file)[0]

            sprites[sprite_name] = pg.image.load(os.path.join(path, file))

        except pg.error as e:
            print(f"Không thể tải hình ảnh {file}: {e}")

def get_sprite(name):
    sprite = sprites.get(name)

    if sprite is None:
        print(f"Không tìm thấy sprite: {name}")
    return sprite