import itertools
import collections
from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())

under = [0] * (n + 1)#i번 카드 아래에있는 카드 start 1
over = [0] * (n + 1)#i번 카드 위에있는 카드 번호, start 1
bottom_of_pile = list(range(0, n + 1))#i번 더미의 바닥에있는 카드 번호

for _ in range(q):
    c, p = map(int, input().split())
    if under[c] == 0:#만약 c가 최하단의카드였다면
        over[p] = c#p위는 c가 된거
        under[c] = p#c아래는 p가 된다
        #bottom_of_pile[bottom_of_pile.index(c)] = 0#c의 원래 카드더미의 아래는 0이되는데,,,
        bottom_of_pile[c] = 0#c의 원래 카드더미의 아래는 0이되는데,,,
    else:#c가 최하단이 아니었다면
        over[under[c]] = 0#c의 아래에있던 카드의 over을 갱신켜준다.
        under[c] = p
        over[p] = c

ans = []
for i in range(1, n + 1):
    curr = bottom_of_pile[i]
    count = 0
    while curr != 0:
        count +=1
        curr = over[curr]
    ans.append(count)

print(*(ans))
