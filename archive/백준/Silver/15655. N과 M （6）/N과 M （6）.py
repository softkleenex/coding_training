# https://www.acmicpc.net/problem/15655

n, m = map(int, input().split())
l = sorted(list(map (int, input().split())))

ans = []

def back(now, buck):
    if len(buck) == m:
        print(*buck)
        return
    
    if now == n:
        return
    
    back(now + 1, buck + [l[now]])
    
    back(now + 1, buck)
    
    
back(0, [])

# ans = sorted(ans)

# for v in ans:
#     print(*v)