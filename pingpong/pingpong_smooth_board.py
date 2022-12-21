import time

from cs1graphics import *
from .vectors_math import *
from .physics_engine import *

delay = 0.05  # 초당 20번
collision_factor = 0.7


class MyBall(Circle):
    VectorX = 0
    VectorY = 0
    friction_factor = 0.005
    xp = 0  # = whiteBall.getReferencePoint().getX()
    yp = 0  # = whiteBall.getReferencePoint().getY()
    radius = 10

    board = 2

    def __init__(self, radius, x, y, ):
        super(MyBall, self).__init__(radius, Point(x, y))
        self.setPosition(x, y)

    def start(self, tick):
        for i in range(tick):
            whiteBall.going(1)

    def setBoard(self, board):
        self.board = board

    def going(self, t):
        canGo = True
        for www in self.board.walls:
            wallNum = www.number
            wall_x = www.wall_x
            wall_y = www.wall_y
            wall_direction = www.direction

            point = self.xp * wall_x + self.yp * wall_y
            velocity = self.VectorX * wall_x + self.VectorY * wall_y
            directionTrue = velocity * wall_direction
            nextLevel = point + velocity - wallNum

            if directionTrue <= 0 and nextLevel * wall_direction <= self.radius:
                canGo = False
                firstTime = np.abs(point - self.radius * wall_direction - wallNum) / np.abs(velocity)
                self.go(firstTime * t)
                self.collision((wall_x, wall_y))
                self.going((1 - firstTime) * t)
                # self.go(1 - firstTime)

        if canGo:
            whiteBall.go(t)

    def setPosition(self, x, y):
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

    # def get_speed(self):
    #     return (self.VectorX ** 2 + self.VectorY ** 2) ** (1 / 2)

    # def friction(self):
    #     # 마찰력에 의해 속도가 줄어든다.
    #     speed = self.get_speed()
    #     minus_speed = speed - self.friction_factor
    #
    #     if minus_speed > 0:
    #         ratio = minus_speed / speed
    #
    #         self.VectorX *= ratio
    #         self.VectorY *= ratio
    #     else:
    #         self.VectorX = 0
    #         self.VectorY = 0

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


# def get_location(angle):
#     dan = theta_to_danwi(angle * np.pi / 180)
#     large = multy_tuple((20 ** 2 + 110 ** 2) ** (0.5), dan)
#     return sum_tuple(large, (200, 300))


class PingPong:
    width = 0
    height = 0
    canvas = 0
    board = 0
    ball = 0

    def __init__(self, width, height, thick):
        self.width = width
        self.height = height
        self.canvas = Canvas(400, 600)
        self.canvas.setBackgroundColor((48, 108, 227))

        self.setTable(thick, 600, thick / 2, 300)
        self.setTable(40, 600, 400, 300)
        self.setTable(400, 40, 200, 0)
        self.setTable(400, 40, 200, 600)

        self.board = Board(400, 600, 20)

    def setBall(self, ball):
        self.ball = ball
        self.ball.setBoard(self.board)
        self.ball.setFillColor('white')
        self.ball.setBorderWidth(0)
        self.canvas.add(whiteBall)

    def setTable(self, x, y, X, Y):
        table = Rectangle(x, y, Point(X, Y))
        table.setFillColor((71, 62, 58))
        table.setBorderWidth(0)
        self.canvas.add(table)

    def start(self, time):
        whiteBall.start(time)

    def finish(self):
        self.canvas.wait()
        self.canvas.close()


pingPong = PingPong(400, 600, 20)

whiteBall = MyBall(10, 100, 75)
whiteBall.setVelocity(-6 * 1, -4 * 1)

pingPong.setBall(whiteBall)

pingPong.start(300)

print("종료")
pingPong.finish()
