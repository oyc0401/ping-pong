import time

from cs1graphics import *
from mamama import *
from physics_engine import *

delay = 0.1  # 초당 20번
collision_factor = 0.7


class MyBall(Circle):
    VectorX = 0
    VectorY = 0
    friction_factor = 0.005
    xp = 0  # = whiteBall.getReferencePoint().getX()
    yp = 0  # = whiteBall.getReferencePoint().getY()
    radius = 10

    board=Board()

    def setBoard(self, board):
        self.board = board

    def going(self, t):

        xp = self.xp
        yp = self.yp
        vx = self.VectorX
        vy = self.VectorY
        r = self.radius

        canGo = True

        for www in board.walls:
            wallNum = www.number
            wall_x = www.wall_x
            wall_y = www.wall_y
            wall_direction = www.direction

            point = xp * wall_x + yp * wall_y
            velocity = vx * wall_x + vy * wall_y
            directionTrue = vx * wall_x * wall_direction
            nextLevel = point + velocity - wallNum

            if directionTrue <= 0 and nextLevel * wall_direction <= r:
                canGo = False
                firstTime = np.abs(point - r * wall_direction - wallNum) / np.abs(velocity)
                whiteBall.go(firstTime)
                whiteBall.collision((wall_x, wall_y))
                whiteBall.go(1 - firstTime)

        if canGo:
            whiteBall.go(1)

    def setXY(self, x, y):
        self.xp = x
        self.yp = y

    def go(self, t):
        self.xp += self.VectorX * t
        self.yp += self.VectorY * t
        super().move(self.VectorX * t, self.VectorY * t)
        # self.friction()
        time.sleep(delay * t)

    def setVelocity(self, speed_x, speed_y):
        self.VectorX = speed_x
        self.VectorY = speed_y

    def get_speed(self):
        return (self.VectorX ** 2 + self.VectorY ** 2) ** (1 / 2)

    def friction(self):
        # 마찰력에 의해 속도가 줄어든다.
        speed = self.get_speed()
        minus_speed = speed - self.friction_factor

        if minus_speed > 0:
            ratio = minus_speed / speed

            self.VectorX *= ratio
            self.VectorY *= ratio
        else:
            self.VectorX = 0
            self.VectorY = 0

    def collision(self, bubson):
        """ R = P + 2n(-P·n) """
        vector = (self.VectorX, self.VectorY)
        # print(vector)
        minus_vector = multy_tuple(-1, vector)

        # print(bubson)
        minus_Pn = inner(minus_vector, bubson)

        projection = multy_tuple(minus_Pn, bubson)
        double_projection = multy_tuple(2, projection)

        Reflection = sum_tuple(vector, double_projection)
        # print(Reflection)

        self.setVelocity(Reflection[0], Reflection[1])


def setTable(x, y, X, Y):
    table = Rectangle(x, y, Point(X, Y))
    table.setFillColor((71, 62, 58))
    table.setBorderWidth(0)
    canvas.add(table)


def get_location(angle):
    dan = theta_to_danwi(angle * np.pi / 180)
    large = multy_tuple((20 ** 2 + 110 ** 2) ** (0.5), dan)
    return sum_tuple(large, (200, 300))


width = 400
height = 600
canvas = Canvas(width + 100, height + 100)
canvas.setBackgroundColor((48, 108, 227))

setTable(20, 600, 10, 300)
setTable(40, 600, 400, 300)
setTable(400, 40, 200, 0)
setTable(400, 40, 200, 600)

board = Board()
board.addWall(Wall(20, Direction.top))
board.addWall(Wall(580, Direction.bottom))
board.addWall(Wall(20, Direction.left))
board.addWall(Wall(380, Direction.right))

# for w in board.walls:
#     print(w)

##################################################

# 흰 공

xxx = 100
yyy = 75
vx = 6
vy = -4

whiteBall = MyBall(10, Point(xxx, yyy))
whiteBall.setXY(xxx, yyy)
whiteBall.setVelocity(vx, vy)

whiteBall.setBoard(board)

whiteBall.setFillColor('white')
whiteBall.setBorderWidth(0)
canvas.add(whiteBall)

for i in range(300):
    whiteBall.going(1)

print("종료")
canvas.wait()
canvas.close()
