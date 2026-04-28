---
title: "[Silver III] 구간 합 구하기 4 - 11659"
tags: ["백준", "Silver III"]
---

# [Silver III] 구간 합 구하기 4 - 11659 

[문제 링크](https://www.acmicpc.net/problem/11659) 

### 성능 요약

메모리: 41144 KB, 시간: 284 ms

### 분류

누적 합

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.</p>

### 출력 

 <p>총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

# 제한
# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N

import sys
input = sys.stdin.readline


n, m = map(int, input().split())
list1 = list(map(int, input().split()))



list2 = list1[:]

if n > 0:
    for i in range(1, len(list2)):
        list2[i] += list2[i-1]
                          


#print(list1, list2)

#list1[x] < 0 1 2 ... list[x] 까지의 누적합이 있다
#

for i in range(0, m):
    a, b =  map(int, input().split())
    a -= 1
    b -= 1
    print(list2[b] - list2[a] + list1[a])
```
