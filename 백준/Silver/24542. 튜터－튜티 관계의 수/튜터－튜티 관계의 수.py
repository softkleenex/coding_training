# https://www.acmicpc.net/problem/24542
import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n, m = map(int, (input().split()))
#n > stu, m > friend
fri = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    fri[a].append(b)
    fri[b].append(a)
    
# print(fri)

visited = [0] * n

def dfs(node):
    visited[node] = True
    count = 1
    for friend in fri[node]:
        if visited[friend] != 1:
            count += dfs(friend)
    return count

ans = 1
mod = 1000000007

for i in range(n):
    if visited[i] != 1:
        size = dfs(i)
        ans = (ans * size) % mod
        
print(ans)    