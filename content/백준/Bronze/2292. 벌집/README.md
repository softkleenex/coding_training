---
title: "[Bronze II] 벌집 - 2292"
tags: ["백준", "Bronze II"]
---

# [Bronze II] 벌집 - 2292 

[문제 링크](https://www.acmicpc.net/problem/2292) 

### 성능 요약

메모리: 111336 KB, 시간: 108 ms

### 분류

수학

### 제출 일자

2026년 3월 27일 19:01:09

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="height:397px; width:363px"></p>

<p>위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.</p>

### 입력 

 <p>첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.</p>

### 출력 

 <p>입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
#https://www.acmicpc.net/problem/2292

import sys
import collections 
import heapq
import itertools 
input = sys.stdin.readline
# sys.setrecursionlimit(10**6) 

#1 > (1)은 0 번
#1 + 1 ~ 1 + 6 까지는 1번
#7 + 1 ~ 7 + 12 까지는 2번
#19 + 1 ~ 19 + 18까지는 3번


n = int(input())

ans = 0
a = 0
b = 1

if n == 1:
    print(1)
    quit()

while not(b >= n and n >= a):
    a = b + 1
    b = b + 6 * ans
    #print(a, b)#(1, 1) #(2, 7)#(8, 19)
    ans += 1
    
print (ans)
```
