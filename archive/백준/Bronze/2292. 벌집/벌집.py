#https://www.acmicpc.net/problem/2292

import sys
import collections 
import heapq
import itertools 
input = sys.stdin.readline
# sys.setrecursionlimit(10**6) 

#1 > (1)은 0 번
#1 + 1 ~ 1 + 6 까지는 1번
#7 + 1 ~ 7 + 12 까지는 2번
#19 + 1 ~ 19 + 18까지는 3번


n = int(input())

ans = 0
a = 0
b = 1

if n == 1:
    print(1)
    quit()

while not(b >= n and n >= a):
    a = b + 1
    b = b + 6 * ans
    #print(a, b)#(1, 1) #(2, 7)#(8, 19)
    ans += 1
    
print (ans)