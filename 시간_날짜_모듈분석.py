'''
    시간, 날짜 모듈 분석

'''

from datetime import date    #datetime에서 date(날짜) 불러오기
print(date.today())          #오늘 날짜 출력

import time
print(time.time())           #1970년 1월1일 이후로 계산된 '초'가 나옴.

import time
print(time.asctime())        # 요일,월,일자,시간,년도를 한번에 보기

import time
print(time.localtime())      # 좀더 상세하게 알려줌.

#오늘날짜에 3일 더한 후 날짜표시하기

from datetime import date, timedelta
date.today()

day = timedelta(days = 3)
today = date.today()
print(today + day)


