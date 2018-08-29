# self는 인자로써 생각하지 않으면 된다.
# 객체명 = 클래스명()     <- 이런식으로 쓴다.

class Super:
    def __init__(self, pi, radius):     # 인자는 self를 제외하고, pi, radius 즉 2개를 넣음.
        self.__pi = pi                  # __의 계념은 함수를 숨겨둔다(private)계념. 외부에서 참조 불가
        self.__radius = radius

    def show(self):
        print(self.__pi, self.__radius)

    def getArea(self):
        return(self.__pi * self.__radius * self.__radius)

# 부모Super의 성질을 자식 Sub이 상속 받는다.

class Sub(Super):
    def __init__(self, pi, radius, height):
        Super.__init__ (self, pi, radius)
        self.__height = height

    def show(self):
        Super.show(self)
        volume = Super.getArea(self) * self.__height
        print(self.__height, volume)


# SubObject는 객체 인스턴스, (객체가 생성되서 나온 인자들) = self
SubObject = Sub(3.14 , 5 , 10)
SubObject.show()
