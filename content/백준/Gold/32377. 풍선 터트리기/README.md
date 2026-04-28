---
title: "[Gold III] 풍선 터트리기 - 32377"
tags: ["백준", "Gold III"]
---

# [Gold III] 풍선 터트리기 - 32377 

[문제 링크](https://www.acmicpc.net/problem/32377) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2026년 3월 7일 22:05:20

### 문제 설명

<p>A, B, C 3명이 $N$개의 풍선을 터트리는 게임을 합니다.</p>

<ul>
	<li>A는 $x$분마다 하나의 풍선을 터트립니다. (A는 게임 시작 후 $x, 2x, 3x$...분에 풍선을 터트립니다.)</li>
	<li>B는 $y$분마다 하나의 풍선을 터트립니다. (B는 게임 시작 후 $y, 2y, 3y$...분에 풍선을 터트립니다.)</li>
	<li>C는 $z$분마다 하나의 풍선을 터트립니다. (C는 게임 시작 후 $z, 2z, 3z$...분에 풍선을 터트립니다.)</li>
	<li>동시에 두 명 이상이 풍선을 터트리는 경우 A, B, C순으로 풍선을 터트립니다.</li>
</ul>

<p>마지막 풍선을 터트리는 사람이 승리한다고 했을 때 A, B, C 중 승자를 출력해주세요.</p>

### 입력 

 <p>첫 번째 줄에 풍선의 개수 $N$과, 풍선을 터트리는 데 걸리는 시간 $x, y, z$가 주어집니다. ($1 ≤ N, x, y, z ≤ 10^9$, $N, x, y, z$는 모두 정수입니다.)</p>

### 출력 

 <p>게임의 승자를 출력해주세요. A가 승자일 경우 <span style="color:#e74c3c;"><code>A win</code></span>을, B가 승자일 경우 <span style="color:#e74c3c;"><code>B win</code></span>을, C가 승자일 경우 <span style="color:#e74c3c;"><code>C win</code></span>을 출력해주세요.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
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
```
