# Test Program for Python PC GUI(popUp & Dialog Box), By Kevin Woo (3D Ways), 2018-08-28
# 시험용 프로그램이므로 참조하시어 PC GUI Project를 완성하시면 됩니다.

# GUI그래픽을 불러올때 ...

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
# from tkinter import colorchooser
from tkinter.colorchooser import *



# 실습 1

# popUp버튼을 눌렀을때 다음과 같은 팝업창이 띄어짐. (클릭할 버튼이름, 클릭했을때 나오는 팝업)

def popUp():
    messagebox.showinfo("popUp", "hello showinfo")          # 도움창
    messagebox.showwarning("popUp", "hello showwarning")    # 경고창 !
    messagebox.showerror("popUp", "hello showerror")        # 에러창 X
    messagebox.askquestion("popUp", "hello askquestion")    # 도움창
    messagebox.askokcancel("popUp", "hello askokcancel")    
    messagebox.askyesno("popUp", "hello askyesno")
    messagebox.askretrycancel("popUp", "hello askretrycancel")

    messagebox.askyesnocancel("askyesnocancel", "예, 아니오, 취소")



# 실습 2

#잘못된 번호를 입력했을 때, (ex 1이 아닌 번호를 입력했을때)

def popUpWrongNumber():
    messagebox.showwarning("popUp", "Please enter number 1")

def entryVal1():
    intValue1 = int(entry1.get()) # int 빼고 entry1.get()만 알파벳 입력 후 시험

    if(intValue1 != 1):
        popUpWrongNumber()

  
window = Tk()
# master = Tk(), root = Tk()

window.geometry("640x480") # LCD VGA Size

Label(window, text = "Input Value1").grid(row = 0)

entry1 = Entry(window)

entry1.grid(row = 0, column = 1)

Button(window, text = 'clickValue1', command = entryVal1).grid(row = 0, column = 2)

popUpButton = Button(window, text ="popUp", command = popUp)
popUpButton.place(x = 320,y = 240)

# popUpButton.pack()



# 실습 3

def getColor():
    color = askcolor() 
    print(color)
    
colorButton = Button(text='색을 선택하세요', command=getColor) # 색상을 선택하면 창에 값이 나옴.
colorButton.place(x = 100,y = 100)  # 창내 버튼의 좌표



# 실습 4

info = messagebox.askyesnocancel("askyesnocancel", "예, 아니오, 취소")
print(info) # 예 True, 아니오 False, 취소 None, 라고 누르면 값이 반환됨.



# 실습 5

charcter = simpledialog.askstring("askstring", "Please enter charcter")
print(charcter)

intNumber = simpledialog.askinteger("askinteger", "Please enter integer number")
print(intNumber)

floatNumber = simpledialog.askfloat("askfloat", "Please enter float number")
print(floatNumber)

window.mainloop()
master.mainloop(), root.mainloop()

# QR 코드 패키지

#패키지설치 : $pip install 패키지 이름-> $ pip install pillow qrcode


import qrcode
image = qrcode.make("http://3dways.co.kr/xe/")
image.save("3dways_qrcode.png")

