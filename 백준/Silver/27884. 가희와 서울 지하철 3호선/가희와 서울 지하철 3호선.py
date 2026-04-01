# https://www.acmicpc.net/problem/27884

import sys
import collections
import itertools

def check_m(now):
    maxans = 1
    ans = 1
    for i in range(0, len(now) - 1):
        if now[i] != now[i + 1]:
            ans += 1
            maxans = ans if ans >= maxans else maxans
        else:
            ans = 1
    
    return maxans
            
n, m = map(int, input().split())
MOD = 10**9 + 7
ans = 0


for p in itertools.product([0, 1], repeat = n):
    if check_m(p) == m:       
        nowans = 1
        for v2 in p:
            if v2 == 0:
                nowans = (nowans * 5) % MOD
            else:
                nowans = (nowans * 11) % MOD
        ans = (ans+ nowans) % MOD
        nowans = 1
        

print(ans)