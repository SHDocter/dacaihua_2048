import pygame
import time
import sys
class Settings():
    def __init__(self):
        # 屏幕设置
        self.screen_width = 400
        self.screen_height = 600
        self.screen_bg = pygame.image.load('images/bg_1.png')
        self.screen_rect = self.screen_bg.get_rect()
        self.numlen = 100
def NumImage(num, screen, x, y):
    if num == 2:
        n = pygame.image.load('images/2.png')
    elif num == 4:
        n = pygame.image.load('images/4.png')
    elif num == 8:
        n = pygame.image.load('images/8.png')
    elif num == 16:
        n = pygame.image.load('images/16.png')
    elif num == 32:
        n = pygame.image.load('images/32.png')
    elif num == 64:
        n = pygame.image.load('images/64.png')
    elif num == 128:
        n = pygame.image.load('images/128.png')
    elif num == 256:
        n = pygame.image.load('images/256.png')
    elif num == 512:
        n = pygame.image.load('images/512.png')
    elif num == 1024:
        n = pygame.image.load('images/1024.png')
    else:
        n = pygame.image.load('images/2048.png')
    r = n.get_rect()
    r.centerx = x
    r.centery = y
    screen.blit(n, r)
def SoFImage(x,screen):
    if x==0:
        time.sleep(2)
        n=pygame.image.load('images/2048_Failed.png')
        screen.blit(n, (20,175))
        pygame.display.update()
        time.sleep(10)
        sys.exit()
    elif x==1:
        time.sleep(2)
        n = pygame.image.load('images/2048_Succeed.png')
        screen.blit(n, (20, 175))
        pygame.display.update()
        time.sleep(10)
        sys.exit()
def UpdateScreen(GameList, set, screen):
    screen.blit(set.screen_bg, set.screen_rect)
    y = set.numlen * 2.5
    for i in range(4):
        x = set.numlen * 0.5
        for j in range(4):
            if GameList[i,j] != 0:
                NumImage(GameList[i,j], screen, x, y)
            x += set.numlen
        y += set.numlen
