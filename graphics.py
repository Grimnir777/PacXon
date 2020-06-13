import pygame
from pygame.locals import *
from pacman import Pacman
from ghost import Ghost
from boxes import Boxes


class Graphics(object):
    """docstring for Graphics"""

    def __init__(self):
        self.boxes_array = [[Boxes.EMPTY for i in range(0, 25)] for j in range(0, 25)]
        self.init_borders()

        self.tabPath = [(-1, -1) for i in range(0, 525)]
        self.indexTabPath = 0

        self.screen = pygame.display.set_mode((500, 500))

        self.pacman = Pacman()
        self.ghost = Ghost()

        self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.PACMAN
        self.boxes_array[self.ghost.posX][self.ghost.posY] = Boxes.GHOST

        self.render(self.pacman)

    def init_borders(self):
        for i in range(0, 25):
            self.boxes_array[i][0] = Boxes.CLOSED
            self.boxes_array[0][i] = Boxes.CLOSED
        for j in range(0, 25):
            self.boxes_array[j][24] = Boxes.CLOSED
            self.boxes_array[24][j] = Boxes.CLOSED

    def update(self, key):
        if key == K_UP:
            if self.pacman.posX >= 1:
                self.pacman.change_direction(key)
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.CLOSED
                self.pacman.move_up()
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.EMPTY) \
                        and (not self.pacman.is_filling):
                    # Starting filling
                    self.pacman.is_filling = True
                    self.pacman.filling_left_side = True
                    self.pacman.filling_right_side = True
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.CLOSED) \
                        and (not self.pacman.is_filling):
                    # Stopping filling filling
                    self.pacman.is_filling = False
                    print("Right side ? " + str(self.pacman.filling_right_side))
                    print("Left side ? " + str(self.pacman.filling_left_side))
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.PACMAN

                # Checking which side is the ghost
                if self.pacman.is_filling:
                    if self.pacman.posX < self.ghost.posX and self.pacman.posY < self.ghost.posY:
                        self.pacman.filling_right_side = False
                    if self.pacman.posX > self.ghost.posX and self.pacman.posY > self.ghost.posY:
                        self.pacman.filling_left_side = False

        elif key == K_DOWN:
            if self.pacman.posX <= 23:
                self.pacman.change_direction(key)
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.CLOSED
                self.pacman.move_down()
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.EMPTY) \
                        and (not self.pacman.is_filling):
                    self.pacman.is_filling = True
                    self.pacman.filling_left_side = True
                    self.pacman.filling_right_side = True
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.CLOSED) \
                        and (not self.pacman.is_filling):
                    self.pacman.is_filling = False
                    print("Right side ? " + str(self.pacman.filling_right_side))
                    print("Left side ? " + str(self.pacman.filling_left_side))
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.PACMAN

                self.pacman.check_filling_side(self.ghost.posX, self.ghost.posY)

        elif key == K_LEFT:
            if self.pacman.posY >= 1:
                self.pacman.change_direction(key)
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.CLOSED
                self.pacman.move_left()
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.EMPTY) \
                        and (not self.pacman.is_filling):
                    self.pacman.is_filling = True
                    self.pacman.filling_left_side = True
                    self.pacman.filling_right_side = True
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.CLOSED) \
                        and (not self.pacman.is_filling):
                    self.pacman.is_filling = False
                    print("Right side ? " + str(self.pacman.filling_right_side))
                    print("Left side ? " + str(self.pacman.filling_left_side))
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.PACMAN

                self.pacman.check_filling_side(self.ghost.posX, self.ghost.posY)

        elif key == K_RIGHT:
            if self.pacman.posY <= 23:
                self.pacman.change_direction(key)
                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.CLOSED
                self.pacman.move_right()
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.EMPTY) \
                        and (not self.pacman.is_filling):
                    self.pacman.is_filling = True
                    self.pacman.filling_left_side = True
                    self.pacman.filling_right_side = True
                if (self.boxes_array[self.pacman.posX][self.pacman.posY] == Boxes.CLOSED) \
                        and (not self.pacman.is_filling):
                    self.pacman.is_filling = False
                    print("Right side ? " + str(self.pacman.filling_right_side))
                    print("Left side ? " + str(self.pacman.filling_left_side))

                self.boxes_array[self.pacman.posX][self.pacman.posY] = Boxes.PACMAN
                self.pacman.check_filling_side(self.ghost.posX, self.ghost.posY)

        elif key == K_r:
            """reinitialisation"""

    def render(self, pac):
        for i in range(0, 25):
            for j in range(0, 25):
                if self.boxes_array[i][j] == Boxes.EMPTY:
                    pygame.draw.rect(self.screen, (0, 0, 0), (j * 20, i * 20, 21, 21))
                elif self.boxes_array[i][j] == Boxes.CLOSED:
                    pygame.draw.rect(self.screen, (17, 47, 134), (j * 20, i * 20, 21, 21))
                    pygame.draw.rect(self.screen, (0, 64, 255), (j * 20, i * 20, 21, 21), 1)
                elif self.boxes_array[i][j] == Boxes.OPEN:
                    pygame.draw.rect(self.screen, (7, 4, 134), (j * 20, i * 20, 21, 21))
                elif self.boxes_array[i][j] == Boxes.GHOST:
                    pygame.draw.circle(self.screen, (0, 255, 0), ((i * 20) + 10, (j * 20) + 10), 9, 0)

        self.screen.blit(pac.picture, (self.pacman.posY * 20, self.pacman.posX * 20))
        pygame.display.update()
        pygame.display.flip()

    def update_ghost_position(self, x, y):
        self.boxes_array[x][y] = Boxes.GHOST

    def print_tab(self):
        string_value = ""
        for row in self.boxes_array:
            for box in row:
                string_value += " {} ".format(str(box.value))
            string_value += "\n"
        print(string_value)
