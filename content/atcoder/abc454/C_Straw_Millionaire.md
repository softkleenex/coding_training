---
title: "[AtCoder] C_Straw_Millionaire"
tags: ["AtCoder", "abc454"]
---

# C_Straw_Millionaire

이 문제는 AtCoder에서 푼 문제입니다.
이 문제는 **abc454** 콘테스트 문제입니다.

🔗 [문제 바로가기](https://atcoder.jp/contests/abc454/tasks/abc454_c)


---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->
주어진 조건은 그래프에 걸맞다, DFS로 해결하였다.



## 💻 코드

```python
from collections import *

n, m = map(int, input().split())
fri = list()
fg = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a in fg.keys():
        fg[a].append(b)
    else:
        fg[a] = [b]

# print(fg)
item = [1]
ans = set([1])


while len(item) > 0:
    curr = item.pop()
    if curr in fg.keys():
        for v in fg[curr]:
            if v in ans:
                pass
            else:
                ans.add(v)
                item.append(v)

print(len(ans))

```
