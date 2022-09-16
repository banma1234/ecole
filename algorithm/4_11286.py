import sys, heapq
input = sys.stdin.readline

numList = []    # heaqp은 빈 list로부터 시작된다.
case = int(input())

for i in range(case):
    num = int(input())
    if num == 0:    # 입력받은 수가 0일 경우
        if len(numList) == 0:   # heaque이 비어있을 경우
            print(0)
        else:
            # heappop()은 heaqp의 최상단 노드를 pop 하고 그 값을 반환한다.
            # 튜플 형태의 원소가 저장되어 있기 때문에 튜플의 1번 index값(원래 값)을 출력한다.
            print(heapq.heappop(numList)[1])
    else:
        # 튜플 형태로 numList에 원소를 삽입한다.
        # 0번 자리에는 절댓값 비교를 위해 절댓값 num을, 1번 자리에는 본래 값(num)을 입력한다.
        heapq.heappush(numList, (abs(num), num))