# https://www.acmicpc.net/problem/32377

import bisect

n, x, y, z = map(int, input().split())

time = 0


# print(help(bisect))


left = 1
right = (n * (min(x, y, z)))

# print(left, right)

ans_time = 0

while left <= right:
    mid = (left + right) // 2
    m =  mid // x + mid // y + mid // z
    if n <= m:
        ans_time = mid
        right = mid -1
    else:
        left = mid + 1
        




pre_time = ans_time - 1
cnt = (pre_time // x) + (pre_time // y) + (pre_time // z)

if ans_time % x == 0:
    cnt += 1
    if n == cnt:
        print("A win")
        quit()
if ans_time % y == 0:
    cnt += 1
    if n == cnt:
        print("B win")
        quit()
if ans_time % z == 0:
    cnt += 1
    if n == cnt:
        print("C win")
        quit()