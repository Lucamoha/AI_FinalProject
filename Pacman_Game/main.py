import pygame as pg
import time
import sys

from constants import *
from objects.menu import Menu, Button
from objects.food import Food
from objects.player import Player
from objects.ghost import Ghost
from Algorithms.BFS import BFS
from Algorithms.BeamSearch import BeamSearch
from Algorithms.Backtracking import Backtracking
from Algorithms.A_Star import A_Star
from Algorithms.Partial_Observation import Partial_Observation
from Algorithms.Q_Learning import QLearning
from Algorithms.Ghost_move import A_star_for_ghost, random_move_for_ghost


level = 1
map = 1    
algo = ""

_N = 0
_M = 0
wallPos = []
foodList = []
foodListToDraw = []  
ghostList = []

player = Player(0, 0)
totalStep = 0
totalFood = 0
counter = 0
totalTime = 0
isMoving = False

# Biến toàn cục để lưu trữ hướng hiện tại
current_direction = RIGHT  # Hướng mặc định


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

pg.mixer.init()
eatFood_Sound = pg.mixer.Sound('assets/sounds/pacman_eatfruit.wav')
pacmanDeath_Sound = pg.mixer.Sound('assets/sounds/pacman_death.wav')
begining_Sound = pg.mixer.Sound('assets/sounds/pacman_beginning.wav')
win_Sound = pg.mixer.Sound('assets/sounds/pacman_intermission.wav')

def initMap(fileMap):
    '''Khởi tạo map, các list đối tượng từ fileMap sau khi người dùng hoàn thành Menu'''
    global totalTime, isMoving
    totalTime = 0
    isMoving = False

    with open(fileMap, 'r') as file:
        _map = file.readlines()

    global _N, _M
    _N = int(_map[0].split()[0])  # Hàng
    _M = int(_map[0].split()[1])  # Cột

    MARGIN["TOP"] = (HEIGHT - _N * SIZE_WALL) // 2
    MARGIN["LEFT"] = (WIDTH - _M * SIZE_WALL) // 2

    global wallPos, foodList, ghostList
    wallPos = []
    foodList = []
    ghostList = []

    for i in range(_N):
        for j in range(_M):
            cell = int(_map[i + 1].split()[j])

            if cell == WALL:
                wallPos.append((i, j))
            elif cell == FOOD:
                foodList.append(Food(i, j))
            elif cell == GHOST:
                ghostList.append(Ghost(i, j))

    player_X = int(_map[len(_map) - 1].split()[0])
    player_Y = int(_map[len(_map) - 1].split()[1])
    player.set_RC(player_X, player_Y)
    player.set_rect()


def timer(func):
    def wrapper(*args, **kwargs):
        global totalTime
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start
        totalTime += elapsed_time
        return result
    return wrapper
BFS = timer(BFS)
BeamSearch = timer(BeamSearch)
Backtracking = timer(Backtracking)
A_Star = timer(A_Star)
Partial_Observation = timer(Partial_Observation)
QLearning = timer(QLearning)

def draw():
    global wallPos, screen, foodList, foodListToDraw, ghostList, counter, isMoving
    screen.fill(BLACK)
    player.draw(screen, counter)

    for i, j in wallPos:
        wallSurface = pg.Surface([SIZE_WALL, SIZE_WALL], pg.SRCALPHA)
        pg.draw.rect(wallSurface, (0, 0, 128), (0, 0, SIZE_WALL, SIZE_WALL))
        pg.draw.rect(wallSurface, (0, 255, 255), (0, 0, SIZE_WALL, SIZE_WALL), 1)
        screen.blit(wallSurface, (j * SIZE_WALL + MARGIN["LEFT"], i * SIZE_WALL + MARGIN["TOP"]))

    for food in foodListToDraw:
        food.draw(screen)
    
    for ghost in ghostList:
        ghost.draw(screen)


def drawMap():
    global isMoving, counter, ghostList, level, foodListToDraw, current_direction, playerPath, algo, isStarted
    if not isMoving:
        draw()
        pg.display.flip()
        if algo != "Manual":
            return
            

    # Nếu là chế độ tự chơi cho ghost di chuyển kể cả khi pacman không di chuyển
    if algo == "Manual" and not isMoving:
        i = 1
        all_ghost_reached_target = False
        while not all_ghost_reached_target:
            all_ghost_reached_target = True
            for ghost in ghostList:
                if not ghost.reached_target():
                    all_ghost_reached_target = False
                    break
                
            if i % 5 == 0:
                if level > 2:
                    for ghost in ghostList:
                        ghost.move()
                draw()
            pg.display.flip()
            clock.tick(FPS)
            i += 1

        for ghost in ghostList:
            ghost.set_rect()

        continueGame = checkCollision()
        if not continueGame:    
            alive = False
            pacmanDeath_Sound.play()
            showEndPage(alive)
                
    i = 1
    while not player.reached_target():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return showMenu()
                # Thêm xử lý thay đổi hướng trong quá trình di chuyển
                elif event.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
                    # Cập nhật hướng mới
                    if event.key == pg.K_UP:
                        new_direction = UP
                    elif event.key == pg.K_DOWN:
                        new_direction = DOWN
                    elif event.key == pg.K_LEFT:
                        new_direction = LEFT
                    elif event.key == pg.K_RIGHT:
                        new_direction = RIGHT
                    
                    # Lưu hướng mới
                    current_direction = new_direction

        if i % 5 == 0:
            player.move()
            if level > 2:
                for ghost in ghostList:
                    ghost.move()    
            counter += 1
            draw()
        if i == 35:
            foodListToDraw = foodList.copy()

        pg.display.flip()
        clock.tick(FPS)
        i += 1
    

    # Khi đã đến ô đích, kiểm tra có thể đi tiếp theo hướng hiện tại không ở chế độ tự chơi
    if algo == "Manual" and isStarted:
        row, col = player.get_RC()
        next_row, next_col = row, col
        
        if current_direction == UP:
            next_row = row - 1
        elif current_direction == DOWN:
            next_row = row + 1
        elif current_direction == LEFT:
            next_col = col - 1
        elif current_direction == RIGHT:
            next_col = col + 1
        
        # Cập nhật hướng cho player
        player.direction = current_direction
        
        # Nếu có thể di chuyển theo hướng hiện tại (không có tường) thì thêm vào playerPath
        if (next_row, next_col) not in wallPos and 0 <= next_row < _N and 0 <= next_col < _M:
            playerPath = [(next_row, next_col)]
        else:
            playerPath = []
    
    for ghost in ghostList:
        ghost.set_rect()

    continueGame = checkCollision()
    if not continueGame:    
        alive = False
        pacmanDeath_Sound.play()
        showEndPage(alive)

    isMoving = False 

def showEndPage(alive = True):
    global screen, level, map, algo, totalStep, totalFood, totalTime
    title = f"--Level: {level} - Map: {map} - Algo: {algo}--"
    print(title)
    print(f"Status: {'Lose' if not alive else 'Win'}")
    print(f"Steps: {totalStep}")
    print(f"Food: {totalFood}")
    print(f"Score: {totalStep * (-1) + totalFood * 10}")
    print(f"Time: {totalTime}s")
    print('-' * len(title))

    def stop_music_and_show_menu():
        pg.mixer.stop()  # Dừng tất cả âm thanh đang phát
        showMenu()
    
    btContinue = Button(300, HEIGHT // 2 + 150, 200, 60, screen, "Continue", stop_music_and_show_menu)
    btExit = Button(WIDTH - 300 - 200, HEIGHT // 2 + 150, 200, 60, screen, "Exit", lambda: (pg.quit(), sys.exit()))

    screen.fill(BLACK)
    screen.blit(pg.image.load('assets/background.jpg'), (0, 0))
    pg.display.flip() 

    StatusTextSurface = pg.font.SysFont('Arial', 100, bold=True).render(f"{'LOSE' if not alive else 'WIN'}", True, (255, 215, 0))
    textWidth = StatusTextSurface.get_size()[0]
    shadowSurface = pg.font.SysFont('Arial', 100, bold=True).render(f"{'LOSE' if not alive else 'WIN'}", True, BLACK)
    screen.blit(shadowSurface, (WIDTH // 2 - textWidth // 2 + 2, 52))
    screen.blit(StatusTextSurface, (WIDTH // 2 - textWidth // 2, 50))


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        if btContinue.animation():
            return
        
        btExit.animation()

        pg.display.flip()
    
def checkCollision():
    global ghostList, player
    # Kiểm tra va chạm với từng Ghost
    for ghost in ghostList:
        if ghost.get_RC() == player.get_RC() or (player.get_pre_RC() == ghost.get_RC() and player.get_RC() == ghost.get_pre_RC()):
            print("Pacman chạm Ghost!")  # Debug
            return False  # Pacman chết
    
    return True 

def showMenu():
    global level, map, algo, screen
    menu = Menu(screen)
    level, map, algo = menu.main()

    initMap(f"levels/Level{level}/map{map}.txt")
    main()

isStarted = False # Kiểm tra xem đã bắt đầu chưa

def main():
    global level, map, algo, totalStep, totalFood, totalTime, isMoving, counter, isStarted
    global screen, foodList, foodListToDraw, ghostList, wallPos, playerPath, current_direction
    
    totalStep = 0
    totalFood = 0
    running = True
    alive = True
    counter = 0
    
    if algo == "BFS":
        algoFunc = BFS
    elif algo == "BeamSearch":
        algoFunc = BeamSearch
    elif algo == "Backtracking":
        algoFunc = Backtracking
    elif algo == "Partial_Observation":
        algoFunc = Partial_Observation
    elif algo == "QLearning":
        algoFunc = QLearning
    elif algo == "A_Star":
        algoFunc = A_Star
    else: # Manual
        algoFunc = None

    playerPath = []


    # Tạm ngưng trước khi bắt đầu
    foodListToDraw = foodList.copy()
    draw()
    pg.display.flip()
    begining_Sound.play()
    time.sleep(4)

    if algo != "Manual" and (level == 1 or level == 2):
        if algo == "QLearning":
            playerPath = algoFunc(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos, map=map, level=level)
        else:
            playerPath = algoFunc(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos)
    
    while running:
        drawMap()
        foodListToDraw = foodList.copy() # Danh sách thức ăn trước khi xóa

        # Xử lý chế độ tự chơi
        if algo == "Manual":
            # Xử lý sự kiện phím chỉ khi không di chuyển
            if not isMoving:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        if event.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
                            isStarted = True  # Đánh dấu đã bắt đầu di chuyển

                            # Lưu hướng mới khi người chơi nhấn phím
                            if event.key == pg.K_UP:
                                current_direction = UP
                            elif event.key == pg.K_DOWN:
                                current_direction = DOWN
                            elif event.key == pg.K_LEFT:
                                current_direction = LEFT
                            elif event.key == pg.K_RIGHT:
                                current_direction = RIGHT
                            elif event.key == pg.K_ESCAPE:
                                return showMenu()

                row, col = player.get_RC()
                next_row, next_col = row, col
                
                # Tính toán vị trí tiếp theo dựa trên hướng hiện tại
                if current_direction == UP:
                    next_row = row - 1
                elif current_direction == DOWN:
                    next_row = row + 1
                elif current_direction == LEFT:
                    next_col = col - 1
                elif current_direction == RIGHT:
                    next_col = col + 1
                
                if isStarted:
                    # Nếu đã bắt đầu di chuyển, kiểm tra xem có thể đi tiếp theo hướng hiện tại không
                    if (next_row, next_col) not in wallPos and 0 <= next_row < _N and 0 <= next_col < _M:
                        playerPath = [(next_row, next_col)]
                    else:
                        playerPath = []

        if not (level == 1 or level == 2):
            for ghost in ghostList:
                current_pos = ghost.get_RC()
                pacman_pos = player.get_RC()

                if level == 3:
                    new_pos = random_move_for_ghost(current_pos, wallPos)
                    if new_pos:
                        ghost.set_RC(new_pos[0], new_pos[1])
                else:
                    ghost_path = A_star_for_ghost(current_pos, pacman_pos, wallPos)
                    if ghost_path and len(ghost_path) > 0:
                        next_pos = ghost_path[0]
                        ghost.set_RC(next_pos[0], next_pos[1])

            if algo != "Manual":
                if algo == "QLearning":
                    playerPath = algoFunc(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos, map=map, level=level)
                else:
                    playerPath = algoFunc(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos)
            
        if playerPath:
            player.set_RC(playerPath[0][0], playerPath[0][1])
            playerPath.pop(0)
            isMoving = True
        elif algo != "Manual" or not playerPath:
            alive = False

        totalStep += 1
        if (level == 5 and totalStep % 20 == 0):
            ghostList.append(Ghost(_N // 2, _M // 2))

        for food in foodList:
            if player.get_RC() == food.get_RC():
                totalFood += 1
                eatFood_Sound.play()
                foodList.remove(food)
                break
        
        if alive and not foodList:
            win_Sound.play()
            showEndPage(alive)
            break
    
    showMenu()


if __name__ == '__main__':
    showMenu()
    pg.quit()