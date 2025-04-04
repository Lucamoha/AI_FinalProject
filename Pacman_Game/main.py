import pygame as pg
import time
import sys

from constants import *
from objects.menu import Menu, Button
from objects.food import Food
from objects.player import Player
from objects.ghost import Ghost
from Algorithms.BFS import BFS
from Algorithms.DFS import DFS
from Algorithms.Ghost_move import A_star, random_move


level = 1
map = 1     # STT map
algo = ""

_N = 0
_M = 0
wallPos = []
foodList = []
ghostList = []

player = Player(0, 0)
totalStep = 0
totalFood = 0
counter = 0
totalTime = 0
isMoving = False


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


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
DFS = timer(DFS)


def draw():
    global wallPos, screen, foodList, ghostList, counter

    screen.fill(BLACK)
    player.draw(screen, counter)

    for i, j in wallPos:
        wallSurface = pg.Surface([SIZE_WALL, SIZE_WALL], pg.SRCALPHA)
        pg.draw.rect(wallSurface, (0, 0, 128), (0, 0, SIZE_WALL, SIZE_WALL))
        pg.draw.rect(wallSurface, (0, 255, 255), (0, 0, SIZE_WALL, SIZE_WALL), 1)
        screen.blit(wallSurface, (j * SIZE_WALL + MARGIN["LEFT"], i * SIZE_WALL + MARGIN["TOP"]))

    for food in foodList:
        food.draw(screen)
    
    for ghost in ghostList:
        ghost.draw(screen)


def drawMap():
    global isMoving, counter, ghostList, level

    if not isMoving:
        draw()
        pg.display.flip()
        return
    
    i = 1
    while not player.reached_target():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return showMenu()

        if i % 5 == 0:
            player.move()
            if level > 2:
                for ghost in ghostList:
                    ghost.move()
            
            draw()

        if i % 10 == 0:
            counter += 1

        pg.display.flip()
        clock.tick(FPS)
        i += 1
    
    for ghost in ghostList:
        ghost.set_rect()
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

    btContinue = Button(300, HEIGHT // 2 + 150, 200, 60, screen, "Continue", showMenu)
    btExit = Button(WIDTH - 300 - 200, HEIGHT // 2 + 150, 200, 60, screen, "Exit", lambda: (pg.quit(), sys.exit()))

    screen.fill(BLACK)
    screen.blit(pg.image.load('assets/background.jpg'), (0, 0))
    pg.display.flip() 

    StatusTextSurface = pg.font.SysFont('Arial', 100, bold=True).render(f"{'LOSE' if not alive else 'WIN'}", True, (255, 215, 0))
    textWidth = StatusTextSurface.get_size()[0]
    shadowSurface = pg.font.SysFont('Arial', 100, bold=True).render(f"{'LOSE' if not alive else 'WIN'}", True, BLACK)
    screen.blit(shadowSurface, (WIDTH // 2 - textWidth // 2 + 2, 52))
    screen.blit(StatusTextSurface, (WIDTH // 2 - textWidth // 2, 50))

    ScoreTextSurface = pg.font.SysFont('Arial', 60, bold=True).render(f"Score: {totalStep * (-1) + totalFood * 10}", True, RED)
    textWidth = ScoreTextSurface.get_size()[0]
    ScoreTextSurfaceShadow = pg.font.SysFont('Arial', 60, bold=True).render(f"Score: {totalStep * (-1) + totalFood * 10}", True, BLACK)
    screen.blit(ScoreTextSurfaceShadow, (WIDTH // 2 - textWidth // 2 + 2, 252))
    screen.blit(ScoreTextSurface, (WIDTH // 2 - textWidth // 2, 250))


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

    for ghost in ghostList:
        if ghost.get_RC() == player.get_RC():
            return False
    
    return True


def showMenu():
    global level, map, algo, screen
    menu = Menu(screen)
    level, map, algo = menu.main()

    initMap(f"levels/Level{level}/map{map}.txt")
    main()


def main():
    global level, map, algo, totalStep, totalFood, totalTime, isMoving, counter
    global screen, foodList, ghostList, wallPos
    
    totalStep = 0
    totalFood = 0
    running = True
    alive = True
    counter = 0

    if algo == "BFS":
        algoFunc = BFS
    elif algo == "DFS":
        algoFunc = DFS

    if level == 1 or level == 2:
        playerPath = algoFunc(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos)

    while running:
        drawMap()
        
        if not (level == 1 or level == 2):
            for ghost in ghostList:
                current_pos = ghost.get_RC()
                pacman_pos = player.get_RC()

                if level == 3:
                    new_pos = random_move(current_pos, wallPos)
                    if new_pos:
                        ghost.set_RC(new_pos[0], new_pos[1])
                else:
                    ghost_path = A_star(current_pos, pacman_pos, wallPos)
                    if ghost_path and len(ghost_path) > 0:
                        next_pos = ghost_path[0]
                        ghost.set_RC(next_pos[0], next_pos[1])
                            
            playerPath = algoFunc(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos)
    
        if playerPath:
            player.set_RC(playerPath[0][0], playerPath[0][1])
            playerPath.pop(0)
            isMoving = True
        else:
            alive = False
        
        totalStep += 1
        if (level == 5 and totalStep % 20 == 0):
            ghostList.append(Ghost(_N // 2, _M // 2))

     
        for food in foodList:
            if player.get_RC() == food.get_RC():
                totalFood += 1
                foodList.remove(food)
                break
        
        if not alive or not foodList:
            showEndPage(alive)
            break
    
    showMenu()


if __name__ == '__main__':
    showMenu()
    pg.quit()