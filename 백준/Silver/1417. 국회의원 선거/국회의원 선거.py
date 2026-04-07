# https://www.acmicpc.net/problem/1417

import sys
import heapq

n = int(input())

dasom = int(input())
others = []
for i in range(n -1):
    vote = int(input())
    heapq.heappush(others, -vote)


# print(others)

ans = 0


while others:
    max_others = -heapq.heappop(others)
    if dasom > max_others:
        break
    max_others -= 1
    dasom += 1
    ans += 1

    heapq.heappush(others, -max_others)

print(ans)
