'''
    GUI  (Graphic User Interface)
    텍스트 명령이 아닌, 마우스 클릭만으로 프로그램을 구동한다.

    Tkinter 의 라이브러리를 제공함.
    
# 1. Button()    마우스로 클릭하여 프로그램 실행
# 2. Label()     컴퓨터 화면에 글자나 이미지 표시
# 3. Canvas()    캔버스위 그림그리기 처럼, 도형,색칠 등 그래픽에 관한것
# 4. Entry()     글자를 입력하기 위해 비어있는 사각박스
# 5. Checkbutton()  여러버튼중 하나 선택하여 수행.
# 6. Radiobutton()  Checkbutton()과 비슷, 하나의 그룹에서 하나만 마우스로 선택가능.
# 7. Mesage()    Label()과 비슷, 출력시 자동으로 폭,줄 맞춤기능 내장
# 8. Text()      사용자가 글자 스타일, 속성을 자유롭게 조정 가능
# 9. Menubutton()   인터넷에서 뜨는 팝업창처럼, 팝업 처리와 메뉴바를 누를때, 아래로 메뉴바가 나오게 하는 풀다운 메뉴를 관리
#10. Menu()      메뉴버튼 관리하는 작은 기능
#11. Frame()     다른 위젯을 받아들이는 기능

'''

'''
#   1. 클릭창 뛰어서 실행하기

from tkinter import *

def AreaOfCircle():
    Pi = 3.1415
    Radius = 5
    circleArea = Pi * Radius * Radius
    print("GUI 프로그램으로 계산한 원의 넓이가", circleArea ,"입니다.")

window = Tk()

label = Label(window,text = "원 넓이 계산")
button = Button(window,text = "클릭하세요", command = AreaOfCircle)
label.pack()    # pack의 의미, label을 창에 배치하라.
button.pack()

#버튼 색상 입히기
button["fg"] = "green" #글자 색
button["bg"] = "red"   #버튼배경색


window.mainloop()       #사용자가 닫을때까지 이벤트 지속
'''


'''
#   2. Canvas에 그림 그리기.

from tkinter import *

window = Tk()
canvas = Canvas(window, width = 500, height = 500)  #창의 크기를 결정.
canvas.pack()

canvas.create_line(10,10,50,50,fill = "green")                  # 숫자의미:  좌표. p112
canvas.create_rectangle(70,70,100,100,fill = "orange")
canvas.create_oval(150, 150, 200, 200, outline = "black", fill="blue")
canvas.create_arc(300, 300, 350, 350, extent = 180, outline = "gray", fill = "purple")

points = [400, 400, 430, 460, 460, 470]
canvas.create_polygon(points, outline = "red", fill = "orange", width = 5)

window.mainloop()
'''


'''
#   3. 움직이는 에니메이션

from tkinter import *
import time

window = Tk()
canvas = Canvas(window, width = 500, height = 100)      # window 크기 설정.
canvas.pack()

carBody = canvas.create_arc(0,30,50,80, extent = 180, outline = "gray", fill="purple")      # 좌표 [0,30]에서 [50,80]까지 그리는데, 180도 각도까지만 그려라,
wheel1 = canvas.create_oval(10, 55, 20, 65, fill = "black")                                 # [10,55]와 [20,65] 사각형 내에 Oval(계란형)을 그려라.
wheel2 = canvas.create_oval(30, 55, 40, 65, fill = "black")

for i in range (220):                                   # 0.035초씩 i가 증가해 220될때까지, 
    canvas.move(carBody, 2, 0)                          # Body가 x좌표로 2씩 이동, y좌표로 0이동.
    canvas.move(wheel1, 2, 0)                           # wheel1 x좌표로 2씩 이동, y좌표로 0이동.
    canvas.move(wheel2, 2, 0)
    window.update()                                     # 화면을 업데이트 해주면서 이동을 표시.
    time.sleep(0.035)                                   # delay같은 역할, 0.035초씩 잘라서 표시.(움직임이 사람눈에 보이도록)

window.mainloop()

# 16진수 RGB색상 소개 0~255 범위로 모든색을 표현

#   #FF0000(255,0,0)  : 빨강색
#   #00FF00(0,255,0)  : 녹색
#   #0000FF(0,0,255)  : 파랑색
#   #000000(0,0,0)    : 검정색
#   #FFFFFF(255,255,255): 흰색
'''


'''
#   4. 캔버스를 이용해 글자 그리기

from tkinter import *

window = Tk()
canvas = Canvas(window, width = 500, height = 100)
canvas.pack()

canvas.create_text(230, 40, text = "이원재", font = ("Rockwell extra bold",30), fill = "blue")

window.mainloop()
'''


'''
#   5. Entry 위젯으로 텍스트 입력하기 (우리가 사용하는 ID입력과 Password입력등을 이것으로 제작.)




from tkinter import *

def AreaOfCircle():
    CircleArea = float(entry1.get()) * float(entry2.get()) * float(entry2.get())
    print("GUI Entry프로그램으로 계산한 원의 넓이: ",CircleArea,  "입니다.")

window = Tk()

Label(window,text = "원주율").grid(row = 0)            # Label을 0번째 행에 배치
Label(window,text = "반지름").grid(row = 1)            # Label을 1번째 행에 배치

entry1 = Entry(window)                                 # 입력창 생성.
entry2 = Entry(window)

entry1.grid(row = 0, column = 1)                       # 입력창(박스)의 설정 위치 설정, 0번째 행, 1번째 열에 
entry2.grid(row = 1, column = 1)

Button(window, text = "클릭하세요", command = AreaOfCircle).grid(row = 2, column = 1)        # 2번째 행과 1번째 열에 클릭박스 배치.

window.mainloop()
'''





'''
#   6. Radio Button (라디오버튼) 선택하기

#   파이썬의 int, string, boolean, double 타입은 변하지 않는 타입, 그래서 Tkinter에서는 값이 변하고 업데이트 되는 타입인 'intVar', 'StringVar', 'BooleanVar', 'DoubleVar'을 사용함.

from tkinter import *

window = Tk()
var = IntVar()

Label(window, text = "우리나라에서 가장 높은 산은?").pack()

Radiobutton(window, text = "북한산", variable = var, value = 1).pack(anchor = W)       #   value를 안바꾸면, 한번에 다 선택이됨.
Radiobutton(window, text = "설악산", variable = var, value = 2).pack(anchor = W)       #   anchor = W 의미, West, 서쪽에다 박아 놓는다. 서쪽으로 고정한다. (E: East, W: West, N: North, S:South)
Radiobutton(window, text = "지리산", variable = var, value = 3).pack(anchor = E)       #   variable = var, 정수면, IntVar() , 문자열이면 StringVar() 쓰면 된다.
Radiobutton(window, text = "한라산", variable = var, value = 4).pack(anchor = S)

window.mainloop()
'''





'''
#   7. Scroll Bar (스크롤 바) 만들기

from tkinter import *
window = Tk()

yscrollbar = Scrollbar(window)                          # 윈도우에 스크롤바 생성
yscrollbar.pack(side = RIGHT, fill = Y)                 # 오른쪽 배치, y축을 모두 채움.

Label(window, text = "스크롤바를 움직이세요").pack()
text = Text(window, yscrollcommand = yscrollbar.set)
text.pack()

text.insert(END, "ABCD"*1000)
yscrollbar.config(command = text.yview)

window.mainloop()
'''





'''
#   8. 메뉴 다루기

from tkinter import *

def toDoFile():                             # 콜백함수(Call Back function)
    print("파일 작업을 수행했습니다!")

def toDoEdit():                             # 콜백함수(Call Back function)
    print("편집 작업을 수행했습니다!")

window = Tk()
menu = Menu(window)                         # 메뉴창 생성.
window.config(menu = menu)

filemenu = Menu(menu)                                                   # 위 메뉴바에 생성 
menu.add_cascade(label = "파일", menu = filemenu)

filemenu.add_command(label = "새문서", command = toDoFile)              # 하위 목록 생성
filemenu.add_command(label = "열기", command = toDoFile)
filemenu.add_command(label = "저장", command = toDoFile)
filemenu.add_command(label = "다른 이름으로 저장", command = toDoFile)
filemenu.add_command(label = "인쇄", command = toDoFile)
filemenu.add_separator()        #   인쇄와 나가기 사이 줄 그어 분리
filemenu.add_command(label = "나가기", command = toDoFile)

editmenu = Menu(menu)                                                   # 위 메뉴바에 생성
menu.add_cascade(label = "편집", menu = editmenu)

editmenu.add_command(label = "붙이기", command = toDoEdit)
editmenu.add_command(label = "바꾸기", command = toDoEdit)
editmenu.add_command(label = "복사", command = toDoEdit)
editmenu.add_command(label = "찾기", command = toDoEdit)

window.mainloop()
'''




'''
# 9. 마우스와 키보드로 이벤트 관리하기         ( 더블클릭할때 작동 예제 )

from tkinter import *

def click(event):
    print("나가시려면 더블 클릭하세요")

def quit(event):
    print("종료합니다")
    import sys;sys.exit()                               # 여러 개의 구문을 한줄에 쓸때 ;을 사용해야 함.

window = Tk()
widget = Button(window, text = "더블 클릭하시오!!")
widget.pack()
widget.bind("<Button-1>", click)                        # <Botton-1> : 마우스 왼쪽 버튼을 눌리면 실행 되는 버튼
widget.bind("<Double-Button-1>", quit)                  # <Botton-2> : 마우스 중간 휠
                                                        # <Bottom-3> : 마우스 오른쪽 버튼 누르면 실행
window.mainloop()                                       #  click     : 이벤트가 발생하면 call back하는 함수.
                                                        #  quit      : event가 발생하면 동작하는 call back함수
# 마우스 이벤트 그외 것들.
#   B1-Motion           : 마우스의 Button-1/2/3  눌린 채로 움직일 때 사용.
#   ButtonRelease-1     : 버튼을 손에서 땔때 발생
#   Enter               : 마우스 포인터가 위젯으로 진입할 때 적용
#   Leave               : 마우스 포인터가 위젯으로 떠나면 적용

# 키보드 이벤트
#   FocusIn             : 키보드의 포커스가 위젯으로 이동할 때
#   FocusOut            : 키보드의 포커스가 다른 위젯으로 이동할 때
#   Return              : 엔터키를 치면
#   Key                 : 아무키나 누를때 발생
#   Shift-Up            : 쉬프트키와 윗쪽 키를 동시에 누를때
#   Configure           : 위젯의 크기나 위치가 변경될 때
'''






# 10. 위젯 배치하기 (계산기 예제)
from tkinter import *

window = Tk()

Button(window, font = ('Rockwell',10),text = '←', width = 4, height = 2).grid(row = 0, column = 1)
Button(window, font = ('Rockwell',10),text = 'CE', width = 4, height = 2).grid(row = 0, column = 2)
Button(window, font = ('Rockwell',10),text = 'C', width = 4, height = 2).grid(row = 0, column = 3)
Button(window, font = ('Rockwell',10),text = '+/-', width = 4, height = 2).grid(row = 0, column = 4)
Button(window, font = ('Rockwell',10),text = '√', width = 4, height = 2).grid(row = 0, column = 5)

Button(window, font = ('Rockwell',10),text = '7', width = 4, height = 2).grid(row = 1, column = 1)
Button(window, font = ('Rockwell',10),text = '8', width = 4, height = 2).grid(row = 1, column = 2)
Button(window, font = ('Rockwell',10),text = '9', width = 4, height = 2).grid(row = 1, column = 3)
Button(window, font = ('Rockwell',10),text = '*', width = 4, height = 2).grid(row = 1, column = 4)
Button(window, font = ('Rockwell',10),text = '%', width = 4, height = 2).grid(row = 1, column = 5)

Button(window, font = ('Rockwell',10),text = '4', width = 4, height = 2).grid(row = 2, column = 1)
Button(window, font = ('Rockwell',10),text = '5', width = 4, height = 2).grid(row = 2, column = 2)
Button(window, font = ('Rockwell',10),text = '6', width = 4, height = 2).grid(row = 2, column = 3)
Button(window, font = ('Rockwell',10),text = '/', width = 4, height = 2).grid(row = 2, column = 4)
Button(window, font = ('Rockwell',10),text = '', width = 4, height = 2).grid(row = 2, column = 5)

Button(window, font = ('Rockwell',10),text = '1', width = 4, height = 2).grid(row = 3, column = 1)
Button(window, font = ('Rockwell',10),text = '2', width = 4, height = 2).grid(row = 3, column = 2)
Button(window, font = ('Rockwell',10),text = '3', width = 4, height = 2).grid(row = 3, column = 3)
Button(window, font = ('Rockwell',10),text = '-', width = 4, height = 2).grid(row = 3, column = 4)
Button(window, font = ('Rockwell',10),text = '', width = 4, height = 2).grid(row = 3, column = 5)

Button(window, font = ('Rockwell',10),text = '0', width = 4, height = 2).grid(row = 4, column = 1)
Button(window, font = ('Rockwell',10),text = '.', width = 4, height = 2).grid(row = 4, column = 2)
Button(window, font = ('Rockwell',10),text = '1/x', width = 4, height = 2).grid(row = 4, column = 3)
Button(window, font = ('Rockwell',10),text = '+', width = 4, height = 2).grid(row = 4, column = 4)
Button(window, font = ('Rockwell',10),text = '=', width = 4, height = 2).grid(row = 4, column = 5)

window.mainloop()

#   좌표
#   0,0  0,1  0,2  0,3  0,4
#   1,0  1,1  1,2  1,3  1,4
#   2,0  2,1  2,2  2,3  2,4
#   3,0  3,1  3,2  3,3  3,4
#   4,0  4,1  4,2  4,3  4,4





