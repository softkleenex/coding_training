---
title: "[Bronze II] 블랙잭 - 2798"
tags: ["백준", "Bronze II"]
---

# [Bronze II] 블랙잭 - 2798 

[문제 링크](https://www.acmicpc.net/problem/2798) 

### 성능 요약

메모리: 31120 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2026년 04월 25일 22:15:05

### 문제 설명

<p>카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.</p>

<p>한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.</p>

<p>김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.</p>

<p>이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.</p>

<p>N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.</p>

### 입력 

 <p>첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.</p>

<p>합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.</p>

### 출력 

 <p>첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```python
def check(m, arr):
	data = 0
	for i in arr:
		data = data + i
		
	if data > m:
		return 0
	else:
		#print(data)
		return data
			
def combination(m, arr):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    maxsum = [0]

    # 2.
    def generate(chosen):
        if len(chosen) == 3:
            maxsum[0] = max(maxsum[0], check(m, chosen))
            return

    	# 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])
    return maxsum[0]




#n과 M 을  A B형식으로 입력 받기

N, M = [int(x) for x in input().split()]


arr1 =  list(map(int, input().split()))


#print(N, M, arr1)


print(combination(M, arr1))



```
