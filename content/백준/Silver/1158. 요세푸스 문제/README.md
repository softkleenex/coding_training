---
title: "[Silver IV] 요세푸스 문제 - 1158"
tags: ["백준", "Silver IV"]
---

# [Silver IV] 요세푸스 문제 - 1158 

[문제 링크](https://www.acmicpc.net/problem/1158) 

### 성능 요약

메모리: 1116 KB, 시간: 1840 ms

### 분류

구현, 자료 구조, 큐

### 제출 일자

2024년 10월 9일 22:51:17

### 문제 설명

<p>요세푸스 문제는 다음과 같다.</p>

<p>1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.</p>

<p>N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)</p>

### 출력 

 <p>예제와 같이 요세푸스 순열을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int turn(int arr[], int len, int count, int* start) 
{
	//start는 비어있는 인덱스(초기값은 0), 비어있는 부분은 0,
	
	int temp = 0;
	while (1) {
		*start = (*start + 1) % len;
		if (*start == 0)
		{
			(*start)++;//index0은 무조건 무효!
		}


		if (arr[*start] != 0)
			temp++;

		if (temp == count)
			break;
	}
	
	int data = arr[*start];
	arr[*start] = 0;
	return data;
}
//[0 1 2 3 4 5 6 7] 0 ~ 7,  len은 8

int main() {
	int N; scanf("%d", &N); N++;
	int* arr = NULL; 
	arr = (int*)malloc(sizeof(int) * N);

	for (int a = 1; a < N; a++)
	{
		arr[a] = a;
	}


	

	int count = 0; scanf("%d", &count);

	int* ans = NULL;
	ans = (int*)calloc(sizeof(int), (N-1));
	int start = 0;

	for (int a = 0; a < N - 1; a++)
	{
		//printf("%d\n", ans[a]);

		ans[a] = turn(arr, N, count, &start);

		//printf("%d\n", ans[a]);
	}


	
	printf("<");
	
	for (int a = 0; a < N - 1; a++)
	{
		printf("%d", ans[a]);
		if (a < N - 2)
		{
			printf(", ");
		}
	}

	printf(">", ans[N-2]);


	return 0;
}
```
