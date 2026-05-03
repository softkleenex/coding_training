---
title: "[AtCoder] D_Card_Pile_Query"
tags: ["AtCoder", "abc455"]
---

# D_Card_Pile_Query

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc455** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc455/tasks/abc455_d)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
N개의 카드들과 N개의 파일 더미들이 있다.
카드와 더미들은 1, 2, ..., N까지의 숫자가 존재한다. 시작에는, pile i번은 오직 카드 i를 포함한다.
다음에 제시되는 작업을  각 i = 1, 2,..., Q에 대해서 순서대로 수행하라.
- 카드 C_i와 그 위에 쌓여있는 모든카드를 이동하십시오, 그들의 순서는 유지됩니다, 움직이는 위치는 카드 P_i위 입니다.
작업을 수행하기 전에, 카드 C_i와 P_i는 다른 pile에 존재합니다, 그리고 P_i는 어떤 더위의 꼭대기에 존재합니다.
각 더미의 모든 카드의 개수를 구해내야한다.

이 문제에서는 c가 최하단인경우에, c가 속해있는 카드더미는 더이상 사용될수 없다. 따라서 bottom_of_plie[c] = 0으로, 즉 카드 번호를 카드 더미 자체로 간주하여도 된다는 조건을 명심해야한다. 또한 쿼리수행이 많아질수 있기 때문에 연결리스트로 해결해야한다.



## 💻 코드

```python
import itertools
import collections
from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())

under = [0] * (n + 1)#i번 카드 아래에있는 카드 start 1
over = [0] * (n + 1)#i번 카드 위에있는 카드 번호, start 1
bottom_of_pile = list(range(0, n + 1))#i번 더미의 바닥에있는 카드 번호

for _ in range(q):
    c, p = map(int, input().split())
    if under[c] == 0:#만약 c가 최하단의카드였다면
        over[p] = c#p위는 c가 된거
        under[c] = p#c아래는 p가 된다
        #bottom_of_pile[bottom_of_pile.index(c)] = 0#c의 원래 카드더미의 아래는 0이되는데,,,
        bottom_of_pile[c] = 0#c의 원래 카드더미의 아래는 0이되는데,,,
    else:#c가 최하단이 아니었다면
        over[under[c]] = 0#c의 아래에있던 카드의 over을 갱신켜준다.
        under[c] = p
        over[p] = c

ans = []
for i in range(1, n + 1):
    curr = bottom_of_pile[i]
    count = 0
    while curr != 0:
        count +=1
        curr = over[curr]
    ans.append(count)

print(*(ans))

```
