---
title: "[Silver I] 정수 삼각형 - 1932"
tags: ["백준", "Silver I"]
---

# [Silver I] 정수 삼각형 - 1932 

[문제 링크](https://www.acmicpc.net/problem/1932) 

### 성능 요약

메모리: 111748 KB, 시간: 124 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<pre>        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5</pre>

<p>위 그림은 크기가 5인 정수 삼각형의 한 모습이다.</p>

<p>맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.</p>

<p>삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.</p>

### 입력 

 <p>첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.</p>

### 출력 

 <p>첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/1932



n = int(input())

pyramid = list()

for _ in range(n):
    temp = list(map(int, input().split()))
    pyramid.append(temp)





# print(*pyramid, sep = '\n')


for i in range(1, len(pyramid)):
    for i2 in range(len(pyramid[i])):
        temp = pyramid[i][i2]
        if 0 <= i2 < len(pyramid[i - 1]):
            temp = max(pyramid[i-1][i2]+ pyramid[i][i2], pyramid[i][i2])

            
        if 0 <= i2 - 1 < len(pyramid[i - 1]):
           temp = max(pyramid[i-1][i2 - 1]+ pyramid[i][i2], temp)
       
        
        pyramid[i][i2] = temp

print(max(pyramid[-1]))
```
