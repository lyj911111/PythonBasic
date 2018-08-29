#무한루프 상태 방지 (메모리 영역을 잠식하여 시스템 한계 봉착 예방)

EventExt = 0

while True:             #C언어 While(1) 이랑 같음. 무한루프

    print("항상 상태를 감시하는 무한 루프")
    EventExt = int(input("이벤트용 정수를 넣어라"))

    if (EventExt):
        print("무한루프 탈출")
        break
    

