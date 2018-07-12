import pygame
from pygame.locals import *
from pacman import pacman
from ghost import ghost


class graphics(object):
    """docstring for Graphics"""
    def __init__(self):
        self.tabScreen = [[0 for i in range(0,25)]for j in range(0,25)]
        for i in range(0,25):
            self.tabScreen[i][0]=1
            self.tabScreen[0][i]=1
        for j in range(0,25):
            self.tabScreen[j][24]=1
            self.tabScreen[24][j]=1

        self.tabPath = [(-1,-1) for i in range (0,525)]
        self.indexTabPath = 0

        self.screen = pygame.display.set_mode((500, 500))

        self.pac = pacman()
        self.ghost = ghost()

        self.tabScreen[self.pac.posX][self.pac.posY]=3
        self.tabScreen[self.ghost.posX][self.ghost.posY]=4

        self.render(self.pac)


    

    def update(self, key):
        if key == K_UP:
            if(self.pac.posX>=1):
                self.pac.changeDirection(key)
                self.tabScreen[self.pac.posX][self.pac.posY]=1
                self.pac.posX-=1
                if(self.tabScreen[self.pac.posX][self.pac.posY]==0) and (self.pac.fill == False):
                    self.pac.fill = True
                if(self.tabScreen[self.pac.posX][self.pac.posY]==1) and (self.pac.fill == True):
                    self.pac.fill = False
                self.tabScreen[self.pac.posX][self.pac.posY]=3

        elif key == K_DOWN:
            if(self.pac.posX<=23):
                self.pac.changeDirection(key)
                self.tabScreen[self.pac.posX][self.pac.posY]=1
                self.pac.posX+=1
                if(self.tabScreen[self.pac.posX][self.pac.posY]==0) and (self.pac.fill == False):
                    self.pac.fill = True
                if(self.tabScreen[self.pac.posX][self.pac.posY]==1) and (self.pac.fill == True):
                    self.pac.fill = False
                self.tabScreen[self.pac.posX][self.pac.posY]=3

        elif key == K_LEFT:
            if(self.pac.posY>=1):
                self.pac.changeDirection(key)
                self.tabScreen[self.pac.posX][self.pac.posY]=1
                self.pac.posY-=1
                if(self.tabScreen[self.pac.posX][self.pac.posY]==0) and (self.pac.fill == False):
                    self.pac.fill = True
                if(self.tabScreen[self.pac.posX][self.pac.posY]==1) and (self.pac.fill == True):
                    self.pac.fill = False
                self.tabScreen[self.pac.posX][self.pac.posY]=3

        elif key == K_RIGHT:
            if(self.pac.posY<=23):
                self.pac.changeDirection(key)
                self.tabScreen[self.pac.posX][self.pac.posY]=1
                self.pac.posY+=1
                if(self.tabScreen[self.pac.posX][self.pac.posY]==0) and (self.pac.fill == False):
                    self.pac.fill = True
                if(self.tabScreen[self.pac.posX][self.pac.posY]==1) and (self.pac.fill == True):
                    self.pac.fill = False
                self.tabScreen[self.pac.posX][self.pac.posY]=3

        elif key == K_r:
                """reinitialisation"""

    def render(self, pac):
        for i in range(0,25):
            for j in range(0,25):
                if self.tabScreen[i][j]==0:
                    pygame.draw.rect(self.screen,(0,0,0),(j*20,i*20,21,21))
                elif self.tabScreen[i][j]==1:
                    pygame.draw.rect(self.screen,(17,47,134),(j*20,i*20,21,21))
                    pygame.draw.rect(self.screen,(0,64,255),(j*20,i*20,21,21),1)
                elif self.tabScreen[i][j]==2:
                    pygame.draw.rect(self.screen,(7,4,134),(j*20,i*20,21,21))
                elif self.tabScreen[i][j]==4:
                    pygame.draw.circle(self.screen,(0,255,0),((i*20)+10,(j*20)+10),9,0)

        self.screen.blit(pac.p, (self.pac.posY*20, self.pac.posX * 20))
        pygame.display.update()
        pygame.display.flip()


    def updateGhostPos():
        self.tabScreen[x][y]=4
    

    def printTab(self):
        for row in self.tabScreen : print(row)