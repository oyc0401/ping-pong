from pingpong.pingpong_smooth_board import *

pingPong = PingPong(800, 600, 20)  # 보드의 사이즈

whiteBall = Ball(30, 100, 75)  # 반지름, x좌표, y좌표
whiteBall.setSpeed(-6, -4)  # 공의 속도 정하기

pingPong.setBall(whiteBall)
pingPong.setDelay(0.05)  # 딜레이 설정 (0.05 = 초당 20회)
pingPong.start(300)  # 300틱 실행

print("종료")
pingPong.finish()
