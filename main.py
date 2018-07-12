import pygame
from pygame.locals import *
from graphics import graphics



pygame.init()

graphic = graphics()


run = True
pygame.key.set_repeat(150,100)
graphic.printTab()
while run:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = 0

        if event.type == KEYDOWN:
            graphic.update(event.key)
            graphic.render(graphic.pac)
            graphic.printTab()
            print(graphic.pac.fill)
    

z=input("saisir 0 pour finir")
print(z)
pygame.quit();