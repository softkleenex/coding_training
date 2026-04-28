---
title: "[Bronze I] 수 정렬하기 3 - 10989"
tags: ["백준", "Bronze I"]
---

# [Bronze I] 수 정렬하기 3 - 10989 

[문제 링크](https://www.acmicpc.net/problem/10989) 

### 성능 요약

메모리: 31120 KB, 시간: 7260 ms

### 분류

정렬

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
import sys
N = int(sys.stdin.readline().strip())
list1= [0] * 10001

for _ in range(N):
	a = int(sys.stdin.readline().strip())
	list1[a] += 1
	
for index, value in enumerate(list1):
	if value != 0:
		for i in range(value):
			sys.stdout.write(f"{index}\n")
```
