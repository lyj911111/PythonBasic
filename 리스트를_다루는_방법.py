''' 리스트 다루기 '''

# 리스트는 왼쪽에서는 0부터 세고, 오른쪽부터는 -1으로 센다.

char = ['a','b','c','d']
string = ["one","two","three"]
ch_st = char + string

print(ch_st)        # character와 string을 합칠 수 있다. 한배열로.
print(char * 3)     # a,b,c,d 와 같은 character를 뒤에 3배로 배열함.

ch_st[0:3] = [0,1,2,3]  # 배열의 0~3자리에 숫자를 넣어
print(ch_st)

ch_st.append(30)    # 배열의 끝에 ()의 값을 넣어준다.
print(ch_st)

del ch_st[7]         # 7번째 배열의 값을 지운다.
print(ch_st)        # 값을 지우면 맨 뒤에 있는 값을 앞으로 땡겨온다.

ch_st.reverse()      # 역순배치
print(ch_st)

print('\n') #개행

# 인덱스 값 추가하기.  insert(인덱싱,값) 함수.
test_list = [0,1,2,3,4]
test_list.insert(1,'damn')  # 인덱스값 1앞에 'damn'을 삽입하라.
print(test_list)

# 인덱스 값 순서대로 정렬하기.  sort() 함수.
test = [5,1,2,3,9,8]
test.sort()
print(test)


