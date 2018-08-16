''' 리스트 자료형 '''

#숫자형 리스트
number = [1,2,3,4,5,6,7,8,9,10]
print(number[0])
print(number[8])

#문자형(character) 리스트
char = ['a','b','c','d','e']
print(char[0])
print(char[3])
char.extend(['f','g','h']) #문자열 추가 함수 뒤에 덧붙임.
print(char[6])              #추가된 g가 출력됨.
print(char)                 #전체 출력 확인

#문자열(string) 리스트
string = ["one","two","three","four","five"]
print(string[4])
string.extend(["six","seven"])  #string도 뒤에 덧붙일 수 있음.
print(string)

print('\n')         #개행 하기.

#혼합형 리스트
mix = ["one","two","three",1,2,3,4]
print(len(mix))                     #길이를 출력
print(mix[2:5])                     #섞어서 중간부분 출력

#리스트(list)형 리스트
listmix = ["one","two","three",[1,2,3,4,5,6]]  # 리스트 내부에 리스트가 있음
print(listmix)
print(listmix[2:3])                         #문자열과 리스트가 같이 출력
print(listmix[3][4])                    #리스트 내부로 접근해서 값을 출력
