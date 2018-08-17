'''
고급수학 숫자 형식처럼 출력하기.

[10.1f]  에서 10은 숫자표시, 1은 소숫점 이하 자리 정밀도 표시
[10.2e]  에서 10은 숫자표시, e는 10의 몇 승으로 표시.

'''

pi = 3.14159

print(format(pi,"10.1f"))   # 소숫점 자릿수 표현.
print(format(pi,"10.3f"))
print(format(pi,"10.5f"))
print("\n")
print(format(pi,"10.1e"))   # 10의 몇승으로 표현.
print(format(pi,"10.3e"))
print(format(pi,"10.5e"))
print("\n")
print(format(300,"10d"))    # 앞에 공백을 10자리 포함.
print(format(300,"5d"))
