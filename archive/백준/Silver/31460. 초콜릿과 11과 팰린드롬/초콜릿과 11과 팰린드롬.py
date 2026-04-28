# https://www.acmicpc.net/problem/31460

import sys
import collections


t = int(input())

12221

11
121

1221


for i in range(t):
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(11)
    else:
        print("1", '2' * (n - 2), "1", sep = '')
        
    