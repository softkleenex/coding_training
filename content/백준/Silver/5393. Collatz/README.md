---
title: "[Silver III] Collatz - 5393"
tags: ["백준", "Silver III"]
---

# [Silver III] Collatz - 5393 

[문제 링크](https://www.acmicpc.net/problem/5393) 

### 성능 요약

메모리: 34536 KB, 시간: 32 ms

### 분류

수학

### 제출 일자

2025년 3월 9일 15:07:07

### 문제 설명

<p>In the process to solve the Collatz conjecture, better known as the 3n + 1 problem, Carl created a physical model with wood and ropes. A wooden bar contains a hole for every natural number from 1 to inﬁnity from left to right. For every even number m there is a rope connecting the mth hole with hole m/2. For every odd number n there is a rope connecting the nth hole with hole 3n + 1.</p>

<p>For an important conference where Carl plans to elaborate on his results, he wants to bring his structure, but it is too large to ﬁt in his bag. So he decided to saw oﬀ the part of the bar containing the ﬁrst N holes only. How many ropes will he need to cut?</p>

### 입력 

 <p>The ﬁrst line of the input contains a single number: the number of test cases to follow. Each test case has the following format:</p>

<ul>
	<li>One line with an integer N, satisfying 0 ≤ N ≤ 10<sup>9</sup>.</li>
</ul>

### 출력 

 <p>For every test case in the input, the output should contain a single number, on a single line: the number of ropes that need to be cut.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 문제
# In the process to solve the Collatz conjecture, better known as the 3n + 1 problem, 
# Carl created a physical model with wood and ropes. A wooden bar contains a hole for every natural 
# number from 1 to inﬁnity from left to right. For every even number m there is a rope connecting 
# the mth hole with hole m/2. For every odd number n there is a rope connecting the nth hole with hole 3n + 1.

# For an important conference where Carl plans to elaborate on his results, 
# he wants to bring his structure, but it is too large to ﬁt in his bag. So he decided to saw oﬀ the part of the bar containing the ﬁrst N holes only. How many ropes will he need to cut?

# 입력
# The ﬁrst line of the input contains a single number: the number of test cases to follow. 
# Each test case has the following format:

# One line with an integer N, satisfying 0 ≤ N ≤ 109.
# 출력
# For every test case in the input, the output should contain a single number, 
# on a single line: the number of ropes that need to be cut.
import math
import sys
input = sys.stdin.readline


n = int(input())


for _ in range(0, n):
    t = int(input())
    #1~target에 연결된, target보다 큰 경우의 개수를 세야한다!
    #3 > 2 ~ 3 (2)
    #5 > 3 ~ 5 (3)
    #12 > 7 ~ 12 (6)
    #240 > 121 ~ 240 (120)
    t_even = math.ceil((t) / 2)
    #3 > 1 ~ 3(2) = 2
    #5 > 3 ~ 5 (3 ~ 2) = 2
    #12 > 5... 11 (6 ~ 3) = 4
    #240 > 81....239 (120 ~ 41) = 80
    #t ~ (N - 1) // 3 + 1사이의 홀수 개수는?
    t1_odd = (t - 1) // 3 if (t - 1) // 3 % 2 == 1 else (t - 1) // 3  + 1
    while t1_odd * 3 + 1 <= t:
        t1_odd += 2
    #print(t1_odd)
    t_odd = (t + 1) // 2 - (t1_odd + 1) // 2 + 1


    print(t_even + t_odd)
```
