---
title: "[Silver V] 매우 어려운 문제 - 31738"
tags: ["백준", "Silver V"]
---

# [Silver V] 매우 어려운 문제 - 31738 

[문제 링크](https://www.acmicpc.net/problem/31738) 

### 성능 요약

메모리: 109544 KB, 시간: 124 ms

### 분류

수학, 애드 혹, 정수론

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>제목과 다르게 이 문제는 아주 쉽다.</p>

<p>2 이상의 정수 $N$, $M$에 대하여, $N!$을 $M$으로 나눈 나머지를 구하여라.</p>

### 입력 

 <p>첫 번째 줄에 두 정수 $N$과 $M$이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 문제의 답에 해당하는 정수를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/31738
import math


n, m = map(int, input().split())



if n >= m:
    print(0)
else:
    a = 1
    for x in range(1, n + 1):
        a = (a * x) % m
    print(a)
```
