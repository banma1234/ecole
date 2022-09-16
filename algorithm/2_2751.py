import sys  # 기존의 input보다 짧은 입력시간을 가진다
input = sys.stdin.readline    # 매번 sys 치기 귀찬아서 넣었다

case = int(input())   # 입력할 수의 개수
numList=[int(input()) for i in range(case)] # case 만큼 사용자 입력을 반복하여 numList 배열에 입력한다.

numList.sort()  # 정렬 내장함수 실행

for i in range(case):
    print(numList[i])   # 출력


# 다른 방법
# import sys

# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))
# for j in sorted(arr):
#     sys.stdout.write(str(j)+'\n')
