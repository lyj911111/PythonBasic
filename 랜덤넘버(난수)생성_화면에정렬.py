# 랜덤넘버(난수) , 화면에 임의 개수로 정렬하기.

import random # 난수 불러오기

for i in range(0, 50, 1):
    randomNumber = random.randint(1,6)

    if(( i % 10 )== 0):
        print("\n")

    print(randomNumber, end="   ")    
