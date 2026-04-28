---
title: "[Silver IV] 블록 놀이 - 16951"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 블록 놀이 - 16951 

[문제 링크](https://www.acmicpc.net/problem/16951) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>욱제는 높이가 1인 블록을 매우 많이 가지고 있고, 블록을 쌓아서 탑 N개를 만들었다. 탑은 일렬로 배열했고, 왼쪽에서부터 i번째 탑의 높이는 A<sub>i</sub>이다.</p>

<p>욱제가 가장 좋아하는 정수는 K이다. 따라서, 인접한 두 탑의 높이 차이를 K로 만들려고 한다. 즉, A<sub>i+1</sub> - A<sub>i</sub> = K를 만족해야 한다.</p>

<p>욱제가 1분 동안 할 수 있는 작업은 탑 하나를 고르고, 탑에 블록을 더 놓아서 높이를 크게 만드는 것 또는 탑에서 블록을 빼서 높이를 작게 만드는 것이다. 인접한 두 탑의 높이 차이를 K로 만드는데 필요한 시간을 구해보자. 욱제는 손이 매우 빠르기 때문에, 1분 동안 놓을 수 있는 블록 또는 뺄 수 있는 블록의 개수는 무한대이다.</p>

<p>탑의 높이는 항상 1보다 크거나 같아야 한다.</p>

### 입력 

 <p>첫째 줄에 탑의 수 N, 욱제가 가장 좋아하는 정수 K가 주어진다.</p>

<p>둘째 줄에는 탑의 높이 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 모든 인접한 두 탑의 높이 차이를 K로 만드는 최소 시간을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#include <stdio.h>
#include <stdlib.h>

///https://www.acmicpc.net/problem/16951

int block(int start, int N, int tow[], int K)
{
	int mintime = 0;
	int temptime = 0;

	int temptow[1001];
	for (int a = 0; a < 1001; a++)
	{
		temptow[a] = tow[a];
	}

	for (int a = 1; a <= 1000; a++)
	{
		if (temptow[0] != a)
		{
			temptow[0] = a;
			temptime++;
		}
		for (int b = 1; b < N; b++)
		{
			if (temptow[b] != temptow[b - 1] + K)
			{
				temptow[b] = temptow[b - 1] + K;
				temptime++;
			}
		}

		if (a == 1 || mintime > temptime)
		{
			mintime = temptime;
		}

		temptime = 0;
		for (int a = 0; a < 1001; a++)
		{
			temptow[a] = tow[a];
		}
	}

	return mintime;
}

int main(int argc, char *argv[])
{
	int tow[1001] = {-1};

	int N = 0;
	int K = 0;

	scanf("%d", &N);
	scanf("%d", &K);

	for (int a = 0; a < N; a++)
	{
		scanf("%d", &tow[a]);
	}

	printf("%d", block(0, N, tow, K));

	return 0;
}
```
