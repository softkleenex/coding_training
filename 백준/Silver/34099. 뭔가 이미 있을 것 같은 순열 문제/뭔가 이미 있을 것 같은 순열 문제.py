# 만약 조건을 만족하는 수열이 있다면 수열 $A_1$, $A_2$, $\cdots$, $A_N$을 공백으로 구분하여 출력한다. 가능한 답이 여러 개라면 그중 아무 것이나 출력한다.
# 만약 조건을 만족하는 수열이 없다면 -1을 출력한다.

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    canuse = list(range(1, n + 1))
    if k != 1:
        print(*canuse, sep = ' ')
    else:
        if n == 2 or n == 3:
            print(-1)
        else:#k == 1, n >= 5
            print(*canuse[1 : : 2], *canuse[0 : : 2],)
            
            