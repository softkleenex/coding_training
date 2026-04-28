---
title: "[Silver I] XOR삼형제 1 - 10728"
tags: ["백준", "Silver I"]
---

# [Silver I] XOR삼형제 1 - 10728 

[문제 링크](https://www.acmicpc.net/problem/10728) 

### 성능 요약

메모리: 112648 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘, 비트마스킹

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p><img alt="" src="" style="height:674px; width:594px"></p>

<p>(위에서 아래로, 오른쪽에서 왼쪽으로 읽어주세요.)</p>

### 입력 

 <p>첫 줄에 테스트 케이스의 수 \(T\)가 주어진다.</p>

<p>이어서 매 테스트 케이스마다 한 줄에 걸쳐 정수 \(N\) 이 주어진다.</p>

<p>이 문제는 두 개의 부분문제로 이루어져 있다.</p>

<p><a href="https://www.acmicpc.net/problem/10728">1번 문제</a>의 입력은 \(1 \leq n \leq 20\)을 만족하며 해결하면 20점을 얻을 수 있다.</p>

<p><a href="https://www.acmicpc.net/problem/10736">2번 문제</a>의 입력은 \(1 \leq n \leq 100\)을 만족하며 해결하면 80점을 얻을 수 있다.</p>

### 출력 

 <p>매 테스트 케이스마다 두 줄에 걸쳐서 답을 출력한다.</p>

<ul>
	<li>첫 줄에는 수열의 길이를 출력한다. </li>
	<li>두 번째 줄에는 조건을 만족하는 수열을 공백으로 구분하여 출력한다. 만약 조건을 만족하는 수열이 여러 개라면, 아무 수열이나 하나 출력한다.</li>
</ul>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/10728

import collections
import itertools
import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    max_len = 0
    max_list = []
    
    def back(now_num, buck, visited):
        global max_len, max_list
        left = n - now_num + 1
        
        if(len(buck) + (left)) <= max_len:
                return
        
        if now_num > n:
            if len(buck) > max_len:
                max_len = len(buck)
                max_list =  buck.copy()
            return

        #우주1: 현재 숫자를 내 바구니에 "넣는" 경으
        
        if not now_num in visited:
            new_visited = visited.copy()
            
            for numbuck in buck:
                new_visited.add(numbuck ^ now_num)
            
            buck.append(now_num)
            
            #바구니에 넣은 상태로 다음 숫자 검사하러 떠나기
            
            back(now_num + 1, buck, new_visited)
            
            #탐색을 끝내고 돌아왔으면, 다른 경우 탐색을 위해서 방금 넣었던것을 다시 뺀다!
            
            buck.remove(now_num)
            
        #우주 2 현재 숫자를 내 바구니에 넣지않고 버리는 경우
        #바구니랑 금지목록은 그대로, 번호만 넘긴다
        
        back(now_num + 1, buck, visited)
                
    back(1, [], set())
    print(max_len)
    print(*max_list)
            
        
            
    
```
