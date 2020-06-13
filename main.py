import pygame
from pygame.locals import *
from graphics import Graphics

pygame.init()

graphics = Graphics()

run = True
pygame.key.set_repeat(150, 100)
graphics.print_tab()
while run:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            run = 0

        if event.type == KEYDOWN:
            graphics.update(event.key)
            graphics.render(graphics.pacman)
            graphics.print_tab()
            print(graphics.pacman.is_filling)

z = input("saisir 0 pour finir")
print(z)
pygame.quit()
