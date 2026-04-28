---
title: "[Silver II] 최대 힙 - 11279"
tags: ["백준", "Silver II"]
---

# [Silver II] 최대 힙 - 11279 

[문제 링크](https://www.acmicpc.net/problem/11279) 

### 성능 요약

메모리: 1504 KB, 시간: 20 ms

### 분류

자료 구조, 우선순위 큐

### 제출 일자

2026년 04월 25일 22:04:59

### 문제 설명

<p>널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.</p>

<ol>
	<li>배열에 자연수 x를 넣는다.</li>
	<li>배열에서 가장 큰 값을 출력하고, <span style="line-height:1.6em">그 값을 배열에서 제거한다. </span></li>
</ol>

<p><span style="line-height:1.6em">프로그램은 처음에 비어있는 배열에서 시작하게 된다.</span></p>

### 입력 

 <p>첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 2<sup>31</sup>보다 작다.</p>

### 출력 

 <p>입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```cpp
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define left(a) a*2+1
#define right(a) a*2+2
#define parent(a) a == 0 ? 0 : (a-1)/2
#define swap(a, b) {int temp = a; a = b; b = temp;}


int my_index = -1;
int arr[100000];


void printarr()
{
	printf("%d, arr:", my_index);
	for (int a = 0; a <= my_index; a++)
	{
		printf("%d ", arr[a]);
	}
	printf("\n");
}

int in_check(int now_index)
{
	if (arr[parent(now_index)] >= arr[now_index])
	{
		return 0;
	}
	else if (arr[parent(now_index)] < arr[now_index])
	{
		swap(arr[parent(now_index)], arr[now_index]);
		now_index = parent(now_index);
	}

	in_check(now_index);

	return 0;
}


void in(int term)
{
	my_index++;
	arr[my_index] = term;
	in_check(my_index);
}




int pop_check(int now_index) {
	int cases = 0;
	if (left(now_index) > my_index)
		cases = 0;
	if (left(now_index) <= my_index)
		cases = 1;
	if (right(now_index) <= my_index)
		cases = 2;

	switch (cases)
	{
	case 0:
		break;
	case 1:
		if (arr[now_index] < arr[left(now_index)])
		{
			swap(arr[now_index], arr[left(now_index)]); now_index = left(now_index);
		}
		else
		{
			return 0;
		}
		break;
	case 2:
	{
		int maxindex = (arr[left(now_index)] > arr[right(now_index)]) ? (left(now_index)) : (right(now_index));

		if(arr[now_index] < arr[maxindex])
		{
			swap(arr[now_index], arr[maxindex]);
			now_index = maxindex;
			pop_check(now_index);
		}
		else {
			return 0;
		}
		break;
	}
	default:
		break;
	}

	return 0;
}


void pop()
{
	if (my_index == -1)
	{
		printf("0\n");//제출 전에 0으로 수정
	}
	else
	{
		printf("%d\n", arr[0]);
		swap(arr[my_index], arr[0]);
		my_index--;
		pop_check(0);
	}

}

/*0
1 2
34 56
78 910 11 12
*/

int main() {
	int N; scanf("%d", &N);
	



	for (int a = 0; a < N; a++)
	{
		scanf("%d", &arr[a]);
	}

	for (int a = 0; a < N; a++)
	{
		int term = arr[a];
		switch (term)
		{
		case 0:
			//printf("pop\n");
			pop();
			//printarr();
			break;
		default:
			//printf("in\n");
			in(term);
			//printarr();
			break;
		}
	}



	return 0;
}
```
