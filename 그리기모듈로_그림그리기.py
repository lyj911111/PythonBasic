'''

그리기 모듈을 이용해 아름다운 그림 그리기

1000
7
255
10
예시그림 입력.

'''


import turtle
t = turtle.Pen()
turtle.bgcolor("yellow")

rainbowColor = ["red","orange","yellow","green","blue","indigo","violet"]

ranges = int(input("1 ~ 1000 정수 반복 횟수 입력하시오:"))
colors = int(input("1 ~ 7 정수 컬러 색 입력하시오:"))
angles = int(input("1 ~ 360 정수 각도를 입력하시오:"))
widths = int(input("1 ~ 10 정수 펜의 폭을 입력하시오:"))

for i in range (ranges):
    t.pencolor(rainbowColor[i%colors])
    t.forward(i)
    t.left(angles)
    t.width(widths)

