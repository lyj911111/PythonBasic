'''
터틀(turtle) 모듈을 이용하여 그림 그리기
1. for루프 이용


'''

import turtle
t = turtle.Pen()

'''
#8각형 그리기. 왼쪽, 오른쪽 

for loopname in range(0, 8, 1):       # 0부터 8까지 1씩 증가하는거임
    t.forward(30)
    t.left(45)

for loopnam in range(0, 8, 1):
    t.forward(30)
    t.right(45)
'''

'''
#원그리기 t.circle(픽셀 반경, extent = 각도)

for i in range(1, 50, 3):           # 1~50 까지 3씩 증가
    t.circle(i, extent = 360)

for i in range(1, 50, 3):           # 1~50 까지 3씩 증가
    t.circle(-i, -360)
'''



'''
# 그림 색상 입히기

색상 종류: red, orange, yellow, green, blue, violet, purple, black, white

#t.pencolor("black")         # 펜의 색상
#turtle.bgcolor("yellow")    # (bg=background)배경색 입히기


import turtle
t = turtle.Pen()
turtle.bgcolor("yellow")

for i in range(150):
    t.pencolor("black")
    t.forward(i)
    t.left(135)
'''


# 그림 색상 채우기

import turtle
t = turtle.Pen()

turtle.bgcolor("magenta")

t.pencolor("black")
t.fillcolor("black")
t.begin_fill()

t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)
t.forward(30)
t.left(45)

t.end_fill()


turtle.bgcolor("yellow")
turtle.bgcolor("red")
