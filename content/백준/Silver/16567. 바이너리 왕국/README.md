---
title: "[Silver III] 바이너리 왕국 - 16567"
tags: ["백준", "Silver III"]
---

# [Silver III] 바이너리 왕국 - 16567 

[문제 링크](https://www.acmicpc.net/problem/16567) 

### 성능 요약

메모리: 222584 KB, 시간: 868 ms

### 분류

구현, 애드 혹, 시뮬레이션

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>바이너리 왕국의 불쌍한 하인들은 매일 바이너리 길을 청소한다. 바이너리 길은 N개의 0 또는 1로 이루어진 수열이다.</p>

<p>0은 깨끗한 칸, 1은 더러운 칸을 의미한다.</p>

<p>그들은 "flip"이라는 기술만을 사용해서 청소를 한다. 이것은 연속된 더러운 칸을 깨끗하게 만드는 기술이다. 즉, 연속된 1을 모두 0으로 만든다.</p>

<p>바이너리 왕국의 악덕한 왕은 매일 하인들에게 M개의 시련을 내리는 것이 취미이다. 시련에는 2가지 종류가 있는데 다음과 같다.</p>

<ul>
	<li>"0": 현재 길의 모든 칸을 깨끗하게 만들기 위한 <strong>"flip"의 최소 횟수</strong>를 하인들에게 크게 외치게 한다.</li>
	<li>"1 i": 바이너리 길의 i번째 칸을 더럽힌다. 단, 이미 더럽혀져 있다면 아무 일도 일어나지 않는다.</li>
</ul>

<p>바이너리 왕국의 불쌍한 하인들의 슬픈 외침들을 출력하라.</p>

### 입력 

 <p>첫째 줄에 바이너리 길의 칸의 개수 N, 시련의 개수 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)</p>

<p>둘째 줄에 N개의 현재 바이너리 길의 상태가 주어진다.</p>

<p>그다음 M개의 줄에 걸쳐서 시련이 주어진다. 이때 0번 시련은 "0", 1번 시련은 "1 i"와 같이 주어진다. (1 ≤ i ≤ N)</p>

### 출력 

 <p>0번 시련이 주어졌을 때, 하인들의 외침을 개행으로 구분하여 출력하라.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/16567

from sys import stdin
from collections import deque
input = stdin.readline

from bisect import bisect_left

n, m = map(int, input().split())

road = list(map(int, input().split()))




tesk = deque()

for _ in range(m):
    temp = list(map(int, input().split()))
    tesk.append(temp) 



ans = 0

for i, v in enumerate(road):
   
        if v == 1 and  (i == 0 or road[i - 1] == 0):
            ans += 1





while tesk:
    now = tesk.popleft()
    if now[0] == 1:#더럽히는 시련이라면
        nowidx = now[1] - 1
       # 새롭게 더럽혀지는 경우만 갱신
        if road[nowidx] == 0:
            road[nowidx] = 1

            left = nowidx - 1
            left_clean = 0 <= left and road[left] == 0
            left_dirty = 0 <= left and road[left] == 1
            
            right = nowidx + 1
            right_clean  = right < n and road[right] == 0
            right_dirty = right < n and road[right] == 1

            if left_dirty and right_dirty:#둘다 더러움
                 ans -= 1
            elif left_clean and right_clean:#둘다 꺠끗함
                 ans += 1
            elif (left_clean and not right_dirty) or (not left_dirty and right_clean):
                ans += 1

            


        
    elif now[0] == 0:
        print(ans)
    else:
        print('error')
```
