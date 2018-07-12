import pygame
from pygame.locals import *
class pacman(object):
    """Pac Man with its coordonates"""
    def __init__(self):
        self.posX = 0
        self.posY = 0

        self.pRight = pygame.image.load("img/pacmanright.png").convert_alpha()
        self.pLeft  = pygame.image.load("img/pacmanleft.png").convert_alpha()
        self.pUp    = pygame.image.load("img/pacmanup.png").convert_alpha()
        self.pDown  = pygame.image.load("img/pacmandown.png").convert_alpha()
        
        self.p = self.pRight
        self.fill = False

    def changeDirection(self, key):
        if(key == K_RIGHT):
            self.p = self.pRight
        elif(key == K_LEFT):
            self.p = self.pLeft
        elif(key == K_UP):
            self.p = self.pUp
        elif(key == K_DOWN):
            self.p = self.pDown

    def initFill():
        self.fill = True

