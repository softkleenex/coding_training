---
title: "[Silver III] N과 M (3) - 15651"
tags: ["백준", "Silver III"]
---

# [Silver III] N과 M (3) - 15651 

[문제 링크](https://www.acmicpc.net/problem/15651) 

### 성능 요약

메모리: 259984 KB, 시간: 1020 ms

### 분류

백트래킹

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.</p>

<ul>
	<li>1부터 N까지 자연수 중에서 M개를 고른 수열</li>
	<li>같은 수를 여러 번 골라도 된다.</li>
</ul>

### 입력 

 <p>첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)</p>

### 출력 

 <p>한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.</p>

<p>수열은 사전 순으로 증가하는 순서로 출력해야 한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
# https://www.acmicpc.net/problem/15651

n,m = map(int, input().split())
#~n 까지, m개 고르기

n = list(i for i in range(1, n + 1))

ans = []

def back(buck):#now는 n의 인덱스, buck은 현재 바구니
    if len(buck) == m:#바구니의 길이가 m개라면, 즉 고를수 있는만큼 골랐다면
        ans.append(buck)#현재 바구니를 정답지에 추가한다
        return
    
    
    for i in range(0, len(n)):
        back(buck + [n[i]])



back([])

# print(ans)

ans.sort()

for v in ans:
    print(*v, sep = ' ')
```
