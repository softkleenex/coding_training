---
title: "[Silver I] 행렬 - 1080"
tags: ["백준", "Silver I"]
---

# [Silver I] 행렬 - 1080 

[문제 링크](https://www.acmicpc.net/problem/1080) 

### 성능 요약

메모리: 111012 KB, 시간: 112 ms

### 분류

그리디 알고리즘

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.</p>

<p>행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)</p>

### 입력 

 <p>첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.</p>

### 출력 

 <p>첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/1080


n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input())))
    
for i in range(n):
    b.append(list(map(int, input())))
    
    
# print(*a, sep = '\n')
# print()
# print(*b, sep = '\n')

def flip(target, y, x):
    dir = ((-1, -1), (-1, 0), (-1, 1), 
           (0, -1), (0, 0), (0, 1),
           (1, -1), (1, 0), (1, 1))
    
    for ny, nx in dir:
        n = target[y + ny][x + nx]
        target[y + ny][x + nx] = 1 if n == 0 else 0


ans = 0

for y in range(1, n-1):
    for x in range(1, m-1):
        if a[y - 1][x - 1] != b[y - 1][x - 1]:
            flip(a, y, x)
            # print(y, x)
            ans += 1
            
            
if a == b:
    print(ans)
else:
    print(-1)
    
    # print(*a, sep = '\n')
    # print()
    # print(*b, sep = '\n')
```
