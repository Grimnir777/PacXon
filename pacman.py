import pygame
from pygame.locals import *
from point import Point


class Pacman(object):
    """Pac Man with its coordinates"""

    def __init__(self):
        self.position = Point(0, 0)

        self.picture_right = pygame.image.load("images/pacmanright.png").convert_alpha()
        self.picture_left = pygame.image.load("images/pacmanleft.png").convert_alpha()
        self.picture_up = pygame.image.load("images/pacmanup.png").convert_alpha()
        self.picture_down = pygame.image.load("images/pacmandown.png").convert_alpha()
        self.picture = self.picture_right

        self.is_filling = False
        self.filling_origin = Point(-1, -1)

    def move_up(self) -> None:
        self.position.shift(-1, 0)

    def move_down(self) -> None:
        self.position.shift(1, 0)

    def move_left(self) -> None:
        self.position.shift(0, -1)

    def move_right(self) -> None:
        self.position.shift(0, 1)

    def change_direction(self, key) -> None:
        if key == K_RIGHT:
            self.picture = self.picture_right
        elif key == K_LEFT:
            self.picture = self.picture_left
        elif key == K_UP:
            self.picture = self.picture_up
        elif key == K_DOWN:
            self.picture = self.picture_down

    def set_filling_origin(self, origin: Point) -> None:
        self.filling_origin = origin
