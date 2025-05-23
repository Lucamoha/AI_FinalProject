import pygame as pg
from constants import *
import os
import sys

pg.init()
font = pg.font.SysFont('Arial', 40)
lbFont = pg.font.SysFont('Arial', 100)
background = pg.image.load('assets/background.jpg')

totalPage = 4

class Button:
    def __init__(self, x, y, width, height, screen, btText: str = "none", function = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.btText = btText
        self.screen = screen
        self.function = function

        self.buttonSurface = pg.Surface((self.width, self.height))
        self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
        self.buttonTextSurface = font.render(btText, True, BLACK)

        self.fillColors = {
            'normal': '#FFD700',
            'hover': '#FFA500',
            'pressed': '#FF8C00',
        }
    
    def animation(self):
        mousePos = pg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pg.mouse.get_pressed()[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.function()
                return True

        self.buttonSurface.blit(self.buttonTextSurface, [
            self.buttonRect.width / 2 - self.buttonTextSurface.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonTextSurface.get_rect().height / 2
        ])
        pg.draw.rect(self.buttonSurface, ORANGE, (0, 0, self.width, self.height), 5)
        self.screen.blit(self.buttonSurface, self.buttonRect)

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.isDone = False
        self.clicked = False
        self.listMap = []

        self.currentPage = 0
        self.Level = 1
        self.Map = 1
        self.Algo = ""
        
        self.btChooseLevel = Button(WIDTH // 2 - 125, HEIGHT - 170, 250, 100, screen, "Choose Level", self._nextPage)

        self.btBack = Button(20, 20, 100, 50, screen, "<<", self._backPage)

        self.btLevel_01 = Button(150, 200, 200, 100, screen, "Level 1", self._loadMapLv1)
        self.btLevel_02 = Button(500, 200, 200, 100, screen, "Level 2", self._loadMapLv2)
        self.btLevel_03 = Button(850, 200, 200, 100, screen, "Level 3", self._loadMapLv3)
        self.btLevel_04 = Button(325, 350, 200, 100, screen, "Level 4", self._loadMapLv4)
        self.btLevel_05 = Button(675, 350, 200, 100, screen, "Level 5", self._loadMapLv5)

        self.btPrevMap = Button(40, HEIGHT - 40 - 50, 100, 50, screen, "<", self._prevMap)
        self.btNextMap = Button(WIDTH - 100 - 40, HEIGHT - 40 - 50, 100, 50, screen, ">", self._nextMap)
        self.btChooseAlgo = Button(WIDTH // 2 - 150, HEIGHT - 40 - 60, 300, 70, screen, "Choose Algorithm", self._nextPage)

        self.btBFS = Button(75, 180, 300, 70, screen, "BFS", self._BFS)
        self.btBeamSearch = Button(450, 180, 300, 70, screen, "BeamSearch", self._BeamSearch)
        self.btBacktracking = Button(825, 180, 300, 70, screen, "BackTracking", self._Backtracking)
        self.btPartial_Observation = Button(75, 290, 300, 70, screen, "Partial Observation", self._Partial_Observation)
        self.btQLearning = Button(450, 290, 300, 70, screen, "Q-Learning", self._QLearning)
        self.btA_Star = Button(825, 290, 300, 70, screen, "A_Star", self._A_Star)
        self.btPlayer = Button(450, 400, 300, 70, screen, "PLAYER", self._player)
    
    def _backPage(self):
        if self.clicked:
            self.currentPage -= 1
        self.clicked = False
    
    def _nextPage(self):
        if self.clicked:
            self.currentPage += 1
        self.clicked = False

    def _drawMap(self, fileMap):
        textSurface = font.render(f'LEVEL {self.Level} - MAP {self.Map}', True, WHITE)
        textWidth, textHeight = textSurface.get_size()
        self.screen.blit(textSurface, (WIDTH // 2 - textWidth // 2, 20))

        with open(fileMap, 'r') as file:
            map = file.readlines()
        
        N = int(map[0].split()[0])
        M = int(map[0].split()[1])

        sizeCell = 20
        count_ghost = 0
        widthMap = M * sizeCell
        heightMap = N * sizeCell
        map_X = WIDTH // 2 - widthMap // 2
        map_Y = 90

        backgroundSurface = pg.Surface((widthMap, heightMap))
        backgroundSurface.fill(BLACK)
        self.screen.blit(backgroundSurface, (map_X, map_Y))

        for i in range(N):
            for j in range(M):
                cell = int(map[i + 1].split()[j])
                x = j * sizeCell + map_X
                y = i * sizeCell + map_Y

                if cell == WALL:
                    image = pg.Surface([sizeCell, sizeCell], pg.SRCALPHA)
                    pg.draw.rect(image, (0, 0, 128), (0, 0, sizeCell, sizeCell))
                    pg.draw.rect(image, (0, 255, 255), (0, 0, sizeCell, sizeCell), 1)
                    self.screen.blit(image, (x, y))
                elif cell == FOOD:
                    image = pg.Surface([sizeCell // 2, sizeCell // 2])
                    image.fill(WHITE)
                    image.set_colorkey(WHITE)
                    pg.draw.ellipse(image, YELLOW, [0, 0, sizeCell // 2, sizeCell // 2])
                    self.screen.blit(image, (x + sizeCell // 4, y + sizeCell // 4))
                elif cell == GHOST:
                    image = pg.image.load(IMAGE_GHOST_PATH[count_ghost]).convert_alpha()
                    image = pg.transform.scale(image, (sizeCell, sizeCell))
                    self.screen.blit(image, (x, y))
                    count_ghost = (count_ghost + 1) % len(IMAGE_GHOST_PATH)

            player_Y = int(map[len(map) - 1].split()[0])
            player_X = int(map[len(map) - 1].split()[1])
            image = pg.image.load(IMAGE_PLAYER_PATH[0]).convert_alpha()
            image = pg.transform.scale(image, (sizeCell, sizeCell))

            x = player_X * sizeCell + map_X
            y = player_Y * sizeCell + map_Y

            self.screen.blit(image, (x, y))

    def _loadMapLv1(self):
        if self.clicked:
            self.Level = 1
            self.listMap = []
            for file in os.listdir('levels/Level1'):
                self.listMap.append('levels/Level1/' + file)
            self._nextPage()
        self.clicked = False

    def _loadMapLv2(self):
        if self.clicked:
            self.Level = 2
            self.listMap = []
            for file in os.listdir('levels/Level2'):
                self.listMap.append('levels/Level2/' + file)
            self._nextPage()
        self.clicked = False

    def _loadMapLv3(self):
        if self.clicked:
            self.Level = 3
            self.listMap = []
            for file in os.listdir('levels/Level3'):
                self.listMap.append('levels/Level3/' + file)
            self._nextPage()
        self.clicked = False
    
    def _loadMapLv4(self):
        if self.clicked:
            self.Level = 4
            self.listMap = []
            for file in os.listdir('levels/Level4'):
                self.listMap.append('levels/Level4/' + file)
            self._nextPage()
        self.clicked = False

    def _loadMapLv5(self):
        if self.clicked:
            self.Level = 5
            self.listMap = []
            for file in os.listdir('levels/Level5'):
                self.listMap.append('levels/Level5/' + file)
            self._nextPage()
        self.clicked = False

    def _nextMap(self):
        if self.clicked:
            self.Map = self.Map % len(self.listMap) + 1
        
        self.clicked = False

    def _prevMap(self):
        if self.clicked:
            self.Map -= 1
            if self.Map == 0:
                self.Map += len(self.listMap)
        
        self.clicked = False
    
    def _BFS(self):
        if self.clicked:    
            self.Algo = "BFS"
            self.isDone = True
        self.clicked = False
    
    def _BeamSearch(self):
        if self.clicked:    
            self.Algo = "BeamSearch"
            self.isDone = True
        self.clicked = False
    
    def _Backtracking(self):
        if self.clicked:    
            self.Algo = "Backtracking"
            self.isDone = True
        self.clicked = False

    def _Partial_Observation(self):
        if self.clicked:    
            self.Algo = "Partial_Observation"
            self.isDone = True
        self.clicked = False

    def _QLearning(self):
        if self.clicked:    
            self.Algo = "QLearning"
            self.isDone = True
        self.clicked = False

    def _A_Star(self):
        if self.clicked:    
            self.Algo = "A_Star"
            self.isDone = True
        self.clicked = False

    def _player(self):
        if self.clicked:    
            self.Algo = "Manual"
            self.isDone = True
        self.clicked = False

    def main(self):
        while not self.isDone:
            self.clicked = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.clicked = True

            if self.currentPage == 0:
                self.screen.blit(background, (0, 0))
                self.btChooseLevel.animation()
            elif self.currentPage == 1:
                self.screen.blit(background, (0, 0))
                self.Map = 1
                self.btBack.animation()
                self.btLevel_01.animation()
                self.btLevel_02.animation()
                self.btLevel_03.animation()
                self.btLevel_04.animation()
                self.btLevel_05.animation()
            elif self.currentPage == 2:
                self.screen.blit(background, (0, 0))
                self._drawMap(f"levels/Level{self.Level}/map{self.Map}.txt")
                self.btBack.animation()
                self.btPrevMap.animation()
                self.btNextMap.animation()
                self.btChooseAlgo.animation()
            elif self.currentPage == 3:
                self.screen.blit(background, (0, 0))
                self.btBack.animation()
                self.btBFS.animation()
                self.btBeamSearch.animation()
                self.btBacktracking.animation()
                self.btPartial_Observation.animation()
                self.btQLearning.animation()
                self.btA_Star.animation()
                self.btPlayer.animation()
            
            pg.display.flip()

        return self.Level, self.Map, self.Algo