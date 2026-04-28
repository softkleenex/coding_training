---
title: "[Bronze V] A+B - 4 - 10951"
tags: ["백준", "Bronze V"]
---

# [Bronze V] A+B - 4 - 10951 

[문제 링크](https://www.acmicpc.net/problem/10951) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 이루어져 있다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

### 출력 

 <p>각 테스트 케이스마다 A+B를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python

list1 = []

try:
    while True:
        A, B = map(int, input().split())
        list1.append(A+B)
    
except EOFError:
    for i in list1:
        print(i)
```
