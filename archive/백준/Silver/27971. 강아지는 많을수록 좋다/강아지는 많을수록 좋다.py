# https://www.acmicpc.net/problem/27971

import sys
input = sys.stdin.readline
from collections import deque 


n, m, a, b = map(int, input().split())
#목표 강쥐수, 닫힌구간 개수, a, b개수


dog = 0

blocked = [0] * (n + 1)

for _ in range(m):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        blocked[i] = 1

visited = [-1 for i in range(n+1)]


def bfs():
    q = deque([0])
    visited[0] = 0
    
    while q:
        now = q.popleft()
        if now == n:
            return visited[now]
        
        for way in (now + a, now + b):
            #ㅁㅏ리를 초과하지 않고,  제한 구간에 들어있지 않고, 미방문 구간이라면
            if way <= n and blocked[way] == 0 and visited[way] == -1:
                visited[way] = visited[now] + 1
                q.append(way)   
    return -1
    
    
print(bfs())
