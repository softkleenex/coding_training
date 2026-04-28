---
title: "[Bronze V] UOS 문자열 - 32929"
tags: ["백준", "Bronze V"]
---

# [Bronze V] UOS 문자열 - 32929 

[문제 링크](https://www.acmicpc.net/problem/32929) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 구현, 문자열, 사칙연산

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>UOS 문자열이란 <span style="color:#e74c3c;"><code>UOSUOSUOSU...</code></span>와 같이 <span style="color:#e74c3c;"><code>UOS</code></span>가 무한히 반복되어 나타나는 문자열이다. 양의 정수 $x$가 주어질 때 UOS 문자열의 $x$번째 문자를 구하여라.</p>

### 입력 

 <p>첫 번째 줄에 $x$가 주어진다. $(1 \leq x \leq 10^9)$</p>

### 출력 

 <p>UOS 문자열의 $x$번째 문자를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python

# UOS 문자열이란 UOSUOSUOSU...와 같이 UOS가 무한히 반복되어 나타나는 문자열이다. 양의 정수 $x$가 주어질 때 UOS 문자열의 $x$번째 문자를 구하여라.

# 입력
# 첫 번째 줄에 $x$가 주어진다. $(1 \leq x \leq 10^9)$ 

# 출력
# UOS 문자열의 $x$번째 문자를 출력한다.

# 예제 입력 1 
# 5
# 예제 출력 1 
# O
# 예제 입력 2 
# 1000000000
# 예제 출력 2 
# U


ans = 'U'
    
n = (int(input()) - 1) % 3 

if n == 0:
    ans = 'U'
elif n == 1:
    ans = 'O'
elif n == 2:
    ans = 'S'
    
print(ans)

```
