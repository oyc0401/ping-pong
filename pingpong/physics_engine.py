from enum import Enum


class RectangleStruct:
    min = (0, 0)
    max = (0, 0)

    def __init__(self, min, max):
        self.min = min
        self.max = max

    def isIn(self, x, y, radius):
        minX, minY = self.min
        maxX, maxY = self.max
        if minX - radius <= x <= maxX + radius and minY - radius <= y <= maxY + radius:
            return True
        else:
            return False


class Direction(Enum):
    top = (0, 1, 1)
    bottom = (0, 1, -1)
    left = (1, 0, 1)
    right = (1, 0, -1)


class Wall:
    number = 0
    wall_x = 0
    wall_y = 0
    direction = 0

    def __init__(self, number, popo):
        self.number = number
        self.wall_x, self.wall_y, self.direction = popo.value


class Board:
    structs = []
    walls = []

    def addWall(self, wall):
        self.walls.append(wall)

    # def addRectangle(self, min, max):
    #     self.structs.append(RectangleStruct(min, max))
