---
title: "[Bronze I] 최대공약수와 최소공배수 - 2609"
tags: ["백준", "Bronze I"]
---

# [Bronze I] 최대공약수와 최소공배수 - 2609 

[문제 링크](https://www.acmicpc.net/problem/2609) 

### 성능 요약

메모리: 31120 KB, 시간: 48 ms

### 분류

수학, 정수론, 유클리드 호제법

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.</p>

### 출력 

 <p>첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
def find1(arr):
	for i in range (max(arr), 0, -1):
		if(arr[0] % i == 0 and arr[1] % i == 0):
			return i
	return False
		
def find2(arr):
	num1 = min(arr)
	while True:
		if(num1 % max(arr)) == 0 and num1 >= max(arr):
			return num1
		elif(num1 >= min(arr) * max(arr)): 
				return min(arr)*max(arr)
		else:
			num1 = num1 + min(arr)
		#	print("!", num1)
		

arr_numbers = list(map(int, input().split()))


print(find1(arr_numbers))
print(find2(arr_numbers))
```
