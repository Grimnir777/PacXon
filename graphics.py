import pygame
from pygame.locals import *
from pacman import Pacman
from ghost import Ghost
from boxes import Boxes
from point import Point

BOX_SIZE = 20


class Graphics(object):
    """docstring for Graphics"""

    def __init__(self):
        self.boxes_array = [[Boxes.EMPTY for i in range(0, 25)] for j in range(0, 25)]
        self.inspected_boxes = []
        self.propagated_boxes = []
        self.init_borders()

        self.screen = pygame.display.set_mode((500, 500))

        self.pacman = Pacman()
        self.ghost = Ghost()

        self.boxes_array[self.pacman.position.x][self.pacman.position.y] = Boxes.PACMAN
        self.boxes_array[self.ghost.position.x][self.ghost.position.y] = Boxes.GHOST

        self.render(self.pacman)

    def init_borders(self):
        for i in range(0, 25):
            self.boxes_array[i][0] = Boxes.CLOSED
            self.boxes_array[0][i] = Boxes.CLOSED
        for j in range(0, 25):
            self.boxes_array[j][24] = Boxes.CLOSED
            self.boxes_array[24][j] = Boxes.CLOSED

    def check_start_filling(self):
        print("Checking start filling")
        if (self.boxes_array[self.pacman.position.x][self.pacman.position.y] == Boxes.EMPTY) \
                and (not self.pacman.is_filling):
            print("Starting filling", self.pacman.position)
            self.pacman.is_filling = True
            self.pacman.filling_origin = Point(self.pacman.position.x, self.pacman.position.y)

    def has_been_inspected(self, position: Point):
        for point in self.inspected_boxes:
            if position.x == point.x and position.y == point.y:
                return True
        return False

    def has_been_propagated(self, position: Point):
        for point in self.propagated_boxes:
            if position.x == point.x and position.y == point.y:
                return True
        return False

    def check_end_filling(self):
        if (self.boxes_array[self.pacman.position.x][self.pacman.position.y] == Boxes.CLOSED) \
                and self.pacman.is_filling:
            print("Stop filling", self.pacman.position)
            self.pacman.is_filling = False

            # check free sides of origin
            origin_top = Point(self.pacman.filling_origin.x - 1, self.pacman.filling_origin.y)
            origin_bottom = Point(self.pacman.filling_origin.x + 1, self.pacman.filling_origin.y)
            origin_left = Point(self.pacman.filling_origin.x, self.pacman.filling_origin.y - 1)
            origin_right = Point(self.pacman.filling_origin.x, self.pacman.filling_origin.y + 1)

            # If two sides (top and bottom are free)
            if self.empty_side(origin_top) and self.empty_side(origin_bottom):
                top_to_fill = self.inspect_side(origin_top)
                self.inspected_boxes = []
                if top_to_fill:
                    self.propagate(origin_top)
                    self.propagated_boxes = []
                bottom_to_fill = self.inspect_side(origin_bottom)
                self.inspected_boxes = []
                if bottom_to_fill:
                    self.propagate(origin_bottom)
                    self.propagated_boxes = []

            # If two sides (left and right are free)
            elif self.empty_side(origin_left) and self.empty_side(origin_right):
                left_to_fill = self.inspect_side(origin_left)
                self.inspected_boxes = []
                if left_to_fill:
                    self.propagate(origin_left)
                    self.propagated_boxes = []
                right_to_fill = self.inspect_side(origin_right)
                self.inspected_boxes = []
                if right_to_fill:
                    self.propagate(origin_right)
                    self.propagated_boxes = []

    def empty_side(self, position: Point):
        return not self.is_out_of_border(position) and self.boxes_array[position.x][position.y] == Boxes.EMPTY

    @staticmethod
    def is_out_of_border(position: Point):
        return position.x < 0 or position.x > 24 or position.y < 0 or position.y > 24

    def inspect_side(self, position: Point):
        if self.is_out_of_border(position) or \
                self.has_been_inspected(position) or \
                self.boxes_array[position.x][position.y] == Boxes.CLOSED:
            return True
        self.inspected_boxes.append(Point(position.x, position.y))
        if self.inspect_side(Point(position.x - 1, position.y)) is False:
            return False
        if self.inspect_side(Point(position.x + 1, position.y)) is False:
            return False
        if self.inspect_side(Point(position.x, position.y - 1)) is False:
            return False
        if self.inspect_side(Point(position.x, position.y + 1)) is False:
            return False
        if self.boxes_array[position.x][position.y] == Boxes.GHOST:
            return False
        self.inspected_boxes.append(Point(position.x, position.y))
        return True

    def propagate(self, position: Point):
        if self.is_out_of_border(position)\
                or self.has_been_propagated(position)\
                or self.boxes_array[position.x][position.y] == Boxes.CLOSED:
            return True
        self.boxes_array[position.x][position.y] = Boxes.CLOSED
        self.propagated_boxes.append(Point(position.x, position.y))
        self.propagate(Point(position.x - 1, position.y))
        self.propagate(Point(position.x + 1, position.y))
        self.propagate(Point(position.x, position.y - 1))
        self.propagate(Point(position.x, position.y + 1))
        return True

    def update(self, key):
        self.boxes_array[self.pacman.position.x][self.pacman.position.y] = Boxes.CLOSED
        if key == K_UP:
            if self.pacman.position.x > 0:
                self.pacman.change_direction(key)
                self.pacman.move_up()

        elif key == K_DOWN:
            if self.pacman.position.x < 24:
                self.pacman.change_direction(key)
                self.pacman.move_down()

        elif key == K_LEFT:
            if self.pacman.position.y > 0:
                self.pacman.change_direction(key)
                self.pacman.move_left()

        elif key == K_RIGHT:
            if self.pacman.position.y < 24:
                self.pacman.change_direction(key)
                self.pacman.move_right()
        elif key == K_r:
            """reinitialisation"""
        self.check_start_filling()
        self.check_end_filling()
        self.boxes_array[self.pacman.position.x][self.pacman.position.y] = Boxes.PACMAN
        print("Pacman position", self.pacman.position)
        print("Filling origin position", self.pacman.filling_origin)

    def render(self, pac):
        for i in range(0, 25):
            for j in range(0, 25):
                if self.boxes_array[i][j] == Boxes.EMPTY:
                    pygame.draw.rect(self.screen, (0, 0, 0), (j * BOX_SIZE, i * BOX_SIZE, 21, 21))
                elif self.boxes_array[i][j] == Boxes.CLOSED:
                    pygame.draw.rect(self.screen, (17, 47, 134), (j * BOX_SIZE, i * BOX_SIZE, 21, 21))
                    pygame.draw.rect(self.screen, (0, 64, 255), (j * BOX_SIZE, i * BOX_SIZE, 21, 21), 1)
                elif self.boxes_array[i][j] == Boxes.OPEN:
                    pygame.draw.rect(self.screen, (7, 4, 134), (j * BOX_SIZE, i * BOX_SIZE, 21, 21))
                elif self.boxes_array[i][j] == Boxes.GHOST:
                    pygame.draw.circle(self.screen, (0, 255, 0), ((i * BOX_SIZE) + int(BOX_SIZE / 2), (j * BOX_SIZE) + int(BOX_SIZE / 2)), 9, 0)

        self.screen.blit(pac.picture, (self.pacman.position.y * BOX_SIZE, self.pacman.position.x * BOX_SIZE))
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
