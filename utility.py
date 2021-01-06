import pygame as pg
from constants import boxsize

def drawBoard(win):
    win.fill((75,75,75))
    for i in range(8):
        for j in range(i%2,8,2):
            pg.draw.rect(win,(255,255,255),(boxsize*i,boxsize*j,boxsize,boxsize))

def isInBoard(pos):
    return pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7

def isBlackCell(pos):
    if pos[0] % 2 == 0:
        if pos[1] % 2 == 0:
            return False
        else:
            return True
    else:
        if pos[1] % 2 == 0:
            return True
        else:
            return False
