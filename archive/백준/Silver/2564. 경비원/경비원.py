# https://www.acmicpc.net/problem/2564

bx, by = list(map(int, input().split()))

n = int(input())

stores = []

for _ in range(n + 1):
    ny, nx = list(map(int, input().split()))
    if ny == 1:
        stores.append(nx)
    elif ny == 2:
        stores.append(bx + by + (bx - nx))
    elif ny == 3:
        stores.append(bx + by + bx + by - nx)
    elif ny == 4:
        stores.append(bx + nx)
        
        
stores, d = stores[0 : -1], stores[-1]

# print(stores, d)

ans = 0

for v in stores:
    ans += min(
        abs(v - d), 
    abs((by + bx + by + bx) - abs(v - d))
    )    
print(ans)