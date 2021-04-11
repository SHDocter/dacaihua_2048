import numpy as np
import pygame
import GameCalculation as GC
import GameImages as GI
import sys
icon=pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
def Operation(GameList,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                OperationNum=GC.Right(GameList)
                RuleNum = GC.Rule(GameList)
                if OperationNum==1:
                    if RuleNum==2:
                        GC.Random2or4(GameList)
                GI.SoFImage(RuleNum, screen)
            elif event.key == pygame.K_LEFT:
                OperationNum=GC.Left(GameList)
                RuleNum = GC.Rule(GameList)
                if OperationNum==1:
                    if RuleNum==2:
                        GC.Random2or4(GameList)
                GI.SoFImage(RuleNum, screen)
            elif event.key == pygame.K_DOWN:
                OperationNum=GC.Down(GameList)
                RuleNum=GC.Rule(GameList)
                if OperationNum==1:
                    if RuleNum==2:
                        GC.Random2or4(GameList)
                GI.SoFImage(RuleNum, screen)
            elif event.key == pygame.K_UP:
                OperationNum=GC.Up(GameList)
                RuleNum=GC.Rule(GameList)
                if OperationNum==1:
                    if RuleNum==2:
                        GC.Random2or4(GameList)
                GI.SoFImage(RuleNum, screen)
def RunGame():
    GameList = np.zeros((4, 4), dtype=int)
    set = GI.Settings()
    pygame.init()
    screen = pygame.display.set_mode((set.screen_width, set.screen_height))
    pygame.display.set_caption("2048            @K1snan")
    GC.Random2or4(GameList)
    GC.Random2or4(GameList)
    while True:
        Operation(GameList,screen)
        pygame.display.update()
        GI.UpdateScreen(GameList, set, screen)
RunGame()
