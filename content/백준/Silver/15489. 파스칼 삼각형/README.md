---
title: "[Silver IV] 파스칼 삼각형 - 15489"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 파스칼 삼각형 - 15489 

[문제 링크](https://www.acmicpc.net/problem/15489) 

### 성능 요약

메모리: 108384 KB, 시간: 100 ms

### 분류

수학, 다이나믹 프로그래밍, 조합론

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>파스칼 삼각형은 아래와 같은 모양으로 이루어져 있다. 양 끝을 제외한 각 수는 자신의 바로 왼쪽 위의 수와 바로 오른쪽 위의 수의 합으로 되어있다.</p>

<p style="text-align:center"><img alt="" src="" style="height:254px; width:400px"></p>

<p>이때 R번째 줄, C번째 수를 위 꼭짓점으로 하는 한 변이 포함하는 수의 개수가 W인 정삼각형과 그 내부를 생각하자. 정삼각형의 변과 그 내부에 있는 수들의 합을 구하고 싶다. 예를 들면, 3번 째 줄, 1번 째 수를 꼭짓점으로 하고 한 변이 포함하는 수의 개수가 4인 정삼각형과 그 내부에 있는 수의 합은 1+(1+3)+(1+4+6)+(1+5+10+10) = 42 이다.</p>

<p>주어진 R, C, W에 대해서 그에 해당하는 합을 구하는 프로그램을 작성하여라.</p>

### 입력 

 <p>첫째 줄에 양의 정수 R, C, W가 공백을 한 칸씩 두고 차례로 주어진다. (단, 2 ≤ R+W ≤ 30, 2 ≤ C+W ≤ 30, 1 ≤ W ≤ 29, C ≤ R)</p>

### 출력 

 <p>첫째 줄에 R번째 줄, C번째 수를 위 꼭짓점으로 하는 한 변이 포함하는 수의 개수가 W인 정삼각형과 그 내부에 있는 수들의 합을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/15489
from sys import stdin
input = stdin.readline

r, c, w = map(int, input().split())


#r, c에서 출발해서, w만큼을 내려가야 한다

triangle = [[1]]

for x in range(1, r + w -1):
    temp = [1]
    for x2 in range(1, x):
        temp.append(triangle[x - 1][x2-1] + triangle[x - 1][x2] )
    temp.append(1)
    triangle.append(temp)

# print(*triangle, sep = '\n')



ans = 0

start = [r-1, c-1]



for x in range(w):


    for x2 in range(0, x+1):
        
        # print(start[0], start[1] + x2, triangle[start[0]][ start[1] + x2])
        ans += triangle[start[0]][ start[1] + x2]

    start[0] += 1

print(ans)
```
