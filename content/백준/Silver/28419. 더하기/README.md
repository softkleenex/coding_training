---
title: "[Silver IV] 더하기 - 28419"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 더하기 - 28419 

[문제 링크](https://www.acmicpc.net/problem/28419) 

### 성능 요약

메모리: 122424 KB, 시간: 116 ms

### 분류

수학, 애드 혹

### 제출 일자

2025년 6월 5일 21:53:22

### 문제 설명

<p>정수로 구성된 수열 $A_1, A_2, \cdots, A_N$이 주어진다. 우리는 이 수열에 아래 연산을 원하는 만큼 반복할 수 있다.</p>

<ul>
	<li>인접한 세 값을 1씩 증가시킨다.</li>
</ul>

<p>이 연산을 최소한으로 사용해 수열의 홀수 번째 위치의 합과 짝수 번째 위치의 합을 같게 만들고자 한다. 최소 몇 번의 연산을 해야 홀수 번째 위치와 짝수 번째 위치의 합이 같아지는지 구하시오. 만약 홀수 번째 위치의 합과 짝수 번째 위치의 합을 같게 만들 수 없다면 <code>-1</code>을 출력한다.</p>

### 입력 

 <p>첫째 줄에 수열의 길이 $N$이 주어진다. $(3 \le N \le 100\,000)$</p>

<p>둘째 줄에 길이가 $N$인 수열 $A_1, A_2, A_3, \cdots, A_N$이 공백으로 구분되어 주어진다. $(-100\,000 \le A_i \le 100\,000)$</p>

### 출력 

 <p>홀수 번째 위치의 합과 짝수 번째 위치의 합을 같게 만들기 위한 최소 연산 수를 출력한다. 불가능하다면 <code>-1</code>을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/28419

n = int(input())
list1 = list(map(int, input().split()))

a = 0
for x in range(0, len(list1) + 1, 2):
    if x < len(list1):
        a += list1[x]


b = 0
for x in range(1, len(list1) + 1, 2):
    if x < len(list1):
        b += list1[x]

if n == 3 and a > b:
    print(-1)
else:
    print(abs(a - b))
```
