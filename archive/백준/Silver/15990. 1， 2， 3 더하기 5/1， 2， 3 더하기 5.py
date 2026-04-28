# https://www.acmicpc.net/problem/15990

t = int(input())

ans = [
        [0, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [1, 1, 1],
       [2, 0, 1]
       ]
#        ]#ans[a][b] = 숫자 a에 대해서 마지막에 b + 1숫자가 오는 경우의 수
#ans[a][0] = a[a - 1][1] + a[a - 1][2]
# ans[a][1] = a[a - 2][0] + a[a-2][2]
# a[a][2] = a[a - 3][0] + a[a - 3][1]
 

for _ in range(t):
    n = int(input())
    while len(ans) - 1 <= n:
        ei = len(ans) - 1
        ans.append([0, 0, 0])
        ans[ei][0] = (ans[ei - 1][1] + ans[ei - 1][2]) % 1000000009
        ans[ei][1] = (ans[ei - 2][0] + ans[ei-2][2]) % 1000000009
        ans[ei][2] = (ans[ei - 3][0] + ans[ei - 3][1] )% 1000000009
    
    print(sum(ans[n]) % 1000000009)
    
