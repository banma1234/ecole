import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x : (x[1], x[0]))
tail = 0
count = 0
for i in arr:
    if i[0] >= tail:
        count += 1
        tail = i[1]
print(count)