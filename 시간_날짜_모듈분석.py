'''
    �ð�, ��¥ ��� �м�

'''

from datetime import date    #datetime���� date(��¥) �ҷ�����
print(date.today())          #���� ��¥ ���

import time
print(time.time())           #1970�� 1��1�� ���ķ� ���� '��'�� ����.

import time
print(time.asctime())        # ����,��,����,�ð�,�⵵�� �ѹ��� ����

import time
print(time.localtime())      # ���� ���ϰ� �˷���.

#���ó�¥�� 3�� ���� �� ��¥ǥ���ϱ�

from datetime import date, timedelta
date.today()

day = timedelta(days = 3)
today = date.today()
print(today + day)


