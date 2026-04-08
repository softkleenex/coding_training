# https://www.acmicpc.net/problem/2075


import sys
import heapq

n = int(input())

list1 = list()

for i in range(n):
    temp = map(int, input().split())
    for v in temp:
        heapq.heappush(list1, v)
    while len(list1) > n:
        heapq.heappop(list1)
# print(list1)

ans = 0

print(heapq.heappop(list1))
