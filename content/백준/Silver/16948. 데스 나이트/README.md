---
title: "[Silver I] 데스 나이트 - 16948"
tags: ["백준", "Silver I"]
---

# [Silver I] 데스 나이트 - 16948 

[문제 링크](https://www.acmicpc.net/problem/16948) 

### 성능 요약

메모리: 115120 KB, 시간: 124 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다. 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.</p>

<p>크기가 N×N인 체스판과 두 칸 (r<sub>1</sub>, c<sub>1</sub>), (r<sub>2</sub>, c<sub>2</sub>)가 주어진다. 데스 나이트가 (r<sub>1</sub>, c<sub>1</sub>)에서 (r<sub>2</sub>, c<sub>2</sub>)로 이동하는 최소 이동 횟수를 구해보자. 체스판의 행과 열은 0번부터 시작한다.</p>

<p>데스 나이트는 체스판 밖으로 벗어날 수 없다.</p>

### 입력 

 <p>첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r<sub>1</sub>, c<sub>1</sub>, r<sub>2</sub>, c<sub>2</sub>가 주어진다.</p>

### 출력 

 <p>첫째 줄에 데스 나이트가 (r<sub>1</sub>, c<sub>1</sub>)에서 (r<sub>2</sub>, c<sub>2</sub>)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/16948

import sys
import collections

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

dir = ((-2, -1), (-2, +1), (+2, -1), (+2, + 1), (0, -2), (0, + 2))


# print(r1, c1, r2, c2)
# print(dir)


#case1. r1과 r2의 차이가 홀수라면 절대로 도달 불가능

ans = 0




def bfs(start):
    used = [[-1] * n for _ in range(n)] 
    used[start[0]] [start[1]] = 0
    q = [start]
    for r, c in q:
        if r == r2 and c == c2:
            return used[r][c]
        
        
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n:
                if used[nr][nc] == -1:
                    used[nr][nc] = used[r][c] + 1
                    q.append([nr, nc])
                    
    return -1


print(bfs([r1, c1]))
                    
                    

            




```
