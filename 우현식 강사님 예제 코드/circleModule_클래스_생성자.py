# OOP Understanding, By Kevin Woo (3D Ways), 2018-08-16
# 원의 면적을 계산하는 추상적인(물리적인) Class (붕어빵 틀 개념) Module

import math

class Circle: # 클래스 템플릿 (명사형 의미의 변수와 동사형 의미의 메소드를 가짐)
    color = "black" # 클래스 멤버 변수, 공통으로 사용되어지는 변수

    # 생성자 & 변수 데이터 필드 초기화
    def __init__(self, radius = 5): # self에는 값 대입 안함, 클래스 자신, 생성자, 파이썬 고유 구문
        self.radius = radius

    # 메소드 (함수 기능)
    def circleArea(self):
        return math.pi * self.radius * self.radius 


