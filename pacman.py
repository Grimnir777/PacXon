import pygame
from pygame.locals import *


class Pacman(object):
    """Pac Man with its coordinates"""

    def __init__(self):
        self.posX = 0
        self.posY = 0

        self.picture_right = pygame.image.load("images/pacmanright.png").convert_alpha()
        self.picture_left = pygame.image.load("images/pacmanleft.png").convert_alpha()
        self.picture_up = pygame.image.load("images/pacmanup.png").convert_alpha()
        self.picture_down = pygame.image.load("images/pacmandown.png").convert_alpha()

        self.picture = self.picture_right
        self.is_filling = False
        self.filling_right_side = True
        self.filling_left_side = True

    def move_up(self):
        self.posX -= 1

    def move_down(self):
        self.posX += 1

    def move_left(self):
        self.posY -= 1

    def move_right(self):
        self.posY += 1

    def change_direction(self, key):
        if key == K_RIGHT:
            self.picture = self.picture_right
        elif key == K_LEFT:
            self.picture = self.picture_left
        elif key == K_UP:
            self.picture = self.picture_up
        elif key == K_DOWN:
            self.picture = self.picture_down

    def check_filling_side(self, ghost_pos_x: int, ghost_pos_y: int) -> None:
        if self.is_filling:
            if self.posX < ghost_pos_x and self.posY < ghost_pos_y:
                self.filling_right_side = False
            if self.posX > ghost_pos_x and self.posY > ghost_pos_y:
                self.filling_left_side = False
