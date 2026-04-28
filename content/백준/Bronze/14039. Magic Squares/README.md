---
title: "[Bronze III] Magic Squares - 14039"
tags: ["백준", "Bronze III"]
---

# [Bronze III] Magic Squares - 14039 

[문제 링크](https://www.acmicpc.net/problem/14039) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each row, all add up to the same total.</p>

<p>Given a 4 × 4 square of numbers, determine if it is magic square.</p>

### 입력 

 <p>The input consists of four lines, each line having 4 space-separated integers.</p>

### 출력 

 <p>Output either magic if the input is a magic square, or not magic if the input is not a magic square.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in each row, all add up to the same total.

# Given a 4 × 4 square of numbers, determine if it is magic square.

# 입력
# The input consists of four lines, each line having 4 space-separated integers.

# 출력
# Output either magic if the input is a magic square, or not magic if the input is not a magic square.


m = "magic"
nm = "not magic"

a = [[0 for _ in range(0, 4)] for __ in range(0, 4)]

# print(*a, sep = '\n')

for i in range(0 , 4):
    a[i] = list(map(int, input().split()))

t = int(sum(a[0]))


for i in range(0, 4):
    if t != sum(a[i]):
        print(nm)
        quit()


for i in range(0, 4):
    s = 0
    for i2 in range(0, 4):
        s += a[i2][i]
    if s != t:
        #print(i, i2)
        print(nm)
        quit

print(m)
```
