import sys
from collections import deque
input = sys.stdin.readline


def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L = [int(x) * 2 for x in L]

    max_ans = 0


    #2^N 가지의 모든 경우의 수를 비트로 표현한다(00000...0 ~ 111...1)
    for i in range(1 << N):
        curr = 1
        count = 0

        for j in range(N):
            if(i >> j) & 1: #j번쨰 경로를 꺼내서, 1인지 체크한다.
                next_pos = curr + (L[j])
            else:
                next_pos = curr - (L[j])
            if curr * next_pos < 0:
                count += 1

            curr = next_pos
        if count > max_ans:
            max_ans = count

    print(max_ans)


solve()
