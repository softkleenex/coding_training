---
title: "[Bronze I] 알고리즘 수업 - 선택 정렬 2 - 23882"
tags: ["백준", "Bronze I"]
---

# [Bronze I] 알고리즘 수업 - 선택 정렬 2 - 23882 

[문제 링크](https://www.acmicpc.net/problem/23882) 

### 성능 요약

메모리: 1116 KB, 시간: 52 ms

### 분류

구현, 정렬, 시뮬레이션

### 제출 일자

2024년 10월 22일 19:58:17

### 문제 설명

<p>오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 <em>K </em>번 교환이 발생한 직후의 배열 A를 출력해 보자.</p>

<p>크기가 <em>N</em>인 배열에 대한 선택 정렬 의사 코드는 다음과 같다.</p>

<pre>selection_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for last <- N downto 2 {
        A[1..last]중 가장 큰 수 A[i]를 찾는다
        if (last != i) then A[last] <-> A[i]  # last와 i가 서로 다르면 A[last]와 A[i]를 교환
    }
}</pre>

### 입력 

 <p>첫째 줄에 배열 A의 크기 <em>N</em>(5 ≤ <em>N</em> ≤ 10,000), 교환 횟수 <em>K</em>(1 ≤ <em>K</em> ≤ N)가 주어진다.</p>

<p>다음 줄에 서로 다른 배열 A의 원소 A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>이 주어진다. (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>)</p>

### 출력 

 <p> <em>K </em>번 교환이 발생한 직후의 배열 A를 한 줄에 출력한다. 교환 횟수가 <em>K </em>보다 작으면 -1을 출력한다.</p>



---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->


## 💻 코드

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<string.h>
#include<stdlib.h>


void sort(int arr[], int len, int try)
{
	int index_last = len-1;

	for (int a = 0; a < try; a++)
	{
		int index_max = 0;
		for (int b = 0; b <= index_last; b++)
		{
			index_max = arr[index_max] > arr[b] ? index_max : b;
		}

		int max = arr[index_max];
		arr[index_max] = arr[index_last];
		arr[index_last] = max;
		index_last == index_max ? try++ : try;//미교관시에 try 보정
		index_last--;
		if (index_last == -1)
		{
			printf("-1"); exit(0);
		}



	}



	for (int a = 0; a < len; a++)
	{
		printf("%d", arr[a]);
		if (a < len - 1)
			printf(" ");
	}


	//arr print
}

int main() {
	int len = 0; scanf("%d", &len);
	int try = 0; scanf("%d", &try);
	int* arr1 = (int*)malloc(sizeof(int) * len);


	for (int a = 0; a < len; a++)
	{
		scanf("%d", &arr1[a]);
	}
	
	sort(arr1, len, try);

	return 0;
}
```
