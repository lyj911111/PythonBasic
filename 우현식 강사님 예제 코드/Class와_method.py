# OOP Understanding, By Kevin Woo (3D Ways), 2018-08-16
# 원의 면적을 계산하는 추상적인 Class (붕어빵 틀)과 반지름에 따른 객체(Object) 생성

import math

class Circle: # 클래스 템플릿 (명사형 의미의 변수와 동사형 의미의 메소드를 가짐)
    color = "black" # 클래스 멤버 변수, 공통으로 사용되어지는 변수

    # 생성자 & 변수 데이터 필드 초기화
    def __init__(self, radius = 5): # self에는 값 대입 안함, 클래스 자신, 생성자, 파이썬 고유 구문
        self.radius = radius

    # 메소드 (함수 기능)
    def circleArea(self):
        return math.pi * self.radius * self.radius 

def main(): # 다른 프로그래밍 언어처럼 중요한 것을 main 함수에 둔다.
    # 반지름 5인 Circle 객체를 생성, 인스턴스화
    myCircle1 = Circle() 
    print(myCircle1.circleArea()) # 객체 메소드 print


    # 반지름 50인 Circle 객체를 생성, 인스턴스화
    myCircle2 = Circle(50)
    print(myCircle2.circleArea())

    # 반지름 100인 Circle 객체를 생성, 인스턴스화
    myCircle3 = Circle(100)
    print(myCircle3.circleArea())

    print(myCircle3.radius) # 객체 멤버 변수 print, 인스턴스 변수

    print(Circle.color) # 클래스 변수
    print(myCircle3.color) # 위의 클래스 변수와 같은 결과
    
    print(math.pi) # '3.141592653589793' print

if __name__ == "__main__": # 같은 모듈내에서만 수행, 다른 모듈에서 import하는 것을 방지, 파이썬 고유 구문
    main() # 마지막으로 여기서 main을 호출하므로 문제가 없다.
