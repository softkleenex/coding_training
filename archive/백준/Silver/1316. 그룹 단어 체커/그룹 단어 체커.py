import sys
import collections
import itertools

n = int(input())

ans = 0

for i in range(n):
    temp = input()
    pre = None
    
    visited = set()
    ans += 1
    
    for now in temp:
        if pre == None:
            pre = now
            visited.add(now)
                
        if now in visited:
            if pre != now:
                #print("실패" + temp)
                ans -= 1
                break
            else:
                pre = now
        else:
            visited.add(now)
            pre = now
    
   # print("성공" + temp)
   
    
    
print(ans)