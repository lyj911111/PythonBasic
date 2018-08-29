# 예외처리

try:
    number1 = eval(input("분자입력: "))
    number2 = eval(input("분모입력: "))
    division = number1 / number2
    print("계산된 값은: %.2f 입니다." %division)

except ZeroDivisionError:
    print("0으로 나누면 안됨")

else:
    print("정상 출력")

finally:
    print("마지막을 출력")
