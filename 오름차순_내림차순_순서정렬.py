#오름차순, 내림차순 순서정렬



sortList = [1,10,8,5,4,3,6,9,2,7]
print(" 순서 오름차순 정렬전",sortList,"입니다")

for i in range (0, (len(sortList)-1)):  # 0부터 시작하므로, 리스트수 - 1
    t = i

    for j in range (i+1, len(sortList)):    #다음 부터 시작하므로 리스트 개수
        if(sortList[t] > sortList[j]):      #sortList[0] > sortList[1] 인지 판단
            t = j

    temp = sortList[i]
    sortList[i] = sortList[t]
    sortList[t] = temp

print( "순서 오름차순 후",sortList,"입니다")

###########################################################

sortList = [1,10,8,5,4,3,6,9,2,7]
print(" 순서 내림차순 정렬전",sortList,"입니다")

for i in range (0, (len(sortList)-1)):  # 0부터 시작하므로, 리스트수 - 1
    t = i

    for j in range (i+1, len(sortList)):    #다음 부터 시작하므로 리스트 개수
        if(sortList[t] < sortList[j]):      #sortList[0] > sortList[1] 인지 판단
            t = j

    temp = sortList[i]
    sortList[i] = sortList[t]
    sortList[t] = temp

print( "순서 오름차순 후",sortList,"입니다")
