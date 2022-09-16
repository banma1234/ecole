import sys, math
input = sys.stdin.readline

m, n = map(int, sys.stdin.readline().split())

primeList = [True] * (int(n ** 0.5) + 1)
primeList[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if primeList[i]:
        if i * i > int(n ** 0.5):
            break
        for j in range(i**2, int(n ** 0.5) + 1, i):
            primeList[j] = False

count = 0
for i in range(1, len(primeList)):
    if primeList[i]:
        res = i * i
        while True:
            if res < m:
                res *= i
                continue
            if res > n:
                break
            res *= i
            count += 1

print(count)

# 메모리 초과
# arr = [i for i in range(2, n + 1) if primeList[i] == True]

# count = 0
# for i in arr:
#     for j in range(2, len(arr)):
#         if i ** j > n:
#             break
#         else:
#             count += 1

# print(count)