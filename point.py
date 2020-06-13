class Point:
    def __init__(self, x_init: int, y_init: int):
        self.x = x_init
        self.y = y_init

    def shift(self, x: int, y: int):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])