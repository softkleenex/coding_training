---
title: "[Bronze V] 문자와 문자열 - 27866"
tags: ["백준", "Bronze V"]
---

# [Bronze V] 문자와 문자열 - 27866 

[문제 링크](https://www.acmicpc.net/problem/27866) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

구현, 문자열

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>단어 $S$와 정수 $i$가 주어졌을 때, $S$의 $i$번째 글자를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 $S$가 주어진다. 단어의 길이는 최대 $1\,000$이다.</p>

<p>둘째 줄에 정수 $i$가 주어진다. ($1 \le i \le \left|S\right|$)</p>

### 출력 

 <p>$S$의 $i$번째 글자를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
a = input().strip()

if not(len(a) <= 1000):
    a = input().strip()


b = int(input().strip())

if not(1 <= b <= len(a)):
    b = int(input().strip())
    
    
c = list(a)

print(c[b-1])
```
