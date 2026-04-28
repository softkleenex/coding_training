---
title: "[Bronze II] Making Change - 27106"
tags: ["백준", "Bronze II"]
---

# [Bronze II] Making Change - 27106 

[문제 링크](https://www.acmicpc.net/problem/27106) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

그리디 알고리즘, 브루트포스 알고리즘

### 제출 일자

2025년 3월 13일 14:27:02

### 문제 설명

<p>Given the amount of a purchase (1 ≤ P ≤ 99) in cents, determine the way to make "change for a dollar" for that purchase. Use four standard US coin denominations: 1, 5, 10, and 25. The way to make change uses the least number coins.</p>

### 입력 

 <p>A single line with one integer, P, the amount of the purchase.</p>

### 출력 

 <p>A single line with four integers telling respectively how many 25 cent, 10 cent, 5 cent, and 1 cent pieces to give as change.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# 문제
# Given the amount of a purchase (1 ≤ P ≤ 99) in cents, determine the way to make "change for a dollar" for that purchase. Use four standard US coin denominations: 1, 5, 10, and 25. The way to make change uses the least number coins.

# 입력
# A single line with one integer, P, the amount of the purchase.

# 출력
# A single line with four integers telling respectively how many 25 cent, 10 cent, 5 cent, and 1 cent pieces to give as change.

# 예제 입력 1 
# 43
# 예제 출력 1 
# 2 0 1 2


p = 100 - int(input())



ans = p // 25
p = p - ans * 25
print(ans, end = ' ')

ans = p // 10
p = p - ans * 10
print(ans, end = ' ')

ans = p // 5
p = p - ans * 5
print(ans, end = ' ')
ans = p // 1
p = p - ans * 1
print(ans, end = ' ')

```
