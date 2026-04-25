# https://www.acmicpc.net/problem/1080


n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input())))
    
for i in range(n):
    b.append(list(map(int, input())))
    
    
# print(*a, sep = '\n')
# print()
# print(*b, sep = '\n')

def flip(target, y, x):
    dir = ((-1, -1), (-1, 0), (-1, 1), 
           (0, -1), (0, 0), (0, 1),
           (1, -1), (1, 0), (1, 1))
    
    for ny, nx in dir:
        n = target[y + ny][x + nx]
        target[y + ny][x + nx] = 1 if n == 0 else 0


ans = 0

for y in range(1, n-1):
    for x in range(1, m-1):
        if a[y - 1][x - 1] != b[y - 1][x - 1]:
            flip(a, y, x)
            # print(y, x)
            ans += 1
            
            
if a == b:
    print(ans)
else:
    print(-1)
    
    # print(*a, sep = '\n')
    # print()
    # print(*b, sep = '\n')