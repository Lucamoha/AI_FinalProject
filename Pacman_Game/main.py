import pygame as pg
import time

from constants import *
from objects.menu import Menu
from objects.food import Food
from objects.player import Player
from objects.ghost import Ghost
from Algorithms.BFS import BFS
from Algorithms.DFS import DFS


level = 1
map = 1     # STT map
algo = ""

_N = 0
_M = 0
wallPos = []
foodList = []
ghostList = []

player = Player(0, 0, 0)
totalStep = 0
totalFood = 0
counter = 0
totalTime = 0


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


def initMap(fileMap):
    '''Khởi tạo map, các list đối tượng từ fileMap sau khi người dùng hoàn thành Menu'''
    global totalTime
    totalTime = 0

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


def drawMap():
    global wallPos, screen, foodList, ghostList, counter

    while True:
        screen.fill(BLACK)

        counter += 1
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
        
        pg.display.flip()

        if player.reached_target():
            break
        else:
            player.move()


def showMenu():
    global level, map, algo, screen
    menu = Menu(screen)
    level, map, algo = menu.main()

    initMap(f"levels/Level{level}/map{map}.txt")
    main()


def main():
    global level, map, algo, totalStep, totalFood, totalTime
    global screen, foodList, ghostList, wallPos
    
    totalStep = 0
    totalFood = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return showMenu()
        
        drawMap()
        pg.display.flip()
        clock.tick(6)
        
        if algo == "BFS":
            playerPath, alive = BFS(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos)
        elif algo == "DFS":
            playerPath, alive = DFS(player.get_RC(), [food.get_RC() for food in foodList], [ghost.get_RC() for ghost in ghostList], wallPos)

        # if level == 3:
        #     ghostPath = GhostMove()

        if playerPath:
            player.set_RC(playerPath[0][0], playerPath[0][1])
        
        totalStep += 1
        for food in foodList:
            if player.get_RC() == food.get_RC():
                totalFood += 1
                foodList.remove(food)
                break
        
        if not alive or not foodList:
            title = f"--Level: {level} - Map: {map} - Algo: {algo}--"
            print(title)
            print(f"Status: {"Die" if not alive else "Win"}")
            print(f"Steps: {totalStep}")
            print(f"Food: {totalFood}")
            print(f"Time: {totalTime}")
            print('-' * len(title))
            break
    
    showMenu()


if __name__ == '__main__':
    showMenu()
    pg.quit()