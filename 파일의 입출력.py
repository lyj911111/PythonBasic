#파일 불러와서 읽기. 

testFile = open('C:\\abc.txt','r')  # 'r' read의 약자, 'rb' read binary 약자 (그림같은 이미지 파일 읽을때)
readFile = testFile.readline()
print(readFile)

#그림 파일 읽기

testFile = open('C:\\0.gif','rb')
readFile = testFile.readline()
print(readFile)

#파일에 추가하기. (문자열을 추가하는 예제)
testFile = open('C:\\abc.txt','a')  # 'a' 문자열 추가 약자
testFile.write('\n 대한민국.')
testFile.close()

#파일 생성해 쓰기
testFile1 = open('C:\\abc1.txt','w') # w: write 쓴다
testFile1.write('쓰기테스트')
testFile1.close()
