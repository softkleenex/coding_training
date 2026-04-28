---
title: "[Bronze II] 카드 공장 (Small) - 17273"
tags: ["백준", "Bronze II"]
---

# [Bronze II] 카드 공장 (Small) - 17273 

[문제 링크](https://www.acmicpc.net/problem/17273) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>진서는 CTP 카드 공장의 노동자이다. 공장에는 <em>N</em>개의 카드가 있으며 각 카드에는 앞면과 뒷면에 숫자가 쓰여있다. 공장장 노진의 명령에 따라서 진서는 카드를 뒤집어야 한다. 명령은 <em>M</em>번 내려지게 되며, 명령은 다음과 같다.</p>

<p><strong>“공장장 노진이 <em>K</em>라는 수를 말하게 되면 진서는 <em>N</em>개의 카드 중 보이고 있는 면이 <em>K</em>이하인 카드를 모두 뒤집어야 한다.”</strong></p>

<p>그리고 공장장의 명령이 끝났을 때, 카드의 보이는 면의 수들의 합을 공장장에게 보고해야 한다.</p>

<p>예를 들면 다음 그림과 같다.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 650px; height: 348px;"></p>

<p><strong>카드들은 처음에 모두 앞면이 보여지도록 세팅되어 있고, 카드에 적힌 수는 10,000 이하의 자연수이다.</strong></p>

### 입력 

 <p>첫 번째 줄에 <em>N</em>과 <em>M</em>이 주어진다. (<em>N </em>= 1, <em>M은 </em>100 이하의 자연수)</p>

<p>그리고 다음 <em>N</em>개의 줄에 카드의 앞면 A<sub>i</sub>와 뒷면 B<sub>i</sub>가 주어진다. (A<sub>i</sub>와 B<sub>i</sub>는 10,000 이하의 자연수)</p>

<p>그리고 다음 <em>M</em>개의 줄에 공장장이 말하는 수 <em>K</em>가 주어진다. (<em>K</em>는 10,000 이하의 자연수)</p>

### 출력 

 <p>명령이 끝났을 때 보이고 있는 카드들의 합을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct card{
	int front;
	int back;
	int now;
}card;


void check(card temp[], int len, int data)
{	
	for (int a = 0; a < len; a++)
	{
		if (temp[a].now <= data)
		{
			temp[a].now = (temp[a].now == temp[a].front) ? temp[a].back : temp[a].front;
		}
	}
}

int main() {
	int N = 0; int M = 0;
	scanf("%d %d", &N, &M);//앞면, 뒷면
	
	card* cards;
	cards = (card*)malloc(sizeof(card) * N);
	
	for (int a= 0; a < N; a++)
	{
		cards[a].front = 0; cards[a].back = 0; cards[a].now = 0;
		scanf("%d %d", &cards[a].front, &cards[a].back); 
		cards[a].now = cards[a].front;
	}
	
	for (int a = 0; a < M; a++)
	{
		int data = 0; scanf("%d", &data);
		check(cards, N, data);
	}


	int sum = 0;
	for (int a = 0; a < N; a++)
	{
		sum += cards[0].now;
	}


	printf("%d", sum);



	return 0;
}
```
