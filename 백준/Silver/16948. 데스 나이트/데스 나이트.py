# https://www.acmicpc.net/problem/16948

import sys
import collections

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

dir = ((-2, -1), (-2, +1), (+2, -1), (+2, + 1), (0, -2), (0, + 2))


# print(r1, c1, r2, c2)
# print(dir)


#case1. r1과 r2의 차이가 홀수라면 절대로 도달 불가능

ans = 0




def bfs(start):
    used = [[-1] * n for _ in range(n)] 
    used[start[0]] [start[1]] = 0
    q = [start]
    for r, c in q:
        if r == r2 and c == c2:
            return used[r][c]
        
        
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n:
                if used[nr][nc] == -1:
                    used[nr][nc] = used[r][c] + 1
                    q.append([nr, nc])
                    
    return -1


print(bfs([r1, c1]))
                    
                    

            



