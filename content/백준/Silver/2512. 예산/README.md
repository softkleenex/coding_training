---
title: "[Silver II] 예산 - 2512"
tags: ["백준", "Silver II"]
---

# [Silver II] 예산 - 2512 

[문제 링크](https://www.acmicpc.net/problem/2512) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

이분 탐색, 매개 변수 탐색

### 제출 일자

2024년 10월 7일 21:18:14

### 문제 설명

<p>국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 <strong>가능한 한 최대의</strong> 총 예산을 다음과 같은 방법으로 배정한다.</p>

<ol>
	<li>모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.</li>
	<li>모든 요청이 배정될 수 없는 경우에는 특정한 <strong>정수</strong> 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. </li>
</ol>

<p>예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. </p>

<p>여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에는 지방의 수를 의미하는 정수 N이 주어진다. N은 3 이상 10,000 이하이다. 다음 줄에는 각 지방의 예산요청을 표현하는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 값들은 모두 1 이상 100,000 이하이다. 그 다음 줄에는 총 예산을 나타내는 정수 M이 주어진다. M은 N 이상 1,000,000,000 이하이다. </p>

### 출력 

 <p>첫째 줄에는 배정된 예산들 중 최댓값인 정수를 출력한다. </p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int getmin(int *arr, int N)
{
	int temp = arr[0];
	for (int a = 0; a < N; a++)
	{
		temp = temp >= arr[a] ? arr[a] : temp;
	}

	return temp;
}

int getmax(int* arr, int N)
{
	int temp = arr[0];
	for (int a = 0; a < N; a++)
	{
		temp = temp <= arr[a] ? arr[a] : temp;
	}

	return temp;
}


int money(int arr[], int N, int line, int M)
{
	int sum = 0;
	for (int a = 0; a < N; a++)
	{	
		sum += arr[a] > line ? line: arr[a];
	}
	return sum;
}


int main() {
	int N = 0;
	scanf("%d", &N);
	int* arr; 
	arr = (int*)malloc(sizeof(int) * N);
	
	for (int a = 0; a < N; a++)
	{
		scanf("%d", &arr[a]);
	}

	



	int M; scanf("%d", &M);
	int left = 0;
	int right = getmax(arr, N);
	int answer = 0;

	
	while (left <= right)
	{
		int mid = (left + right) / 2;
		int sum = money(arr, N, mid, M);
		if (sum <= M)
		{
			answer = mid;
			left = mid + 1;
		}else
		{
			right = mid - 1;
		}
	}


	printf("%d", answer);

	free(arr);
	return 0;
}
```
