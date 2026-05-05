from itertools import *


dices = []
for _ in range(3):
    curr = list(map(int, input().split()))
    dices.append([curr.count(4), curr.count(5), curr.count(6)])

ans = 0.0

for v1, v2, v3 in permutations((0, 1, 2), 3):
    ans += (dices[0][v1] * dices[1][v2] * dices[2][v3]) / (6 * 6 * 6)

print(f"{ans:.10f}")
