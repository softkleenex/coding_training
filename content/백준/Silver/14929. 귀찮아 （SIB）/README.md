---
title: "[Silver IV] 귀찮아 (SIB) - 14929"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 귀찮아 (SIB) - 14929 

[문제 링크](https://www.acmicpc.net/problem/14929) 

### 성능 요약

메모리: 120928 KB, 시간: 112 ms

### 분류

수학, 누적 합

### 제출 일자

2025년 5월 20일 17:52:04

### 문제 설명

<p>\[\sum_{1 \le a < b \le n}{x_ax_b}\]</p>

### 입력 

 <p>n과 x<sub>i</sub>가 주어짇나. n은 10만 이하ㅇ고, x<sub>i</sub>는 젗ㄹ댓값이 100이하인 정수디이다.</p>

### 출력 

 <p>위에서 구하란 걸 구하면 된ㄷ.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
import sys
input = sys.stdin.readline

import itertools

n = int(input())

# print(help(itertools.combinations))

nums =(list(map(int, input().split())))

ans1 = (pow(sum(nums) , 2)) 

ans2 = sum(pow(num, 2) for num in nums)


print((ans1 - ans2) // 2)
```
