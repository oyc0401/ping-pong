import time

from cs1graphics import *

import numpy as np

delay = 0.01  # 초당 20번
collision_factor = 0.7


def inner(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]


def sum_tuple(v1, v2):
    a, b = v1
    A, B = v2

    return (a + A, b + B)


def multy_tuple(value, vector):
    a, b = vector
    a *= value
    b *= value
    return (a, b)


def theta_to_bubson(theta):
    # 세타로 단위법선벡터를 구한다
    return (np.sin(theta), np.cos(theta))


def theta_to_danwi(theta):
    # 세타로 단위벡터를 구한다
    return (np.cos(theta), np.sin(theta))

def angle_to_theta(angle):
    # 기울기를 세타로 바꿔준다
    return np.arctan(angle)


class myball(Circle):
    __VectorX = 3
    __VectorY = 5
    friction_factor = 0.005

    def go(self):
        super().move(self.__VectorX, self.__VectorY)
        self.friction()
        time.sleep(delay)

    def setVelocity(self, x, y):
        self.__VectorX = x
        self.__VectorY = y

    def get_speed(self):
        return (self.__VectorX ** 2 + self.__VectorY ** 2) ** (1 / 2)

    def friction(self):
        # 마찰력에 의해 속도가 줄어든다.
        speed = self.get_speed()
        minus_speed = speed - self.friction_factor

        if minus_speed > 0:
            ratio = minus_speed / speed

            self.__VectorX *= ratio
            self.__VectorY *= ratio
        else:
            self.__VectorX = 0
            self.__VectorY = 0

    def collision(self, bubson):
        """ R = P + 2n(-P·n) """
        vector = (self.__VectorX, self.__VectorY)
        print(vector)
        minus_vector = multy_tuple(-1, vector)

        print(bubson)
        minus_Pn = inner(minus_vector, bubson)

        projection = multy_tuple(minus_Pn, bubson)
        double_projection = multy_tuple(2, projection)

        Reflection = sum_tuple(vector, double_projection)
        print(Reflection)

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
canvas = Canvas(width, height)
canvas.setBackgroundColor((48, 108, 227))

setTable(40, 600, 0, 300)
setTable(40, 600, 400, 300)
setTable(400, 40, 200, 0)
setTable(400, 40, 200, 600)
##################################################

nowAngle = 0
wall = Rectangle(20,200, Point(200, 300))
wall.setFillColor((71, 62, 58))
wall.setBorderWidth(0)
wall.rotate(45)
canvas.add(wall)

# 흰 공
whiteBall = myball(10, Point(150, 550))
whiteBall.setFillColor('white')
whiteBall.setBorderWidth(0)
canvas.add(whiteBall)

r = 30
whiteBall.setVelocity(-6, -4)

tanacgle = (np.arctan(1/6) * 360 / (2 * np.pi))
t=0
isOut= True

while (whiteBall.get_speed() > 0):

    whiteBall.go()
    xp = whiteBall.getReferencePoint().getX()
    yp = whiteBall.getReferencePoint().getY()
    if xp < 0 + r:
        whiteBall.collision((1, 0))
    if yp < 0 + r:
        whiteBall.collision((0, -1))
    if xp > 400 - r:
        whiteBall.collision((-1, 0))
    if yp > 600 - r:
        whiteBall.collision((0, -1))

    nowAngle += 1
    wall.rotate(1)
    #print(t)

    x1, y1 = get_location(nowAngle + 270 + 45 - tanacgle)

    x2, y2 = get_location(nowAngle + 180 - 45 + tanacgle)

    x3, y3 = get_location(nowAngle + 90 + 45 - tanacgle)

    x4, y4 = get_location(nowAngle - 45 + tanacgle)


    D12 = (x2 - x1) * (yp - y1) - (xp - x1) * (y2 - y1)  # 1-2 번 왼쪽에 있으면 양수

    D34 = (x4 - x3) * (yp - y3) - (xp - x3) * (y4 - y3)  # 3-4 번 왼쪽에 있으면 양수

    D41 = (x1 - x4) * (yp - y4) - (xp - x4) * (y1 - y4)  # 4-1 번 왼쪽에 있으면 양수

    D23 = (x3 - x2) * (yp - y2) - (xp - x2) * (y3 - y2)  # 2-3 번 왼쪽에 있으면 양수

    bigger = -10000
    if D12 < 0 and D34 < 0 and D41 < 0 and D23 < 0 and isOut:
        if D12 > bigger:
            bigger = D12
        if D34 > bigger:
            bigger = D34
        if D41 > bigger:
            bigger = D41
        if D23 > bigger:
            bigger = D23

        print(bigger)
        if bigger == D12:
            print("D12")
            whiteBall.collision(theta_to_bubson((270 - 45 - nowAngle) * np.pi / 180))
        elif bigger == D34:
            print("D34")
            whiteBall.collision(theta_to_bubson((90 - 45 - nowAngle) * np.pi / 180))
        elif bigger == D41:
            print("D41")
            whiteBall.collision(theta_to_bubson((180 - 45 - nowAngle) * np.pi / 180))
        elif bigger == D23:
            print("D23")
            whiteBall.collision(theta_to_bubson((360 - 45 - nowAngle) * np.pi / 180))

        print("원 안이예요")
        isOut=False
    else:
        isOut=True
    t+=1

print("종료")
canvas.wait()
canvas.close()
