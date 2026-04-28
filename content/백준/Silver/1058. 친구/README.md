---
title: "[Silver II] 친구 - 1058"
tags: ["백준", "Silver II"]
---

# [Silver II] 친구 - 1058 

[문제 링크](https://www.acmicpc.net/problem/1058) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 최단 경로, 플로이드–워셜

### 제출 일자

2024년 11월 19일 12:57:04

### 문제 설명

<p>지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.</p>

<p>A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.</p>

### 입력 

 <p>첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.</p>

### 출력 

 <p>첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
 #include <stdio.h>

#include <string.h>

#include <stdlib.h>

void friend_2nd(int d[50][50], int len) {

 	 for(int m=0; m < len; m++)

   	 	for(int s=0; s < len; s++)

    	  	for(int e = 0; e < len; e++)

      	  		if (s != m && m != e && e != m)

							if(d[s][e] > d[s][m] + d[m][e]) d[s][e] = d[s][m] + d[m][e];

}

int main(){

	int N = 0; scanf("%d",  &N);

	int friends [50][50] = {0};

	for(int a = 0; a <N; a++)

	{

		for(int a2 = 0; a2 < N; a2++)

		{

			char temp = '0';

			scanf(" %c", &temp); 

			friends[a][a2] = (temp == 'Y') ? 1 : 999999;

			}

		}

		

	friend_2nd(friends, N);

	

	int max = 0;

	for(int i = 0; i < N; i++)

		{

			int count = 0;

			for(int j = 0; j < N; j++)

				{

					if(i != j && friends[i][j] <= 2) count++;

					}

				max = max >= count ? max : count;

			}

	

	printf("%d", max);

	

	

	

	return 0;

	}
```
