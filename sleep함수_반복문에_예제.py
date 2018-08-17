'''
    sleep() 함수,

    초단위로 시간 지연시킬때, 반복문에 도움
    1초마다 생성
'''

import time

loopCount = 0
while(loopCount < 5):
    print("반복문을 처리하는 while 예약어가 필요하다.")
    time.sleep(1)
    loopCount = loopCount + 1


for loopCount1 in range(0, 10, 2):
    print(time.time())
    time.sleep(1)

# 파이썬 언어로 작성한 알고리즘의 성능분석을 위해
# 실행시간을 측정 예제.

loopCount = 0
startPoint = time.time()

while (loopCount < 15 ):
    print("반복문 처리하는 while 예약어 필요")
    loopCount = loopCount + 1

finishPoint = time.time()

print('\n',"처리시간은: ",finishPoint - startPoint, "초 입니다.")
