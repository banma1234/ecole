import sys
from collections import deque   # deque 라이브러리 사용
input = sys.stdin.readline

num = int(input())
# 1부터 num까지의 숫자로 이루어진 deque 생성
card = deque([i for i in range(1, num + 1)])

while(len(card) > 1):   # card의 원소 개수가 1개가 될때 까지 반복
    card.popleft()  # 가장 왼쪽의 원소 제거
    card.rotate(-1) # 역방향으로 deque 1회 순환

print(card[0])

# 시간초과
# while(len(card) > 1):
#     card.append(card[1])
#     del card[0:2]

# print(card[0])

