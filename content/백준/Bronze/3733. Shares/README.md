---
title: "[Bronze V] Shares - 3733"
tags: ["백준", "Bronze V"]
---

# [Bronze V] Shares - 3733 

[문제 링크](https://www.acmicpc.net/problem/3733) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

수학, 사칙연산

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>A group of N persons and the ACM Chief Judge share equally a number of S shares (not necessary all of them). Let x be the number of shares aquired by each person (x must be an integer). The problem is to compute the maximum value of x.</p>

<p>Write a program that reads pairs of integer numbers from an input text file. Each pair contains the values of 1 ≤ N ≤ 10000 and 1 ≤ S ≤ 10<sup>9</sup> in that order. The input data are separated freely by white spaces, are correct, and terminate with an end of file. For each pair of numbers the program computes the maximum value of x and prints that value on the standard output from the beginning of a line, as shown in the example below.</p>

### 입력 

 Empty

### 출력 

 Empty



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
line1 = []

while True:
    try:
        line2 = list(map(int, input().split()))

        if not(1 <= line2[0] <= 10000, 1<= line2[1] <= 10**9):
            line2 = map(int, input().split())
        
        line2[0] = line2[0] + 1
        
        if(line2[1] % line2[0] == 0):
            line1.append(line2[1] // line2[0])
        else :
            line1.append(line2[1] // line2[0])
        
    except EOFError:
        break


for i in line1:
    print(i)



```
