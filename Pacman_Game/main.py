import pygame as pg
from constants import *
from objects.wall import Wall

pg.init()

# Cấu hình cửa sổ game
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pac-Man - Test Wall Rendering")
clock = pg.time.Clock()

# Khai báo biến toàn cục
_map = []
N = 0
M = 0

# Hàm đọc bản đồ từ file
def readMapInFile(map_name: str):
    global N, M, _map
    with open(map_name, "r") as f:
        x = f.readline().split()
        N, M = int(x[0]), int(x[1])
        
        _map = []
        for _ in range(N):
            line = list(map(int, f.readline().split()))
            _map.append(line)

        # Căn giữa bản đồ
        MARGIN["TOP"] = max(0, (HEIGHT - N * SIZE_WALL) // 2)
        MARGIN["LEFT"] = max(0, (WIDTH - M * SIZE_WALL) // 2)

# Đọc bản đồ
readMapInFile("levels/Level2/map1.txt")

# Vẽ màn hình game
running = True
while running:
    screen.fill(BLACK)  # Xóa màn hình
    
    # Vẽ tường dựa vào `_map`
    for i in range(N):
        for j in range(M):
            if _map[i][j] == WALL:
                wall = Wall(i, j)  # Tạo đối tượng tường
                wall.draw(screen)  # Vẽ tường lên màn hình
    
    pg.display.flip()  # Cập nhật màn hình
    
    # Bắt sự kiện thoát game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    clock.tick(FPS)

pg.quit()
