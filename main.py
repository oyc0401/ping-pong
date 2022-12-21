from pingpong.pingpong_smooth_board import *


pingPong = PingPong(400, 600, 20)

whiteBall = MyBall(10, 100, 75)
whiteBall.setVelocity(-6 * 1, -4 * 1)

pingPong.setBall(whiteBall)

pingPong.start(300)

print("종료")
pingPong.finish()