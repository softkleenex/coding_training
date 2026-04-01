# https://www.acmicpc.net/problem/1157
import collections
import itertools
import sys
import math
import heapq

n = input().upper()

#print(n)

target = dict(collections.Counter(n))

maxv = max(target.values())

ans = []

for k, v in target.items():
    if target[k] == maxv:
        ans.append(k)
        
        
if len(ans) >= 2:
    print("?")
else:
    print(ans[0])